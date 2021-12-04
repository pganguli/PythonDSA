def kmp_fail(p):

    # Initialize
    m = len(p)
    fail = [0 for i in range(m)]

    # Update
    j,k = 1,0
    while j < m:
        if p[j] == p[k]: # k+1 chars match
            fail[j] = k+1
            j,k = j+1,k+1
        elif k > 0: # find shorter prefix
            k = fail[k-1]
        else: # no match found at j
            j += 1

    return(fail)

def find_kmp(t, p):
    n,m = len(t),len(p)
    if m == 0:
        return 0 # pattern is empty
    fail = kmp_fail(p) # preprocessing
    j = 0 # index into text
    k = 0 # index into pattern
    while j < n:
        if t[j] == p[k]: # matched p[0:k+1]
            if k == m - 1: # match is complete
                return(j - m + 1)
            j,k = j+1, k+1 # extend match
        elif k > 0:
            k = fail[k-1] # use smaller prefix
        else:
            j += 1

    return(-1) # reached end without match

def isPalindrome(s):
    return kmp_fail(s + '#' + s[::-1]) == len(s)
