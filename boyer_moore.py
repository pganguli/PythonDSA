def boyermoore(t,p):
    last = {} # Preprocess
    for i in range(len(p)):
        last[p[i]] = i

    poslist,i = [],0 # Loop
    while i <= (len(t)-len(p)):
        matched,j = True,len(p)-1
        while j >= 0 and matched:
            if t[i+j] != p[j]:
                matched = False
            j -= 1
        if matched:
            poslist.append(i)
            i += l
        else:
            j = j + 1
            if t[i+j] in last.keys():
                i = i + max(j-last[t[i+j]],1)
            else:
                i = i + j + 1
    return (poslist)
