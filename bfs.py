import queue

def BFSListPathLevel(AList, v):
    (level,parent) = ({},{})
    for i in AList.keys():
        level[i] = -1
        parent[i] = -1
    q = queue.Queue()
    level[v] = 0
    q.put(v)

    while(not q.empty()):
        j = q.get()
        for k in AList[j]:
            if (level[k] == -1):
                level[k] = level[j] + 1
                parent[k] = j
                q.put(k)

    return(level, parent)
