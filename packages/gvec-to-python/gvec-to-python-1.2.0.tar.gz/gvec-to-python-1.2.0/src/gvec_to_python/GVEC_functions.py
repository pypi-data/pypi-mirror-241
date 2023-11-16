import json

import numpy as np

from gvec_to_python.base.make_base import make_base
from gvec_to_python.geometry.domain import GVEC_domain
from gvec_to_python.equilibrium.profiles import GVEC_profiles


class GVEC:
    """Primary class of `gvec_to_python` that wraps around everything as a simple interface.
    Loads GVEC data from a .json file, initializes GVEC domain and profiles.

    The class provides the MHD equilibrium calculated by GVEC as callable methods:

    p0, p3              ... equilibrium pressure (0-form, 1-form)
    bv, b1, b2, b_cart  ... equilibrium magentic field (contra-variant, co-variant=1-form, 2-form, Cartesian)
    av, a1, a2, a_cart  ... equilibrium vector potential (contra-variant, co-variant=1-form, 2-form, Cartesian) 

    These methods can be called with float, 1d or 3d array arguments (meshgrid is performed).
    Five different mappings can be chosen:

    1. f_gvec: (s, th, ze) -> (x, y, z)         ... standard gvec mapping. s=sqrt(phi_norm) in [0,1], th,ze in [0,2pi]
    2. f_pest: (s, th2, ze2) -> (x, y, z)       ... gvec straight-field-line mapping  th2,ze2 in [0,2pi]
    3. f_unit: (s, u, v) -> (x, y, z)           ... gvec with unit cube as logical domain  (th,ze)=2pi(u,v)
    4. f_unit_pest : (s, u, v) -> (x, y, z)     ... gvec straight-field-line with unit cube as logical domain
    5. f_wo_hmap : (s, th, ze) -> (X1, X2, ze)  ... standard gvec to X1,X2,zeta. For default torus (hmap=1), (R,Z,phi)=(X1,X2,-zeta)

    See GVEC.domian for details. The mapping must be set via the mapping setter method.
    The profiles can be accessed via self.profiles, see GVEC_profiles for details.

    Parameters
    ----------
        json_file : str
            The absolute path to the .json file created by GVEC_Reader.

        mapping : str
            Which mapping to use: "gvec", "pest", "unit", "unit_pest" or "wo_hmap" (see GVEC_domain class).
            Can be changed later using the setter.

        unit_tor_domain : string
            Needed for toroidal angle v in "unit" mappings. Defines the extend of the domain in toroidal direction. 
            v in [0, 1] maps to zeta=2*pi*v*tor_fraction 
            - "full"  :  v in [0, 1] maps to the full torus, tor_fraction=1.0.  [DEFAULT]
            - "one-fp":  v in [0, 1] maps to one field period, tor_fraction=1/nfp
            -  "2/3" or "0.5"  :  string of any meaningful float or ratio for tor_fraction, must be >0 and <=1

        use_pyccel : bool
            Whether to use pyccel kernels for matrix operations.
    """

    def __init__(self, json_file: str, mapping='gvec', unit_tor_domain="full", use_pyccel=False):

        # Read GVEC JSON output file.
        with open(json_file) as f:
            data = json.load(f)
        self._data = data

        self._use_pyccel = use_pyccel

        # basis coefficients
        X1_coef = np.array(data['X1']['coef'])
        X2_coef = np.array(data['X2']['coef'])
        LA_coef = np.array(data['LA']['coef'])

        # bases
        X1_base = make_base(data, 'X1')
        X2_base = make_base(data, 'X2')
        LA_base = make_base(data, 'LA')

        # number of field periods (stellarator)
        nfp = data['general']['nfp']
        self._nfp = nfp

        # Access profile point values (Greville)
        spos_grev = np.array(data['profiles']['greville']['spos'])
        phi_grev = np.array(data['profiles']['greville']['phi'])
        chi_grev = np.array(data['profiles']['greville']['chi'])
        iota_grev = np.array(data['profiles']['greville']['iota'])
        pres_grev = np.array(data['profiles']['greville']['pres'])

        assert len(
            spos_grev) == data['profiles']['greville']['nPoints'],           'Greville points should have the same length as `nPoints`.'
        assert len(
            phi_grev) == data['profiles']['greville']['nPoints'],      'Phi greville profile should have the same length as `nPoints`.'
        assert len(
            chi_grev) == data['profiles']['greville']['nPoints'],      'Chi greville profile should have the same length as `nPoints`.'
        assert len(
            iota_grev) == data['profiles']['greville']['nPoints'],     'Iota greville profile should have the same length as `nPoints`.'
        assert len(
            pres_grev) == data['profiles']['greville']['nPoints'], 'Pressure greville profile should have the same length as `nPoints`.'

        # spline space info for profile interpolation
        sgrid = data["grid"]["sGrid"]
        degree = data['X1']["s_base"]["deg"]

        # domain object
        self._domain = GVEC_domain(X1_base, X2_base, LA_base, X1_coef,
                                   X2_coef, LA_coef, nfp, unit_tor_domain=unit_tor_domain, use_pyccel=use_pyccel)

        # profile object
        self._profiles = GVEC_profiles(
            sgrid, degree, spos_grev, phi_grev, chi_grev, iota_grev, pres_grev)

        # use the mapping setter
        assert mapping in {'gvec', 'pest', 'unit', 'unit_pest', 'wo_hmap'}
        self.mapping = mapping

        # Expose other metadata
        self._minor_radius = data['general']['a_minor']
        self._major_radius = data['general']['r_major']

    @property
    def data(self):
        '''Json data from GVEC run via create_GVEC_json.'''
        return self._data

    @property
    def use_pyccel(self):
        '''Whether to use pyccel kernels for matrix operations.'''
        return self._use_pyccel

    @property
    def domain(self):
        '''Object for all things related to GVEC mappings.'''
        return self._domain

    @property
    def profiles(self):
        '''Object for GVEC radial profiles.'''
        return self._profiles

    @property
    def mapping(self):
        '''Which mapping to use: "gvec", "pest", "unit", "unit_pest" or "wo_hmap" (see GVEC_domain class).'''
        return self._mapping

    @mapping.setter
    def mapping(self, mapping):
        '''Can be used to change the mapping.'''

        # mapping to Cartesian coordinates
        self._f = getattr(self.domain, 'f_' + mapping)
        self._df = getattr(self.domain, 'df_' + mapping)
        self._det_df = getattr(self.domain, 'det_df_' + mapping)
        self._df_inv = getattr(self.domain, 'df_' + mapping + '_inv')
        self._g = getattr(self.domain, 'g_' + mapping)
        self._g_inv = getattr(self.domain, 'g_' + mapping + '_inv')

        # for transformations of a1_gvec and bv_gvec to other logical coordinates than "gvec"
        if mapping in {'gvec', 'wo_hmap'}:
            self.l = None
            self.dl = None
            self.dl_inv = None
            self.det_dl = None
        elif mapping == 'pest':
            self.l = self.domain.Pmap
            self.dl = self.domain.dP
            self.dl_inv = self.domain.dP_inv
            self.det_dl = self.domain.det_dP
        elif mapping == 'unit':
            self.l = self.domain.Lmap
            self.dl = self.domain.dL
            self.dl_inv = self.domain.dL_inv
            self.det_dl = self.domain.det_dL
        elif mapping == 'unit_pest':
            self.l = self.domain.PLmap
            self.dl = self.domain.dPL
            self.dl_inv = self.domain.dPL_inv
            self.det_dl = self.domain.det_dPL

        self._mapping = mapping

    @property
    def nfp(self):
        '''Number of Field periods used in the GVEC run.'''
        return self._nfp
    @property
    def f(self):
        '''The callable map from logical to Cartesian coordiantes, set via the mapping setter.'''
        return self._f

    @property
    def df(self):
        '''The callable Jacobian of the map from logical to Cartesian coordiantes, set via the mapping setter.'''
        return self._df

    @property
    def det_df(self):
        '''The callable Jacobian determinant of the map from logical to Cartesian coordiantes, set via the mapping setter.'''
        return self._det_df

    @property
    def df_inv(self):
        '''The callable inverse Jacobian of the map from logical to Cartesian coordiantes, set via the mapping setter.'''
        return self._df_inv

    @property
    def g(self):
        '''The callable metric tensor of the map from logical to Cartesian coordiantes, set via the mapping setter.'''
        return self._g
    
    @property
    def g_inv(self):
        '''The callable inverse metric tensor of the map from logical to Cartesian coordiantes, set via the mapping setter.'''
        return self._g_inv

    # direct access to MHD equilibrium
    def p0(self, s, a1, a2):
        '''Pressure as 0-form in one of the coordinates "gvec", "pest", "unit" or unit_pest.
        Coordinates can be chosen using the mapping setter.

        Parameters
        ----------
            s, a1, a2 : float or array-like
                Coordinates in logical space. If list or np.array, must be either 1d or 3d (from meshgrid).
                s in [0, 1] and a1, a2 are angle-like, either in [0, 2*pi]^2 or in [0, 1]^2. 

        Returns
        -------
            A float (single-point evaluation) or 3d numpy array (meshgrid evaluation).
        '''
        return self.profiles.profile(s, a1, a2, name='pressure')

    def p3(self, s, a1, a2):
        '''Pressure as 3-form in one of the coordinates "gvec", "pest", "unit" or unit_pest.
        Coordinates can be chosen using the mapping setter.

        Parameters
        ----------
            s, a1, a2 : float or array-like
                Coordinates in logical space. If list or np.array, must be either 1d or 3d (from meshgrid).
                s in [0, 1] and a1, a2 are angle-like, either in [0, 2*pi]^2 or in [0, 1]^2. 

        Returns
        -------
            A float (single-point evaluation) or 3d numpy array (meshgrid evaluation).
        '''
        return self.det_df(s, a1, a2) * self.p0(s, a1, a2)

    def p_cart(self, s, a1, a2):
        '''Pressure in Cartesian coordinates, evaluated at one of the coordinates "gvec", "pest", "unit" or unit_pest.
        Coordinates can be chosen using the mapping setter.

        Parameters
        ----------
            s, a1, a2 : float or array-like
                Coordinates in logical space. If list or np.array, must be either 1d or 3d (from meshgrid).
                s in [0, 1] and a1, a2 are angle-like, either in [0, 2*pi]^2 or in [0, 1]^2. 

        Returns
        -------
            A 2-tuple: first entry is either a float (single-point evaluation) or 3d numpy array (meshgrid evaluation).
                Second entry are the Cartesian coordinates of evaluation points.
        '''
        return self.p0(s, a1, a2), self.f(s, a1, a2)

    def bv(self, s, a1, a2):
        '''Contra-variant components (vector-field) of the magnetic field in one of the coordinates "gvec", "pest", "unit" or unit_pest.
        Coordinates can be chosen using the mapping setter.

        Parameters
        ----------
            s, a1, a2 : float or array-like
                Coordinates in logical space. If list or np.array, must be either 1d or 3d (from meshgrid).
                s in [0, 1] and a1, a2 are angle-like, either in [0, 2*pi]^2 or in [0, 1]^2. 

        Returns
        -------
            A 3-tuple of either floats (single-point evaluation) or 3d numpy arrays (meshgrid evaluation).
        '''
        if self.l is None:
            return self._bv_gvec(s, a1, a2)
        else:
            return self.transform(self._bv_gvec(*self.l(s, a1, a2)), s, a1, a2, kind='pull_vector', full_map=False)

    def b1(self, s, a1, a2):
        '''Co-variant components (1-form) of the magnetic field in one of the coordinates "gvec", "pest", "unit" or unit_pest.
        Coordinates can be chosen using the mapping setter.

        Parameters
        ----------
            s, a1, a2 : float or array-like
                Coordinates in logical space. If list or np.array, must be either 1d or 3d (from meshgrid).
                s in [0, 1] and a1, a2 are angle-like, either in [0, 2*pi]^2 or in [0, 1]^2. 

        Returns
        -------
            A 3-tuple of either floats (single-point evaluation) or 3d numpy arrays (meshgrid evaluation).
        '''
        return self.transform(self.bv(s, a1, a2), s, a1, a2, kind='v_to_1')

    def b2(self, s, a1, a2):
        '''2-form components of the magnetic field as in one of the coordinates "gvec", "pest", "unit" or unit_pest.
        Coordinates can be chosen using the mapping setter.

        Parameters
        ----------
            s, a1, a2 : float or array-like
                Coordinates in logical space. If list or np.array, must be either 1d or 3d (from meshgrid).
                s in [0, 1] and a1, a2 are angle-like, either in [0, 2*pi]^2 or in [0, 1]^2. 

        Returns
        -------
            A 3-tuple of either floats (single-point evaluation) or 3d numpy arrays (meshgrid evaluation).
        '''
        return self.transform(self.bv(s, a1, a2), s, a1, a2, kind='v_to_2')

    def b_cart(self, s, a1, a2):
        '''Cartesian components of the magnetic field evaluated at one of the coordinates "gvec", "pest", "unit" or unit_pest.
        Coordinates can be chosen using the mapping setter.

        Parameters
        ----------
            s, a1, a2 : float or array-like
                Coordinates in logical space. If list or np.array, must be either 1d or 3d (from meshgrid).
                s in [0, 1] and a1, a2 are angle-like, either in [0, 2*pi]^2 or in [0, 1]^2. 

        Returns
        -------
            A 2-tuple: first entry is a 3-tuple of either floats (single-point evaluation) or 3d numpy arrays (meshgrid evaluation).
                Second entry are the Cartesian coordinates of evaluation points.
        '''
        return self.transform(self.bv(s, a1, a2), s, a1, a2, kind='push_vector'), self.f(s, a1, a2)

    def av(self, s, a1, a2):
        '''Contra-variant components (vector-field) of the vector potential in one of the coordinates "gvec", "pest", "unit" or unit_pest.
        Coordinates can be chosen using the mapping setter.

        Parameters
        ----------
            s, a1, a2 : float or array-like
                Coordinates in logical space. If list or np.array, must be either 1d or 3d (from meshgrid).
                s in [0, 1] and a1, a2 are angle-like, either in [0, 2*pi]^2 or in [0, 1]^2. 

        Returns
        -------
            A 3-tuple of either floats (single-point evaluation) or 3d numpy arrays (meshgrid evaluation).
        '''
        return self.transform(self.a1(s, a1, a2), s, a1, a2, kind='1_to_v')

    def a1(self, s, a1, a2):
        '''Co-variant components (1-form) of the vector potential in one of the coordinates "gvec", "pest", "unit" or unit_pest.
        Coordinates can be chosen using the mapping setter.

        Parameters
        ----------
            s, a1, a2 : float or array-like
                Coordinates in logical space. If list or np.array, must be either 1d or 3d (from meshgrid).
                s in [0, 1] and a1, a2 are angle-like, either in [0, 2*pi]^2 or in [0, 1]^2. 

        Returns
        -------
            A 3-tuple of either floats (single-point evaluation) or 3d numpy arrays (meshgrid evaluation).
        '''
        if self.l is None:
            return self._a1_gvec(s, a1, a2)
        else:
            return self.transform(self._a1_gvec(*self.l(s, a1, a2)), s, a1, a2, kind='pull_1form', full_map=False)

    def a2(self, s, a1, a2):
        '''2-form components of the vector potential as in one of the coordinates "gvec", "pest", "unit" or unit_pest.
        Coordinates can be chosen using the mapping setter.

        Parameters
        ----------
            s, a1, a2 : float or array-like
                Coordinates in logical space. If list or np.array, must be either 1d or 3d (from meshgrid).
                s in [0, 1] and a1, a2 are angle-like, either in [0, 2*pi]^2 or in [0, 1]^2. 

        Returns
        -------
            A 3-tuple of either floats (single-point evaluation) or 3d numpy arrays (meshgrid evaluation).
        '''
        return self.transform(self.a1(s, a1, a2), s, a1, a2, kind='1_to_2')

    def a_cart(self, s, a1, a2):
        '''Cartesian components of vector potential evaluated at one of the coordinates "gvec", "pest", "unit" or unit_pest.
        Coordinates can be chosen using the mapping setter.

        Parameters
        ----------
            s, a1, a2 : float or array-like
                Coordinates in logical space. If list or np.array, must be either 1d or 3d (from meshgrid).
                s in [0, 1] and a1, a2 are angle-like, either in [0, 2*pi]^2 or in [0, 1]^2. 

        Returns
        -------
            A 2-tuple: first entry is a 3-tuple of either floats (single-point evaluation) or 3d numpy arrays (meshgrid evaluation).
                Second entry are the Cartesian coordinates of evaluation points.
        '''
        return self.transform(self.a1(s, a1, a2), s, a1, a2, kind='push_1form'), self.f(s, a1, a2)

    def jv(self, s, a1, a2):
        '''Contra-variant components (vector-field) of the equilibirum current curl B / mu0 in one of the coordinates "gvec", "pest", "unit" or unit_pest.
        Coordinates can be chosen using the mapping setter.

        Parameters
        ----------
            s, a1, a2 : float or array-like
                Coordinates in logical space. If list or np.array, must be either 1d or 3d (from meshgrid).
                s in [0, 1] and a1, a2 are angle-like, either in [0, 2*pi]^2 or in [0, 1]^2. 

        Returns
        -------
            A 3-tuple of either floats (single-point evaluation) or 3d numpy arrays (meshgrid evaluation).
        '''
        return self.transform(self.j2(s, a1, a2), s, a1, a2, kind='2_to_v')

    def j1(self, s, a1, a2):
        '''Co-variant components (1-form) of the equilibirum current curl B / mu0 in one of the coordinates "gvec", "pest", "unit" or unit_pest.
        Coordinates can be chosen using the mapping setter.

        Parameters
        ----------
            s, a1, a2 : float or array-like
                Coordinates in logical space. If list or np.array, must be either 1d or 3d (from meshgrid).
                s in [0, 1] and a1, a2 are angle-like, either in [0, 2*pi]^2 or in [0, 1]^2. 

        Returns
        -------
            A 3-tuple of either floats (single-point evaluation) or 3d numpy arrays (meshgrid evaluation).
        '''
        return self.transform(self.j2(s, a1, a2), s, a1, a2, kind='2_to_1')

    def j2(self, s, a1, a2):
        '''2-form components of the equilibirum current curl B / mu0 as in one of the coordinates "gvec", "pest", "unit" or unit_pest.
        Coordinates can be chosen using the mapping setter.

        Parameters
        ----------
            s, a1, a2 : float or array-like
                Coordinates in logical space. If list or np.array, must be either 1d or 3d (from meshgrid).
                s in [0, 1] and a1, a2 are angle-like, either in [0, 2*pi]^2 or in [0, 1]^2. 

        Returns
        -------
            A 3-tuple of either floats (single-point evaluation) or 3d numpy arrays (meshgrid evaluation).
        '''
        if self.l is None:
            return self._j2_gvec(s, a1, a2)
        else:
            return self.transform(self._j2_gvec(*self.l(s, a1, a2)), s, a1, a2, kind='pull_2form', full_map=False)

    def j_cart(self, s, a1, a2):
        '''Cartesian components of equilibirum current curl B / mu0 evaluated at one of the coordinates "gvec", "pest", "unit" or unit_pest.
        Coordinates can be chosen using the mapping setter.

        Parameters
        ----------
            s, a1, a2 : float or array-like
                Coordinates in logical space. If list or np.array, must be either 1d or 3d (from meshgrid).
                s in [0, 1] and a1, a2 are angle-like, either in [0, 2*pi]^2 or in [0, 1]^2. 

        Returns
        -------
            A 2-tuple: first entry is a 3-tuple of either floats (single-point evaluation) or 3d numpy arrays (meshgrid evaluation).
                Second entry are the Cartesian coordinates of evaluation points.
        '''
        j = self.jv(s, a1, a2)
        return self.transform(self.jv(s, a1, a2), s, a1, a2, kind='push_vector'), self.f(s, a1, a2)

    # test equilibirum condition grad p = J x B / mu0
    def assert_equil(self, s, a1, a2):
        '''Test the equilibirum condition grad p = J x B / mu0.'''

        p = self.profiles.profile(s, a1, a2, name='pressure', der=None) 
        p_s = self.profiles.profile(s, a1, a2, name='pressure', der='s') 
        j = self.j2(s, a1, a2)
        b = self.bv(s, a1, a2)
        abs_j = np.sqrt(j[0]**2 + j[1]**2 + j[2]**2)
        abs_b = np.sqrt(b[0]**2 + b[1]**2 + b[2]**2)

        print(p_s.shape, j[0].shape, b[0].shape)
        print('p:', np.max(np.abs(p)))
        print('p_s:', np.max(np.abs(p_s)))
        print('j1:', np.max(np.abs(j[0])))
        print('j2:', np.max(np.abs(j[1])))
        print('j3:', np.max(np.abs(j[2])))
        print('b1:', np.max(np.abs(b[0])))
        print('b2:', np.max(np.abs(b[1])))
        print('b3:', np.max(np.abs(b[2])))
        print('p_s = (j2 x bv)_1, rel error:', np.max(np.abs(p_s - (j[1] * b[2] - j[2] * b[1])) / (abs_j * abs_b)))
        print('0   = (j2 x bv)_2, rel error:', np.max(np.abs(j[2] * b[0] - j[0] * b[2]) / (abs_j * abs_b)))
        print('0   = (j2 x bv)_3, rel error:', np.max(np.abs(j[0] * b[1] - j[1] * b[0]) / (abs_j * abs_b)))
        #assert np.allclose(p_s, j[1] * b[2] - j[2] * b[1])
        #assert np.allclose(0*b[0], j[2] * b[0] - j[0] * b[2])
        #assert np.allclose(0*b[0], j[0] * b[1] - j[1] * b[0])

    #---------------------------------
    # Internal methods (gvec fields)
    #---------------------------------

    def _a1_gvec(self, s, th, ze):
        '''Vector potential as 1-form (co-variant components) in gvec standard coordinates (map f).

        Parameters
        ----------
            s, th, ze : float or array-like
                Coordinates in [0, 1] x [0, 2*pi]^2. If list or np.array, must be either 1d or 3d (from meshgrid).

        Returns
        -------
            A 3-tuple of either floats (single-point evaluation) or 3d numpy arrays (meshgrid evaluation).'''

        phi = self.profiles.profile(s, th, ze, name='phi')
        dphi = self.profiles.profile(s, th, ze, name='phi', der='s')
        chi = self.profiles.profile(s, th, ze, name='chi')

        return (- self._lambda(s, th, ze) * dphi, phi, -chi)

    def _bv_gvec(self, s, th, ze):
        '''Magnetic field as vector-field (contra-variant components) in gvec standard coordinates (map f).

        Parameters
        ----------
            s, th, ze : float or array-like
                Coordinates in [0, 1] x [0, 2*pi]^2. If list or np.array, must be either 1d or 3d (from meshgrid).

        Returns
        -------
            A 3-tuple of either floats (single-point evaluation) or 3d numpy arrays (meshgrid evaluation).'''

        det_df = self.domain.det_df_gvec(s, th, ze)

        return (0.*det_df, self._b_small_th(s, th, ze) / det_df, self._b_small_ze(s, th, ze) / det_df)

    def _j2_gvec(self, s, th, ze):
        '''Equilibirum current curl B / mu0, as 2-form in gvec standard coordinates (map f).

        Parameters
        ----------
            s, th, ze : float or array-like
                Coordinates in [0, 1] x [0, 2*pi]^2. If list or np.array, must be either 1d or 3d (from meshgrid).

        Returns
        -------
            A 3-tuple of either floats (single-point evaluation) or 3d numpy arrays (meshgrid evaluation).'''

        mu0 = 1.2566370621219e-6
        b = np.ascontiguousarray(self._bv_gvec(s, th, ze))

        grad_bt = self._grad_b_theta(s, th, ze)
        grad_bz = self._grad_b_zeta(s, th, ze)
        db_ds = np.ascontiguousarray((0.*grad_bt[0], grad_bt[0], grad_bz[0]))
        db_dt = np.ascontiguousarray((0.*grad_bt[1], grad_bt[1], grad_bz[1]))
        db_dz = np.ascontiguousarray((0.*grad_bt[2], grad_bt[2], grad_bz[2]))

        g = self.domain.g_gvec(s, th, ze)
        dg_ds = self.domain.dg_gvec(s, th, ze, der='s')
        dg_dt = self.domain.dg_gvec(s, th, ze, der='th')
        dg_dz = self.domain.dg_gvec(s, th, ze, der='ze')

        # meshgrid evaluation
        if g.ndim == 5:
            dgb_ds = GVEC_domain.matvec_5d(dg_ds, b, use_pyccel=self.use_pyccel) + GVEC_domain.matvec_5d(g, db_ds, use_pyccel=self.use_pyccel)
            dgb_dt = GVEC_domain.matvec_5d(dg_dt, b, use_pyccel=self.use_pyccel) + GVEC_domain.matvec_5d(g, db_dt, use_pyccel=self.use_pyccel)
            dgb_dz = GVEC_domain.matvec_5d(dg_dz, b, use_pyccel=self.use_pyccel) + GVEC_domain.matvec_5d(g, db_dz, use_pyccel=self.use_pyccel)
        # single point evaluation
        else:
            dgb_ds = dg_ds @ b + g @ db_ds
            dgb_dt = dg_dt @ b + g @ db_dt
            dgb_dz = dg_dz @ b + g @ db_dz

        j1 = (dgb_dt[2] - dgb_dz[1]) / mu0
        j2 = (dgb_dz[0] - dgb_ds[2]) / mu0
        j3 = (dgb_ds[1] - dgb_dt[0]) / mu0

        return j1, j2, j3

    def _grad_b_theta(self, s, th, ze):
        '''Gradient w.r.t (s, theta, zeta) of the second component of _bv_gvec, returned as 3-tuple.
        '''
        det_df = self.domain.det_df_gvec(s, th, ze)
        dphi = self.profiles.profile(s, th, ze, name='phi', der='s')
        dchi = self.profiles.profile(s, th, ze, name='chi', der='s')
        ddphi = self.profiles.profile(s, th, ze, name='phi', der='ss')
        ddchi = self.profiles.profile(s, th, ze, name='chi', der='ss')

        term1 = ddchi - ddphi * self._lambda_ze(s, th, ze) - dphi * self._lambda_sze(s, th, ze)
        term2 = - self._b_small_th(s, th, ze) * self.domain.dJ_gvec(s, th, ze, der='s') / det_df
        db_ds = (term1 + term2) / det_df

        term1 = - dphi * self._lambda_thze(s, th, ze) 
        term2 = - self._b_small_th(s, th, ze) * self.domain.dJ_gvec(s, th, ze, der='th') / det_df
        db_dt = (term1 + term2) / det_df

        term1 = - dphi * self._lambda_zeze(s, th, ze) 
        term2 = - self._b_small_th(s, th, ze) * self.domain.dJ_gvec(s, th, ze, der='ze') / det_df
        db_dz = (term1 + term2) / det_df

        return db_ds, db_dt, db_dz 

    def _grad_b_zeta(self, s, th, ze):
        '''Gradient w.r.t (s, theta, zeta) of the third component of _bv_gvec, returned as 3-tuple.
        '''

        det_df = self.domain.det_df_gvec(s, th, ze)
        dphi = self.profiles.profile(s, th, ze, name='phi', der='s')
        ddphi = self.profiles.profile(s, th, ze, name='phi', der='ss')

        term1 = ddphi * (1. + self._lambda_th(s, th, ze)) + dphi * self._lambda_sth(s, th, ze)
        term2 = - self._b_small_ze(s, th, ze) * self.domain.dJ_gvec(s, th, ze, der='s') / det_df
        db_ds = (term1 + term2) / det_df

        term1 = dphi * self._lambda_thth(s, th, ze) 
        term2 = - self._b_small_ze(s, th, ze) * self.domain.dJ_gvec(s, th, ze, der='th') / det_df
        db_dt = (term1 + term2) / det_df

        term1 = dphi * self._lambda_thze(s, th, ze) 
        term2 = - self._b_small_ze(s, th, ze) * self.domain.dJ_gvec(s, th, ze, der='ze') / det_df
        db_dz = (term1 + term2) / det_df

        return db_ds, db_dt, db_dz 

    def _b_small_th(self, s, th, ze):
        '''B^theta * J'''

        dphi = self.profiles.profile(s, th, ze, name='phi', der='s')
        dchi = self.profiles.profile(s, th, ze, name='chi', der='s')

        return dchi - dphi * self._lambda_ze(s, th, ze)

    def _b_small_ze(self, s, th, ze):
        '''B^zeta * J'''

        dphi = self.profiles.profile(s, th, ze, name='phi', der='s')

        return dphi * (1. + self._lambda_th(s, th, ze))

    # lambda function
    def _lambda(self, s, th, ze):
        '''The lambda function from gvec.'''
        return self.domain.LA_base.eval_stz(s, th, ze, self.domain.LA_coef)

    def _lambda_s(self, s, th, ze):
        '''s-derivative of the lambda function from gvec.'''
        return self.domain.LA_base.eval_stz(s, th, ze, self.domain.LA_coef, der='s')

    def _lambda_th(self, s, th, ze):
        '''theta-derivative of the lambda function from gvec.'''
        return self.domain.LA_base.eval_stz(s, th, ze, self.domain.LA_coef, der='th')

    def _lambda_ze(self, s, th, ze):
        '''zeta-derivative of the lambda function from gvec.'''
        return self.domain.LA_base.eval_stz(s, th, ze, self.domain.LA_coef, der='ze')

    def _lambda_ss(self, s, th, ze):
        '''Second derivative of the lambda function from gvec.'''
        return self.domain.LA_base.eval_stz(s, th, ze, self.domain.LA_coef, der='ss')

    def _lambda_thth(self, s, th, ze):
        '''Second derivative of the lambda function from gvec.'''
        return self.domain.LA_base.eval_stz(s, th, ze, self.domain.LA_coef, der='thth')

    def _lambda_zeze(self, s, th, ze):
        '''Second derivative of the lambda function from gvec.'''
        return self.domain.LA_base.eval_stz(s, th, ze, self.domain.LA_coef, der='zeze')

    def _lambda_sth(self, s, th, ze):
        '''Second derivative of the lambda function from gvec.'''
        return self.domain.LA_base.eval_stz(s, th, ze, self.domain.LA_coef, der='sth')

    def _lambda_sze(self, s, th, ze):
        '''Second derivative of the lambda function from gvec.'''
        return self.domain.LA_base.eval_stz(s, th, ze, self.domain.LA_coef, der='sze')

    def _lambda_thze(self, s, th, ze):
        '''Second derivative of the lambda function from gvec.'''
        return self.domain.LA_base.eval_stz(s, th, ze, self.domain.LA_coef, der='thze')
    
    #---------------
    # Helper methods
    #---------------

    def transform(self, b, s, a1, a2, kind, full_map=True):
        '''Transformations of vector-valued functions under a map m:
        
        pull_vector:    out = dm_inv * b    (dm is the Jacobian of m)
        pull_1form:     out = dm.T * b
        pull_2form:     out = det_dm * dm_inv * b
        push_vector:    out = dm * b
        push_1form:     out = dm_inv.T * b
        v_to_1:         out = g * b         (g is the metric tensor of m)
        1_to_v:         out = g_inv * b
        v_to_2:         out = det_dm * b
        2_to_v:         out = b / det_dm
        1_to_2:         out = det_dm * g_inv * b
        2_to_1:         out = g * b / det_dm
        
        Parameters
        ----------
            b : tuple[float/array]
                3-tuple of input vector-valued function evaluated as float or array.
                
            s, a1, a2 : float or array-like
                Coordinates in logical space. If list or np.array, must be either 1d or 3d (from meshgrid).
                s in [0, 1] and a1, a2 are angle-like, either in [0, 2*pi]^2 or in [0, 1]^2.
                
            kind : str
                Which transformation to use: "pull_vector", "pull_1form", "pull_2form", "push_vector", "push_1form", or "push_2form".
                
            full_map : bool
                True: use the full map "f" to Cartesian coordinates or False: use a map "l" between logical coordinates.
                Both are set in the mapping setter.
                
        Returns
        -------
            A 3-tuple of either floats (single-point evaluation) or 3d numpy arrays (meshgrid evaluation).'''

        assert isinstance(b, tuple)
        assert len(b) == 3

        # pull to other logical
        if kind == 'pull_vector':
            if full_map:
                raise NotImplementedError
            else:
                if self.mapping == 'gvec':
                    return b
                else:
                    mat = self.dl_inv(s, a1, a2)
                    transpose = False

        elif kind == 'pull_1form':
            if full_map:
                raise NotImplementedError
            else:
                if self.mapping == 'gvec':
                    return b
                else:
                    mat = self.dl(s, a1, a2)
                    transpose = True

        elif kind == 'pull_2form':
            if full_map:
                raise NotImplementedError
            else:
                if self.mapping == 'gvec':
                    return b
                else:
                    mat = GVEC_domain.swap_J_axes(GVEC_domain.swap_J_back(self.dl_inv(s, a1, a2)) * self.det_dl(s, a1, a2))
                    transpose = False

        # push to physical
        elif kind == 'push_vector':
            if full_map:
                mat = self.df(s, a1, a2)
                transpose = False
            else:
                raise NotImplementedError

        elif kind == 'push_1form':
            if full_map:
                mat = self.df_inv(s, a1, a2)
                transpose = True
            else:
                raise NotImplementedError

        # transform to other logical
        elif kind == 'v_to_1':
            if full_map:
                mat = self.g(s, a1, a2)
                transpose = False
            else:
                raise NotImplementedError

        elif kind == '1_to_v':
            if full_map:
                mat = self.g_inv(s, a1, a2)
                transpose = False
            else:
                raise NotImplementedError

        elif kind == 'v_to_2':
            if full_map:
                out = self.det_df(s, a1, a2) * np.ascontiguousarray(b)
                return out[0], out[1], out[2]
            else:
                raise NotImplementedError

        elif kind == '2_to_v':
            if full_map:
                out = np.ascontiguousarray(b) / self.det_df(s, a1, a2)
                return out[0], out[1], out[2]
            else:
                raise NotImplementedError

        elif kind == '1_to_2':
            if full_map:
                mat = GVEC_domain.swap_J_axes(GVEC_domain.swap_J_back(self.g_inv(s, a1, a2)) * self.det_df(s, a1, a2))
                transpose = False
            else:
                raise NotImplementedError   

        elif kind == '2_to_1':
            if full_map:
                mat = GVEC_domain.swap_J_axes(GVEC_domain.swap_J_back(self.g(s, a1, a2)) / self.det_df(s, a1, a2))
                transpose = False
            else:
                raise NotImplementedError 

        else:
            raise NotImplementedError      

        # meshgrid evaluation
        if mat.ndim == 5:
            out = GVEC_domain.matvec_5d(mat, np.ascontiguousarray(b), transpose_a=transpose, use_pyccel=self.use_pyccel)
        # single-point evaluation
        else:
            if transpose:
                out = mat.T @ b
            else:
                out = mat @ b

        return out[0], out[1], out[2]
