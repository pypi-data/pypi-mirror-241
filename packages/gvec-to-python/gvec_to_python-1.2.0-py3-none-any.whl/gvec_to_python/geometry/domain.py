import numpy as np
from scipy.optimize import newton

from gvec_to_python.geometry.kernels import matmul_5d_kernel, matvec_5d_kernel, transpose_5d_kernel


class GVEC_domain:
    """Provides four different mappings from a logical (computational) domain to the physical plasma domain (in Euclidean space).
    There are five different coordinate systems used:

    a. Cartesian coordiantes (x, y, z) in R^3.
    b. R-Z-phi coordinates, termed (q1, q2, ze) in R^2 x [0, 2*pi]. (q1, q2) span the R-Z Cartesian plane and (ze) is the toroidal angle.
    c. Gvec (or Vmec) coordinates (s, th, ze) in [0, 1] x [0, 2*pi]^2. (s) is the radial coordinate (s=1 corresponds to the last closed flux surface).
    d. Gvec straight-field-line coordinates (PEST), denoted (s2, th2, ze2) in [0, 1] x [0, 2*pi]^2. (th2) is theta-star.
    e. Struphy unit cube coordinates (s, u, v) in [0, 1]^3.

    The four mappings provided by the class are:

    1. f_gvec: (s, th, ze) -> (x, y, z)     ... standard gvec mapping
    2. f_pest: (s2, th2, ze2) -> (x, y, z)  ... gvec straight-field-line mapping
    3. f_unit: (s, u, v) -> (x, y, z)       ... gvec with unit cube as logical domain
    4. f_unit_pest : (s, u, v) -> (x, y, z) ... gvec straight-field-line with unit cube as logical domain
    
    There is also a fifth mapping to R-Z-phi coordinates:
    
    5. f_wo_hmap: (s, th, ze) -> (X1, X2, ze) ... Mapping to X1,X2,zeta. For default torus (hmap=1), (R,Z,phi)=(X1,X2,-zeta)

    All five mappings have a polar singulatiry at s=0 (resp. s2=0). The mappings are compositions of sub-functions:

    f_gvec = h ° X
    f_pest = f_gvec ° P
    f_unit = f_gvec ° L
    f_unit_pest = f_pest ° L
    f_wo_hmap = X 

    where

    X: (s, th, ze) -> (q1, q2, ze) is computed by GVEC's minimization algorithm, and represented in a spline x Fourier^2 basis.
    h: (q1, q2, ze) -> (x, y, z) is a simple torus (but could be easily generalized, called hmap in gvec):
        x = q1*cos(ze)
        y = -q1*sin(ze)
        z = q2
    P: (s2, th2, ze2) -> (s, th, ze) defines a pullback to the straight-field-line coordinates (s2, th2, ze2). The inverse is given by
        s2 = s
        th2 = th + lambda(s, th, ze)
        ze2 = ze
    L: (s, u, v) -> (s, th, ze) defines a pullback to the unit cube (can also map to PEST coordinates).
        s = s
        th = 2*pi*u
        ze = 2*pi*v*tor_fraction     where tor_fraction is 1 for the full torus, 1/nfp for one field period  

    The following methods can be called for f_gvec (for the other mappings, substitute "_gvec" by the resp. appendix):
    self.f_gvec      ... mapping
    self.df_gvec     ... Jacobian matrix
    self.det_df_gvec ... Jacobian determinant
    self.df_gvec_inv ... inverse Jacobian matrix
    self.g_gvec      ... metric tensor
    self.g_gvec_inv  ... inverse metric tensor

    Evaluation points can be float or array-like (1d or 3d).

    There are also three @staticmethods prepare_args, swap_J_axes and matmul_5d.

    Parameters
    ----------
        X1_base, X2_base, LA_base : obj
            gvec_to_python Base object.

        X1_coef : np.array
            The coefficients of the map q1 = X1(s, th, ze) in the spline-Fourier basis. (toroidal angle zeta in [0,2pi] on the full torus)

        X2_coef : np.array
            The coefficients of the map q2 = X2(s, th, ze) in the spline-Fourier basis. (toroidal angle zeta in [0,2pi] on the full torus)

        LA_coef : np.array
            The coefficients of lambda(s, th, ze) in the spline-Fourier basis. (toroidal angle zeta in [0,2pi] on the full torus)

        nfp : int
            Number of field periods in the equilibrium.

        unit_tor_domain : string
            Needed only for toroidal angle v in "unit" mappings. Defines the extend of the domain in toroidal direction. 
            v in [0, 1] maps to zeta=2*pi*v*tor_fraction 
            - "full"  :  v in [0, 1] maps to the full torus, tor_fraction=1.0.  [DEFAULT]
            - "one-fp":  v in [0, 1] maps to one field period, tor_fraction=1/nfp
            -  "2/3" or "0.5"  :  string of any meaningful float or ratio  for tor_fraction, must be >0 and <=1, defines a fraction of the full torus.
             

        use_pyccel : bool
            Whether to use pyccel kernels for matrix operations.
    """

    def __init__(self, X1_base, X2_base, LA_base, X1_coef, X2_coef, LA_coef, nfp, unit_tor_domain="full", use_pyccel=False):

        self._X1_base = X1_base
        self._X2_base = X2_base
        self._LA_base = LA_base
        self._nfp = nfp
        self._unit_tor_domain = unit_tor_domain
        if unit_tor_domain=="full":
            self._tor_fraction = 1.0
        elif unit_tor_domain=="one-fp":
            self._tor_fraction = 1.0/nfp
        else:
            exec( "self._tor_fraction = "+ unit_tor_domain ) # executes the setting of _tor_fraction
            assert ((np.amin(self._tor_fraction)>0.0) and (np.amax(self._tor_fraction)<=1.0)) , ("`tor_fraction` must be >0 and <=1. but is %f" % self._tor_fraction )

        self._X1_coef = X1_coef
        self._X2_coef = X2_coef
        self._LA_coef = LA_coef

        self._use_pyccel = use_pyccel

    @property
    def X1_base(self):
        '''Basis object for X1 mapping.'''
        return self._X1_base

    @property
    def X2_base(self):
        '''Basis object for X2 mapping.'''
        return self._X2_base

    @property
    def LA_base(self):
        '''Basis object for lambda.'''
        return self._LA_base

    @property
    def X1_coef(self):
        '''The coefficients of the map q1 = X1(s, u, v) in the spline-Fourier basis.'''
        return self._X1_coef

    @property
    def X2_coef(self):
        '''The coefficients of the map q2 = X2(s, u, v) in the spline-Fourier basis.'''
        return self._X2_coef

    @property
    def LA_coef(self):
        '''The coefficients of lambda(s, u, v) in the spline-Fourier basis.'''
        return self._LA_coef

    @property
    def unit_tor_domain(self):
        '''unit_tor_domain : string
            Needed for toroidal angle v in "unit" mappings. Defines the extent of the domain in toroidal direction
             - "full"  :  v in [0, 1] maps to the full torus. (default)
             - "one-fp":  v in [0, 1] maps to one field period,  i.e. zeta = 2*pi/nfp*v
             - "2"     :  string of any meaningful positive number, full torus will be divided by that integer '''
        return self._unit_tor_domain

    @property
    def nfp(self):
        '''Number of field periods in the equilibrium.'''
        return self._nfp

    @property
    def tor_fraction(self):
        '''for unit mappings, how v in [0, 1] maps to the full torus, zeta=[0,2pi*tor_fraction]'''
        return self._tor_fraction

    @property
    def use_pyccel(self):
        '''Boolean, whether to use pyccel kernels for matrix multiplications.'''
        return self._use_pyccel

    # standard gvec coordinates
    def f_gvec(self, s, th, ze):
        '''The map f_gvec:(s, th, ze) -> (x, y, z), where (s, th, ze) in [0, 1] x [0, 2*pi]^2 and (x, y, z) are the Cartesian coordinates.

        Parameters
        ----------
            s, th, ze : float or array-like
                Coordinates in [0, 1] x [0, 2*pi]^2. If list or np.array, must be either 1d (meshgrid evaluation) or 3d numpy arrays.

        Returns
        -------
            A 3-tuple of either floats (single-point evaluation) or 3d numpy arrays
        '''
        return self.hmap(*self.Xmap(s, th, ze))

    def df_gvec(self, s, th, ze):
        '''The Jacobian matrix of f_gvec.

        Parameters
        ----------
            s, th, ze : float or array-like
                Coordinates in [0, 1] x [0, 2*pi]^2. If list or np.array, must be either 1d (meshgrid evaluation) or 3d numpy arrays.

        Returns
        -------
            A 2d numpy array (single-point evaluation) or a 5d numpy array, 
            with the last two indices referring to the Jacobian entries at each point.'''

        tmp1 = self.dX(s, th, ze)  # Jacobian of the Xmap
        tmp2 = self.dh(*self.Xmap(s, th, ze))  # Jacobian of the hmap

        # meshgrid evaluation
        if tmp1.ndim == 5:
            out = self.matmul_5d(tmp2, tmp1, use_pyccel=self.use_pyccel)
        # single-point evaluation
        else:
            out = tmp2 @ tmp1

        return out

    def det_df_gvec(self, s, th, ze):
        '''The Jacobian determinant of f_gvec.

        Parameters
        ----------
            s, th, ze : float or array-like
                Coordinates in [0, 1] x [0, 2*pi]^2. If list or np.array, must be either 1d (meshgrid evaluation) or 3d numpy arrays.

        Returns
        -------
            A float (single-point evaluation) or a 3d numpy array (meshgrid evaluation).'''

        tmp1 = self.det_dX(s, th, ze)
        tmp2 = self.det_dh(*self.Xmap(s, th, ze))
        return tmp1 * tmp2

    def df_gvec_inv(self, s, th, ze):
        '''The inverse Jacobian matrix of f_gvec.

        Parameters
        ----------
            s, th, ze : float or array-like
                Coordinates in [0, 1] x [0, 2*pi]^2. If list or np.array, must be either 1d (meshgrid evaluation) or 3d numpy arrays.

        Returns
        -------
            A 2d numpy array (single-point evaluation) or a 5d numpy array.'''

        return np.linalg.inv(self.df_gvec(s, th, ze))

    def g_gvec(self, s, th, ze):
        '''The metric tensor of f_gvec.

        Parameters
        ----------
            s, th, ze : float or array-like
                Coordinates in [0, 1] x [0, 2*pi]^2. If list or np.array, must be either 1d (meshgrid evaluation) or 3d numpy arrays.

        Returns
        -------
            A 2d numpy array (single-point evaluation) or a 5d numpy array.'''

        tmp = np.ascontiguousarray(self.df_gvec(s, th, ze))  # Jacobian of f_gvec

        # meshgrid evaluation
        if tmp.ndim == 5:
            out = self.matmul_5d(tmp, tmp, transpose_a=True, use_pyccel=self.use_pyccel)
        # single-point evaluation
        else:
            out = tmp.T @ tmp

        return out

    def g_gvec_inv(self, s, th, ze):
        '''Inverse metric tensor of f_gvec.

        Parameters
        ----------
            s, th, ze : float or array-like
                Coordinates in [0, 1] x [0, 2*pi]^2. If list or np.array, must be either 1d (meshgrid evaluation) or 3d numpy arrays.

        Returns
        -------
            A 2d numpy array (single-point evaluation) or a 5d numpy array.'''

        return np.linalg.inv(self.g_gvec(s, th, ze))

    def dg_gvec(self, s, th, ze, der=None):
        '''Partial derivative of the metric tensor. der in  {"s", "th", "ze"} indicates which derivative to evaluate.'''

        if der is None:
            return self.g_gvec(s, th, ze)
        elif der == 's':
            comp = 0
        elif der == 'th':
            comp = 1
        elif der == 'ze':
            comp = 2
        else:
            raise ValueError(f'Derivative {der} not defined.')

        dX = self.dX(s, th, ze)
        ddX_di = self.ddX(s, th, ze)[comp]

        gh = self.gh(*self.Xmap(s, th, ze))
        dgh_dq1 = self.dgh_dq1(*self.Xmap(s, th, ze))

        # meshgrid evaluation
        if dX.ndim == 5:
            dq1_di = dX[:, :, :, 0, comp]
            dgh_di = self.swap_J_axes(self.swap_J_back(dgh_dq1) * dq1_di)
        
            tmp1 = self.matmul_5d(gh, dX, use_pyccel=self.use_pyccel)
            tmp2 = self.matmul_5d(dgh_di, dX, use_pyccel=self.use_pyccel)
            tmp3 = self.matmul_5d(gh, ddX_di, use_pyccel=self.use_pyccel)

            term1 = self.matmul_5d(ddX_di, tmp1, transpose_a=True, use_pyccel=self.use_pyccel)
            term2 = self.matmul_5d(dX, tmp2, transpose_a=True, use_pyccel=self.use_pyccel)
            term3 = self.matmul_5d(dX, tmp3, transpose_a=True, use_pyccel=self.use_pyccel)
        # single point evaluation
        else:
            dq1_di = dX[0, comp]
            dgh_di = dgh_dq1 * dq1_di
        
            tmp1 = gh @ dX    
            tmp2 = dgh_di @ dX
            tmp3 = gh @ ddX_di

            term1 = ddX_di.T @ tmp1
            term2 = dX.T @ tmp2
            term3 = dX.T @ tmp3

        return term1 + term2 + term3

    def dJ_gvec(self, s, th, ze, der=None):
        '''Partial derivative of Jacobian determinant. der in  {"s", "th", "ze"} indicates which derivative to evaluate.'''

        if der is None:
            return self.det_df_gvec(s, th, ze)
        elif der == 's':
            comp = 0
        elif der == 'th':
            comp = 1
        elif der == 'ze':
            comp = 2
        else:
            raise ValueError(f'Derivative {der} not defined.')

        dX = self.dX(s, th, ze)

        # meshgrid evaluation
        if dX.ndim == 5:
            dq1_di = dX[:, :, :, 0, comp]
        # single point evaluation
        else:
            dq1_di = dX[0, comp]

        q1, q2, ze2 = self.Xmap(s, th, ze)

        return dq1_di * self.det_dX(s, th, ze) + self.det_dh(q1, q2, ze2) * self.dJ_X(s, th, ze)[comp]

    # gvec_pest coordinates
    def f_pest(self, s2, th2, ze2):
        '''The map f_pest:(s2, th2, ze2) -> (x, y, z), where (s2, th2, ze2) in [0, 1] x [0, 2*pi]^2 are straight-field-line coordinates (PEST)
        and (x, y, z) are the Cartesian coordinates.

        Parameters
        ----------
            s2, th2, ze2 : float or array-like
                Coordinates in [0, 1] x [0, 2*pi]^2. If list or np.array, must be either 1d (meshgrid evaluation) or 3d numpy arrays.

        Returns
        -------
            A 3-tuple of either floats (single-point evaluation) or 3d numpy arrays (meshgrid evaluation).
        '''
        return self.f_gvec(*self.Pmap(s2, th2, ze2))

    def df_pest(self, s2, th2, ze2):
        '''The Jacobian matrix of f_pest.

        Parameters
        ----------
            s2, th2, ze2 : float or array-like
                Coordinates in [0, 1] x [0, 2*pi]^2. If list or np.array, must be either 1d (meshgrid evaluation) or 3d numpy arrays.

        Returns
        -------
            A 2d numpy array (single-point evaluation) or a 5d numpy array, 
            with the last two indices referring to the Jacobian entries at each point.'''

        tmp1 = self.dP(s2, th2, ze2)  # Jacobian of the Pmap
        tmp2 = self.df_gvec(*self.Pmap(s2, th2, ze2))  # Jacobian of f_gvec

        # meshgrid evaluation
        if tmp1.ndim == 5:
            out = self.matmul_5d(tmp2, tmp1, use_pyccel=self.use_pyccel)
        # single-point evaluation
        else:
            out = tmp2 @ tmp1

        return out

    def det_df_pest(self, s2, th2, ze2):
        '''The Jacobian determinant of f_pest.

        Parameters
        ----------
            s2, th2, ze2 : float or array-like
                Coordinates in [0, 1] x [0, 2*pi]^2. If list or np.array, must be either 1d (meshgrid evaluation) or 3d numpy arrays.

        Returns
        -------
            A float (single-point evaluation) or a 3d numpy array (meshgrid evaluation).'''

        tmp1 = self.det_dP(s2, th2, ze2)
        tmp2 = self.det_df_gvec(*self.Pmap(s2, th2, ze2))
        return tmp1 * tmp2

    def df_pest_inv(self, s2, th2, ze2):
        '''The inverse Jacobian matrix of f_pest.

        Parameters
        ----------
            s2, th2, ze2 : float or array-like
                Coordinates in [0, 1] x [0, 2*pi]^2. If list or np.array, must be either 1d (meshgrid evaluation) or 3d numpy arrays.

        Returns
        -------
            A 2d numpy array (single-point evaluation) or a 5d numpy array.'''

        return np.linalg.inv(self.df_pest(s2, th2, ze2))

    def g_pest(self, s2, th2, ze2):
        '''The metric tensor of f_pest.

        Parameters
        ----------
            s2, th2, ze2 : float or array-like
                Coordinates in [0, 1] x [0, 2*pi]^2. If list or np.array, must be either 1d (meshgrid evaluation) or 3d numpy arrays.

        Returns
        -------
            A 2d numpy array (single-point evaluation) or a 5d numpy array.'''

        tmp = np.ascontiguousarray(self.df_pest(s2, th2, ze2))  # Jacobian of f_gvec

        # meshgrid evaluation
        if tmp.ndim == 5:
            out = self.matmul_5d(tmp, tmp, transpose_a=True, use_pyccel=self.use_pyccel)
        # single-point evaluation
        else:
            out = tmp.T @ tmp

        return out

    def g_pest_inv(self, s2, th2, ze2):
        '''Inverse metric tensor of f_pest.

        Parameters
        ----------
            s2, th2, ze2 : float or array-like
                Coordinates in [0, 1] x [0, 2*pi]^2. If list or np.array, must be either 1d (meshgrid evaluation) or 3d numpy arrays.

        Returns
        -------
            A 2d numpy array (single-point evaluation) or a 5d numpy array.'''

        return np.linalg.inv(self.g_pest(s2, th2, ze2))

    # unit cube coordinates
    def f_unit(self, s, u, v):
        '''The map f_unit:(s, u, v) -> (x, y, z), where (s, u, v) in [0, 1]^3 and (x, y, z) are the Cartesian coordinates.

        Parameters
        ----------
            s, u, v : float or array-like
                Coordinates in [0, 1]^3. If list or np.array, must be either 1d (meshgrid evaluation) or 3d numpy arrays.

        Returns
        -------
            A 3-tuple of either floats (single-point evaluation) or 3d numpy arrays (meshgrid evaluation).
        '''
        return self.f_gvec(*self.Lmap(s, u, v))

    def df_unit(self, s, u, v):
        '''The Jacobian matrix of f_unit.

        Parameters
        ----------
            s, u, v : float or array-like
                Coordinates in [0, 1]^3. If list or np.array, must be either 1d (meshgrid evaluation) or 3d numpy arrays.

        Returns
        -------
            A 2d numpy array (single-point evaluation) or a 5d numpy array, 
            with the last two indices referring to the Jacobian entries at each point.'''

        tmp1 = self.dL(s, u, v)  # Jacobian of the Lmap
        tmp2 = self.df_gvec(*self.Lmap(s, u, v))  # Jacobian of f_gvec

        # meshgrid evaluation
        if tmp1.ndim == 5:
            out = self.matmul_5d(tmp2, tmp1, use_pyccel=self.use_pyccel)
        # single-point evaluation
        else:
            out = tmp2 @ tmp1

        return out

    def det_df_unit(self, s, u, v):
        '''The Jacobian determinant of f_unit.

        Parameters
        ----------
            s, u, v : float or array-like
                Coordinates in [0, 1]^3. If list or np.array, must be either 1d (meshgrid evaluation) or 3d numpy arrays.

        Returns
        -------
            A float (single-point evaluation) or a 3d numpy array (meshgrid evaluation).
        '''
        return self.det_df_gvec(*self.Lmap(s, u, v)) * (2*np.pi)**2*self.tor_fraction

    def df_unit_inv(self, s, u, v):
        '''The inverse Jacobian matrix of f_unit.

        Parameters
        ----------
            s, u, v : float or array-like
                Coordinates in [0, 1]^3. If list or np.array, must be either 1d (meshgrid evaluation) or 3d numpy arrays.

        Returns
        -------
            A 2d numpy array (single-point evaluation) or a 5d numpy array.'''

        return np.linalg.inv(self.df_unit(s, u, v))

    def g_unit(self, s, u, v):
        '''The metric tensor of f_unit.

        Parameters
        ----------
            s, u, v : float or array-like
                Coordinates in [0, 1]^3. If list or np.array, must be either 1d (meshgrid evaluation) or 3d numpy arrays.

        Returns
        -------
            A 2d numpy array (single-point evaluation) or a 5d numpy array.'''

        tmp = np.ascontiguousarray(self.df_unit(s, u, v))  # Jacobian of f_unit

        # meshgrid evaluation
        if tmp.ndim == 5:
            out = self.matmul_5d(tmp, tmp, transpose_a=True, use_pyccel=self.use_pyccel)
        # single-point evaluation
        else:
            out = tmp.T @ tmp

        return out

    def g_unit_inv(self, s, u, v):
        '''The inverse metric tensor of f_unit.

        Parameters
        ----------
            s, u, v : float or array-like
                Coordinates in [0, 1]^3. If list or np.array, must be either 1d (meshgrid evaluation) or 3d numpy arrays.

        Returns
        -------
            A 2d numpy array (single-point evaluation) or a 5d numpy array.'''

        return np.linalg.inv(self.g_unit(s, u, v))

    # unit cube pest coordinates
    def f_unit_pest(self, s, u, v):
        '''The map f_unit_pest:(s, u, v) -> (x, y, z), where (s, u, v) in [0, 1]^3 are straight-field-line coordinates (PEST)
        and (x, y, z) are the Cartesian coordinates.

        Parameters
        ----------
            s, u, v : float or array-like
                Coordinates in [0, 1]^3. If list or np.array, must be either 1d (meshgrid evaluation) or 3d numpy arrays.

        Returns
        -------
            A 3-tuple of either floats (single-point evaluation) or 3d numpy arrays (meshgrid evaluation).
        '''
        return self.f_pest(*self.Lmap(s, u, v))

    def df_unit_pest(self, s, u, v):
        '''The Jacobian matrix of f_unit_pest.

        Parameters
        ----------
            s, u, v : float or array-like
                Coordinates in [0, 1]^3. If list or np.array, must be either 1d (meshgrid evaluation) or 3d numpy arrays.

        Returns
        -------
            A 2d numpy array (single-point evaluation) or a 5d numpy array, 
            with the last two indices referring to the Jacobian entries at each point.'''

        tmp1 = self.dL(s, u, v)  # Jacobian of the Lmap
        tmp2 = self.df_pest(*self.Lmap(s, u, v))  # Jacobian of f_pest

        # meshgrid evaluation
        if tmp1.ndim == 5:
            out = self.matmul_5d(tmp2, tmp1, use_pyccel=self.use_pyccel)
        # single-point evaluation
        else:
            out = tmp2 @ tmp1

        return out

    def det_df_unit_pest(self, s, u, v):
        '''The Jacobian determinant of f_unit_pest.

        Parameters
        ----------
            s, u, v : float or array-like
                Coordinates in [0, 1]^3. If list or np.array, must be either 1d (meshgrid evaluation) or 3d numpy arrays.

        Returns
        -------
            A float (single-point evaluation) or a 3d numpy array (meshgrid evaluation).
        '''
        return self.det_df_pest(*self.Lmap(s, u, v)) * (2*np.pi)**2*self.tor_fraction

    def df_unit_pest_inv(self, s, u, v):
        '''The inverse Jacobian matrix of f_unit_pest.

        Parameters
        ----------
            s, u, v : float or array-like
                Coordinates in [0, 1]^3. If list or np.array, must be either 1d (meshgrid evaluation) or 3d numpy arrays.

        Returns
        -------
            A 2d numpy array (single-point evaluation) or a 5d numpy array.'''

        return np.linalg.inv(self.df_unit_pest(s, u, v))

    def g_unit_pest(self, s, u, v):
        '''The metric tensor of f_unit_pest.

        Parameters
        ----------
            s, u, v : float or array-like
                Coordinates in [0, 1]^3. If list or np.array, must be either 1d (meshgrid evaluation) or 3d numpy arrays.

        Returns
        -------
            A 2d numpy array (single-point evaluation) or a 5d numpy array.'''

        tmp = np.ascontiguousarray(self.df_unit_pest(s, u, v))  # Jacobian of f_unit_pest

        # meshgrid evaluation
        if tmp.ndim == 5:
            out = self.matmul_5d(tmp, tmp, transpose_a=True, use_pyccel=self.use_pyccel)
        # single-point evaluation
        else:
            out = tmp.T @ tmp

        return out

    def g_unit_pest_inv(self, s, u, v):
        '''The inverse metric tensor of f_unit_pest.

        Parameters
        ----------
            s, u, v : float or array-like
                Coordinates in [0, 1]^3. If list or np.array, must be either 1d (meshgrid evaluation) or 3d numpy arrays.

        Returns
        -------
            A 2d numpy array (single-point evaluation) or a 5d numpy array.'''

        return np.linalg.inv(self.g_unit_pest(s, u, v))

    # R-Z-phi coordinates
    def f_wo_hmap(self, s, th, ze):
        '''The map f_wo_hmap:(s, th, ze) -> (q1, q2, ze), where (s, th, ze) in [0, 1] x [0, 2*pi]^2 and (q1, q2, ze) R-Z-phi coordinates.

        Parameters
        ----------
            s, th, ze : float or array-like
                Coordinates in [0, 1] x [0, 2*pi]^2. If list or np.array, must be either 1d (meshgrid evaluation) or 3d numpy arrays.

        Returns
        -------
            A 3-tuple of either floats (single-point evaluation) or 3d numpy arrays.
        '''
        return self.Xmap(s, th, ze)

    def df_wo_hmap(self, s, th, ze):
        '''The Jacobian matrix of f_wo_hmap.

        Parameters
        ----------
            s, th, ze : float or array-like
                Coordinates in [0, 1] x [0, 2*pi]^2. If list or np.array, must be either 1d (meshgrid evaluation) or 3d numpy arrays.

        Returns
        -------
            A 2d numpy array (single-point evaluation) or a 5d numpy array, 
            with the last two indices referring to the Jacobian entries at each point.
        '''
        return self.dX(s, th, ze)

    def det_df_wo_hmap(self, s, th, ze):
        '''The Jacobian determinant of f_wo_hmap.

        Parameters
        ----------
            s, th, ze : float or array-like
                Coordinates in [0, 1] x [0, 2*pi]^2. If list or np.array, must be either 1d (meshgrid evaluation) or 3d numpy arrays.

        Returns
        -------
            A float (single-point evaluation) or a 3d numpy array.
        '''
        return self.det_dX(s, th, ze)

    def df_wo_hmap_inv(self, s, th, ze):
        '''The inverse Jacobian matrix of f_wo_hmap.

        Parameters
        ----------
            s, th, ze : float or array-like
                Coordinates in [0, 1] x [0, 2*pi]^2. If list or np.array, must be either 1d (meshgrid evaluation) or 3d numpy arrays.

        Returns
        -------
            A 2d numpy array (single-point evaluation) or a 5d numpy array.'''

        return np.linalg.inv(self.df_wo_hmap(s, th, ze))

    def g_wo_hmap(self, s, th, ze):
        '''The metric tensor of f_wo_hmap.

        Parameters
        ----------
            s, th, ze : float or array-like
                Coordinates in [0, 1] x [0, 2*pi]^2. If list or np.array, must be either 1d (meshgrid evaluation) or 3d numpy arrays.

        Returns
        -------
            A 2d numpy array (single-point evaluation) or a 5d numpy array.'''

        tmp = np.ascontiguousarray(self.df_wo_hmap(s, th, ze))  # Jacobian of f_wo_hmap

        # meshgrid evaluation
        if tmp.ndim == 5:
            out = self.matmul_5d(tmp, tmp, transpose_a=True, use_pyccel=self.use_pyccel)
        # single-point evaluation
        else:
            out = tmp.T @ tmp

        return out

    def g_wo_hmap_inv(self, s, th, ze):
        '''Inverse metric tensor of f_wo_hmap.

        Parameters
        ----------
            s, th, ze : float or array-like
                Coordinates in [0, 1] x [0, 2*pi]^2. If list or np.array, must be either 1d (meshgrid evaluation) or 3d numpy arrays.

        Returns
        -------
            A 2d numpy array (single-point evaluation) or a 5d numpy array.'''

        return np.linalg.inv(self.g_wo_hmap(s, th, ze))


    # ---------------
    # Helper methods
    # ---------------

    # Xmap
    def Xmap(self, s, th, ze):
        '''The map (q1, q2, ze) = X(s, th, ze) computed by GVEC's minimization algorithm.

        Parameters
        ----------
            s, th, ze : float or array-like
                Coordinates in [0, 1] x [0, 2*pi]^2. If list or np.array, must be either 1d (meshgrid evaluation) or 3d numpy arrays.

        Returns
        -------
            A 3-tuple of either floats (single-point evaluation) or 3d numpy arrays.'''

        s, th, ze = self.prepare_args(s, th, ze, sparse=False)

        q1 = self.X1_base.eval_stz(s, th, ze, self.X1_coef)
        q2 = self.X2_base.eval_stz(s, th, ze, self.X2_coef)
        ze = ze + 0*q1 # broadcast to correct shape

        return q1, q2, ze

    def dX(self, s, th, ze):
        '''Jacobian matrix of the Xmap.'''
        s, th, ze = self.prepare_args(s, th, ze)

        dX1ds = self.X1_base.eval_stz(s, th, ze, self.X1_coef, der='s')
        dX1dt = self.X1_base.eval_stz(s, th, ze, self.X1_coef, der='th')
        dX1dz = self.X1_base.eval_stz(s, th, ze, self.X1_coef, der='ze')

        dX2ds = self.X2_base.eval_stz(s, th, ze, self.X2_coef, der='s')
        dX2dt = self.X2_base.eval_stz(s, th, ze, self.X2_coef, der='th')
        dX2dz = self.X2_base.eval_stz(s, th, ze, self.X2_coef, der='ze')

        zmat = np.zeros_like(dX1ds)
        omat = np.ones_like(dX1ds)

        J = np.array(((dX1ds, dX1dt, dX1dz),
                      (dX2ds, dX2dt, dX2dz),
                      ( zmat,  zmat,  omat)))

        return self.swap_J_axes(J)

    def ddX(self, s, th, ze):
        '''Returns a 3-tuple for the three partial derivatives of dX w.r.t s, th and ze.'''
        s, th, ze = self.prepare_args(s, th, ze)

        # partial derivative dJ/ds
        ddX1_dds = self.X1_base.eval_stz(s, th, ze, self.X1_coef, der='ss')
        ddX1_dsdt = self.X1_base.eval_stz(s, th, ze, self.X1_coef, der='sth')
        ddX1_dsdz = self.X1_base.eval_stz(s, th, ze, self.X1_coef, der='sze')

        ddX2_dds = self.X2_base.eval_stz(s, th, ze, self.X2_coef, der='ss')
        ddX2_dsdt = self.X2_base.eval_stz(s, th, ze, self.X2_coef, der='sth')
        ddX2_dsdz = self.X2_base.eval_stz(s, th, ze, self.X2_coef, der='sze')

        zmat = np.zeros_like(ddX1_dds)

        J_s = np.array(((ddX1_dds, ddX1_dsdt, ddX1_dsdz),
                        (ddX2_dds, ddX2_dsdt, ddX2_dsdz),
                        (    zmat,      zmat,      zmat)))

        # partial derivative dJ/dth
        ddX1_ddt = self.X1_base.eval_stz(s, th, ze, self.X1_coef, der='thth')
        ddX1_dtdz = self.X1_base.eval_stz(s, th, ze, self.X1_coef, der='thze')

        ddX2_ddt = self.X2_base.eval_stz(s, th, ze, self.X2_coef, der='thth')
        ddX2_dtdz = self.X2_base.eval_stz(s, th, ze, self.X2_coef, der='thze')

        J_th = np.array(((ddX1_dsdt, ddX1_ddt, ddX1_dtdz),
                         (ddX2_dsdt, ddX2_ddt, ddX2_dtdz),
                         (     zmat,     zmat,      zmat)))

        # partial derivative dJ/dze
        ddX1_ddz = self.X1_base.eval_stz(s, th, ze, self.X1_coef, der='zeze')

        ddX2_ddz = self.X2_base.eval_stz(s, th, ze, self.X2_coef, der='zeze')

        J_ze = np.array(((ddX1_dsdz, ddX1_dtdz, ddX1_ddz),
                         (ddX2_dsdz, ddX2_dtdz, ddX2_ddz),
                         (     zmat,      zmat,     zmat)))

        return self.swap_J_axes(J_s), self.swap_J_axes(J_th), self.swap_J_axes(J_ze)

    def dX_inv(self, s, th, ze):
        '''Inverse Jacobian matrix of the Xmap.'''
        return np.linalg.inv(self.dX(s, th, ze))

    def det_dX(self, s, th, ze):
        '''Jacobian determinant of the Xmap.'''
        return np.linalg.det(self.dX(s, th, ze))

    def dJ_X(self, s, th, ze):
        '''Returns a 3-tuple for the three partial derivatives of det_dX w.r.t s, th and ze.'''

        dX = self.dX(s, th, ze)

        # meshgrid evaluation
        if dX.ndim == 5:
            dX1_ds = dX[:, :, :, 0, 0]
            dX2_ds = dX[:, :, :, 1, 0]
            dX1_dt = dX[:, :, :, 0, 1]
            dX2_dt = dX[:, :, :, 1, 1]
        # single point evaluation
        else:
            dX1_ds = dX[0, 0]
            dX2_ds = dX[1, 0]
            dX1_dt = dX[0, 1]
            dX2_dt = dX[1, 1]

        ddX = self.ddX(s, th, ze)
        
        tmp = []
        for n in range(3):
            # meshgrid evaluation
            if dX.ndim == 5:
                tmp += [ddX[n][:, :, :, 0, 0] * dX2_dt + ddX[n][:, :, :, 1, 1] * dX1_ds
                      - ddX[n][:, :, :, 1, 0] * dX1_dt - ddX[n][:, :, :, 0, 1] * dX2_ds]
            # single point evaluation
            #            X1ds/di * dX2_dt + dX1dt/di * dX1_ds 
            #           -X2ds/di * dX1_dt - dX2dt/di * dX2_ds 
            else:            
                tmp += [ddX[n][0, 0] * dX2_dt + ddX[n][1, 1] * dX1_ds
                      - ddX[n][1, 0] * dX1_dt - ddX[n][0, 1] * dX2_ds]

        return tmp[0], tmp[1], tmp[2]

    # hmap
    def hmap(self, q1, q2, ze):
        '''The map (x, y, z) = h(q1, q2, ze) which is a simple torus.

        Parameters
        ----------
            q1, q2, ze : float or array-like
                Coordinates in R^2 x [0, 2*pi]. If list or np.array, must be either 1d (meshgrid evaluation) or 3d numpy arrays.

        Returns
        -------
            A 3-tuple of either floats (single-point evaluation) or 3d numpy arrays.'''

        x = q1 * np.cos(ze)
        y = - q1 * np.sin(ze)
        z = q2
        return x, y, z

    def dh(self, q1, q2, ze):
        '''Jacobian matrix of the hmap.'''

        zmat = np.zeros_like(q1)
        omat = np.ones_like(q1)

        J = np.array(((np.cos(ze), zmat, -q1*np.sin(ze)),
                      (-np.sin(ze), zmat, -q1*np.cos(ze)),
                      (zmat, omat, zmat)))

        return self.swap_J_axes(J)

    def dh_inv(self, q1, q2, ze):
        '''Inverse Jacobian matrix of the hmap.'''
        return np.linalg.inv(self.dh(q1, q2, ze))

    def det_dh(self, q1, q2, ze):
        '''Jacobian determinant of the hmap.'''
        return np.linalg.det(self.dh(q1, q2, ze))

    def gh(self, q1, q2, ze):
        '''Metric tensor of hmap.'''

        zmat = np.zeros_like(q1)
        omat = np.ones_like(q1)

        J = np.array(((omat, zmat, zmat),
                      (zmat, omat, zmat),
                      (zmat, zmat, q1**2)))

        return self.swap_J_axes(J)

    def dgh_dq1(self, q1, q2, ze):
        '''Partial derivative of gh w.r.t q1.'''

        zmat = np.zeros_like(q1)

        J = np.array(((zmat, zmat, zmat),
                      (zmat, zmat, zmat),
                      (zmat, zmat, 2*q1)))

        return self.swap_J_axes(J)

    # Lmap
    def Lmap(self, s, u, v):
        '''The map (s, th, ze) = L(s, u, v) defined by th = 2*pi*u and ze = 2*pi*v/nfp with Jacobian determinant 4*pi^2/nfp.
        Here, the integer nfp>=1 indicates whether to use a toroidal field period in the mapping.

        Parameters
        ----------
            s, u, v : float or array-like
                Coordinates in [0, 1]^3. If list or np.array, must be either 1d (meshgrid evaluation) or 3d numpy arrays.

        Returns
        -------
            A 3-tuple of either floats (single-point evaluation) or 3d numpy arrays.'''

        s, u, v = self.prepare_args(s, u, v, sparse=False)
        return s, (2*np.pi)*u, (2*np.pi)*self.tor_fraction*v

    def dL(self, s, u, v):
        '''Jacobian matrix of the Lmap.'''

        s, u, v = self.prepare_args(s, u, v, sparse=False)
        zmat = np.zeros_like(s)
        omat = np.ones_like(s)

        J = np.array(((omat, zmat, zmat),
                      (zmat, omat*(2*np.pi), zmat),
                      (zmat, zmat, omat*(2*np.pi)*self.tor_fraction)))

        return self.swap_J_axes(J)

    def dL_inv(self, s, u, v):
        '''Inverse Jacobian matrix of the Lmap.'''

        s, u, v = self.prepare_args(s, u, v, sparse=False)
        zmat = np.zeros_like(s)
        omat = np.ones_like(s)

        J = np.array(((omat, zmat, zmat),
                      (zmat, omat/(2*np.pi), zmat),
                      (zmat, zmat, omat/((2*np.pi)*self.tor_fraction))))

        return self.swap_J_axes(J)

    def det_dL(self, s, u, v):
        '''Jacobian determinant of the Lmap.'''
        s, u, v = self.prepare_args(s, u, v, sparse=False)
        return np.ones_like(s) * (2*np.pi)**2 * self.tor_fraction

    # pest map
    def Pmap(self, s_in, th2_in, ze_in):
        '''The map (s, th, ze) = P(s, th2, ze) giving the gvec coordinates (s, th, ze) in [0, 1] x [0, 2*pi]^2
         in terms of straight-field-line (PEST) coordinates (s, th2, ze) in [0, 1] x [0, 2*pi]^2.

        Parameters
        ----------
            s_in, th2_in, ze_in : float or array-like
                PEST coordinates in [0, 1] x [0, 2*pi]^2. If list or np.array, must be either 1d (meshgrid evaluation) or 3d numpy arrays.

        Returns
        -------
            A 3-tuple of either floats (single-point evaluation) or 3d numpy arrays.'''

        def find_th(s_val,th2_val,ze_val):
            '''  1D root finder solving th+lambda(s,th,ze)-th2=0 for th, given s,th2,ze ''' 
            func   = lambda th: th + self.LA_base.eval_stz(s_val, th, ze_val, self.LA_coef) - th2_val
            fprime = lambda th: 1 + self.LA_base.eval_stz(s_val, th, ze_val, self.LA_coef, der='th')
            return newton(func, th2_val, fprime) #th2_val as startvalue

        s, th2, ze = self.prepare_args(s_in, th2_in, ze_in, sparse=True)
        vfind_th=np.vectorize(find_th, otypes=[float])
        th=vfind_th(s,th2,ze)

        return s + 0*th, th, ze + 0*th


    def dP(self, s2, th2, ze2):
        '''Jacobian of the Pmap.'''

        s, th, ze = self.Pmap(s2, th2, ze2)

        dlambda_ds = self.LA_base.eval_stz(s, th, ze, self.LA_coef, der='s')
        dlambda_dth = self.LA_base.eval_stz(s, th, ze, self.LA_coef, der='th')
        dlambda_dze = self.LA_base.eval_stz(s, th, ze, self.LA_coef, der='ze')

        dth_ds2 = - dlambda_ds / (1. + dlambda_dth)
        dth_dth2 = 1. / (1. + dlambda_dth)
        dth_dze2 = - dlambda_dze / (1. + dlambda_dth)

        zmat = np.zeros_like(s)
        omat = np.ones_like(s)

        J = np.array(((omat, zmat, zmat),
                      (dth_ds2, dth_dth2, dth_dze2),
                      (zmat, zmat, omat)))

        return self.swap_J_axes(J)

    def dP_inv(self, s2, th2, ze2):
        '''Inverse Jacobian of the Pmap.'''
        return np.linalg.inv(self.dP(s2, th2, ze2))

    def det_dP(self, s2, th2, ze2):
        '''Jacobian determinant of the Pmap.'''
        return np.linalg.det(self.dP(s2, th2, ze2))

    # combine Lmap and pest map (only map, Jacobian and inverse)
    def PLmap(self, s, u, v):
        '''The composition P ° L.
        
        Parameters
        ----------
            s, u, v : float or array-like
                Coordinates in [0, 1]^3. If list or np.array, must be either 1d (meshgrid evaluation) or 3d numpy arrays.

        Returns
        -------
            A 3-tuple of either floats (single-point evaluation) or 3d numpy arrays.
        '''
        return self.Pmap(*self.Lmap(s, u, v))
    
    def dPL(self, s, u, v):
        '''Jacobian matrix of the composition P ° L.'''

        tmp1 = self.dL(s, u, v)  # Jacobian of the Lmap
        tmp2 = self.dP(*self.Lmap(s, u, v))  # Jacobian of the Pmap

        # meshgrid evaluation
        if tmp1.ndim == 5:
            out = self.matmul_5d(tmp2, tmp1, use_pyccel=self.use_pyccel)
        # single-point evaluation
        else:
            out = tmp2 @ tmp1

        return out

    def dPL_inv(self, s, u, v):
        '''Inverse Jacobian matrix of the composition P ° L.'''
        return np.linalg.inv(self.dPL(s, u, v))

    def det_dPL(self, s, u, v):
        '''Jacobian determinant of the composition P ° L.'''
        return np.linalg.det(self.dPL(s, u, v))

    @staticmethod
    def prepare_args(s, u, v, sparse=False):
        '''Checks consistency, prepares arguments and performs meshgrid if necessary.'''

        if isinstance(s, (list, tuple)):
            s = np.array(s)

        if isinstance(u, (list, tuple)):
            u = np.array(u)

        if isinstance(v, (list, tuple)):
            v = np.array(v)

        if isinstance(s, np.ndarray):

            assert isinstance(
                u, np.ndarray), '2nd argument should be of type `np.ndarray`. Got {} instead.'.format(type(u))
            assert isinstance(
                v, np.ndarray), '3rd argument should be of type `np.ndarray`. Got {} instead.'.format(type(v))

            assert s.ndim == u.ndim, '2nd argument has different dimensions than the 1st. Expected {}, got {} instead.'.format(
                s.ndim, u.ndim)
            assert s.ndim == v.ndim, '3rd argument has different dimensions than the 1st. Expected {}, got {} instead.'.format(
                s.ndim, v.ndim)
            if s.ndim == 1:
                s, u, v = np.meshgrid(s, u, v, indexing='ij', sparse=sparse)

        return s, u, v

    @staticmethod
    def swap_J_axes(J):
        """Swap axes of a batch of Jacobians, such that it is compatible with numpy's batch processing.

        When the inputs are 1D arrays or 3D arrays of meshgrids, the Jacobian dimensions by default will be (3, 3, eta1, eta2, eta3).  
        However, all of numpy's matrix operations expect the 3x3 part to be the last two dimensions, i.e. (eta1, eta2, eta3, 3, 3).  
        This function will first check if the Jacobian has dimensions > 2 (there is no point swapping axis of a scalar input).
        Then it will check if the 3x3 portion is at the beginning of the `shape` tuple. 
        If the conditions are met, it will move the first two axes of 5D Jacobian to the last two, such that it is compatible with numpy's batch processing.

        Parameters
        ----------
            J : numpy.ndarray of shape (3, 3) or (3, 3, ...)
                A batch of Jacobians.

        Returns
        -------
            numpy.ndarray of shape (3, 3) or (..., 3, 3)
                A batch of Jacobians.
        """

        if J.ndim > 2 and J.shape[:2] == (3, 3):
            J = np.moveaxis(J, 0, -1)
            J = np.moveaxis(J, 0, -1)
        return J

    @staticmethod
    def swap_J_back(J):
        """Reverse of swap_J_axes.

        Parameters
        ----------
            J : numpy.ndarray of shape (3, 3) or (..., 3, 3)
                A batch of Jacobians.

        Returns
        -------
            numpy.ndarray of shape (3, 3) or (3, 3, ...)
                A batch of Jacobians.
        """

        if J.ndim > 2 and J.shape[-2:] == (3, 3):
            J = np.moveaxis(J, -1, 0)
            J = np.moveaxis(J, -1, 0)
        return J

    @staticmethod
    def transpose_5d(a, use_pyccel=False):
        '''Performs matrix transposition in the last two indices of the 5-dim array a.
        
        Parameters
        ----------
            a : array[float]
                5-dimensional matrix.

            use_pyccel : bool
                Whether to use an accelerated kernel for the multiplication.
                
        Returns
        -------
            A 5-dim C-contiguous array with the result.'''
        
        a_shp = a.shape

        assert isinstance(a, np.ndarray)
        assert a.ndim == 5

        out = np.ascontiguousarray(np.empty(shape=(*a_shp[:3], a_shp[4], a_shp[3])))
        if use_pyccel:
            transpose_5d_kernel(np.ascontiguousarray(a), out)
        else:
            for i in range(a_shp[0]):
                for j in range(a_shp[1]):
                    for k in range(a_shp[2]):
                        out[i, j, k] = a[i, j, k].T

        return out

    @staticmethod
    def matmul_5d(a, b, transpose_a=False, use_pyccel=False):
        '''Performs matrix multiplication a*b in the last two indices of two 5-dim arrays.
        If transpose_a=False and a is of shape (s0, s1, s2, l, m), then b must be of shape (s0, s1, s2, m, n).
        
        Parameters
        ----------
            a, b : array[float]
                5-dimensional matrices to multiply.
                
            transpose_a : bool
                Whether to transpose a.

            use_pyccel : bool
                Whether to use an accelerated kernel for the multiplication.
                
        Returns
        -------
            A 5-dim C-contiguous array with the result.'''
        
        a_shp = a.shape

        assert isinstance(a, np.ndarray)
        assert isinstance(b, np.ndarray)
        assert a.ndim == 5
        assert b.ndim == 5
        assert a.shape[:3] == b.shape[:3]

        if transpose_a:
            tmp = GVEC_domain.transpose_5d(a, use_pyccel=use_pyccel)
        else:
            tmp = np.ascontiguousarray(a)

        assert tmp.shape[4] == b.shape[3]

        out = np.ascontiguousarray(np.empty(shape=(*a_shp[:3], tmp.shape[3], b.shape[4])))

        if use_pyccel:
            matmul_5d_kernel(tmp, np.ascontiguousarray(b), out)
        else:
            for i in range(a_shp[0]):
                for j in range(a_shp[1]):
                    for k in range(a_shp[2]):
                        out[i, j, k] = tmp[i, j, k] @ b[i, j, k]

        return out

    @staticmethod
    def matvec_5d(a, b, transpose_a=False, use_pyccel=False):
        '''Performs matrix-vector multiplication a*b with the last two indices of the 5-dim array a.
        a must have shape (s0, s1, s2, n, m) and b must have "swapped axes" with shape (m, s0, s1, s2).
        Hence the last index of a contracts with the first index of b.
        
        Parameters
        ----------
            a : array[float]
                5-dimensional matrix to multiply.

            b : array[float]
                4-dimensional matrix to multiply.
                
            transpose_a : bool
                Whether to transpose a.

            use_pyccel : bool
                Whether to use an accelerated kernel for the multiplication.
                
        Returns
        -------
            A 4-dim C-contiguous array with the result.'''
        
        a_shp = a.shape

        assert isinstance(a, np.ndarray)
        assert isinstance(b, np.ndarray)
        assert a.ndim == 5
        assert b.ndim == 4
        assert a.shape[:3] == b.shape[1:]

        if transpose_a:
            tmp = GVEC_domain.transpose_5d(a, use_pyccel=use_pyccel)
        else:
            tmp = np.ascontiguousarray(a)
            
        assert tmp.shape[4] == b.shape[0]

        out = np.ascontiguousarray(np.empty(shape=(tmp.shape[3], *a_shp[:3])))

        if use_pyccel:
            matvec_5d_kernel(tmp, np.ascontiguousarray(b), out)
        else:
            for i in range(a_shp[0]):
                for j in range(a_shp[1]):
                    for k in range(a_shp[2]):
                        out[:, i, j, k] = tmp[i, j, k] @ b[:, i, j, k]

        return out
