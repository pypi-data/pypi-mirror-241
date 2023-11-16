def matmul_5d_kernel(a: 'float[:,:,:,:,:]', b: 'float[:,:,:,:,:]', out: 'float[:,:,:,:,:]'):
    '''Performs matrix multiplication in the last two indices of 5-dim arrays.
    If a is shape shape (s0, s1, s2, l, m) then b must be shape shape (s0, s1, s2, m, n).'''

    out[:] = 0.

    for i in range(out.shape[0]):
        for j in range(out.shape[1]):
            for k in range(out.shape[2]):
                for l in range(out.shape[3]):
                    for n in range(out.shape[4]):
                        for m in range(a.shape[4]):
                            out[i, j, k, l, n] += a[i, j, k, l, m] * b[i, j, k, m, n]

def matvec_5d_kernel(a: 'float[:,:,:,:,:]', b: 'float[:,:,:,:]', out: 'float[:,:,:,:]'):
    '''Performs matrix-vector multiplication in the last two indices of the 5-dim array a.
    a must have shape (s0, s1, s2, n, m) and b must have "swapped axes" with shape (m, s0, s1, s2).
    Hence the last index of a contracts with the first index of b.'''

    out[:] = 0.

    for i in range(out.shape[1]):
        for j in range(out.shape[2]):
            for k in range(out.shape[3]):
                for l in range(out.shape[0]):
                    for m in range(b.shape[0]):
                        out[l, i, j, k] += a[i, j, k, l, m] * b[m, i, j, k]

def transpose_5d_kernel(a: 'float[:,:,:,:,:]', out: 'float[:,:,:,:,:]'):
    '''Matrix transpose in the last two indices of a 5-dim array.
    If a is shape shape (., ., ., m, n) then out must be shape shape (., ., ., n, m).'''

    for i in range(out.shape[0]):
        for j in range(out.shape[1]):
            for k in range(out.shape[2]):
                for n in range(out.shape[3]):
                    for m in range(out.shape[4]):
                        out[i, j, k, n, m] = a[i, j, k, m, n]