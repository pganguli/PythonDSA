def LCS(u,v):
    import numpy as np
    (m,n) = (len(u) ,len(v))
    lcs = np.zeros((m+1,n+1))

    for c in range(n-1,-1,-1):
        for r in range(m-1,-1,-1):
            if u[r] == v[c]:
                lcs[r,c] = 1 + lcs[r+1,c+1]
            else:
                lcs[r,c] = max(lcs[r+1,c], lcs[r,c+1])
    return(lcs[0,0])
