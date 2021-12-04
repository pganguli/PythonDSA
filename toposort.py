import queue

def toposortlist(AList):
    (indegree, toposortlist, lpath) = ({},[],{})
    for u in AList.keys():
        indegree[u], lpath[u] = 0, 0
    for u in AList.keys():
        for v in AList[u]:
            indegree[v] += 1

    zerodegreeq = queue.Queue()

    for u in AList.keys():
        if indegree[u] == 0:
            zerodegreeq.put(u)

    while (not zerodegreeq.empty()):
        j = zerodegreeq.get()
        toposortlist.append(j)
        indegree[j] -= 1
        for k in AList[j]:
            indegree[k] -= 1
            lpath[k] = max(lpath[k], lpath[j] + 1)
            if indegree[k] == 0:
                zerodegreeq.put(k)
    return toposortlist, lpath
