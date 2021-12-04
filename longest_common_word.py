def LCW(u,v):
    import numpy as np
    (m,n) = (len(u), len(v))
    lcw = np.zeros((m+1,n+1))

    maxlcw = 0

    for c in range(n-1,-1,-1):
        for r in range(m-1,-1,-1):
            if u[r] == v[c]:
                lcw[r,c] = 1 + lcw[r+1,c+1]
            else:
                lcw[r,c] = 0

            if lcw[r,c] > maxlcw:
                maxlcw = lcw[r,c]

    return (maxlcw)
