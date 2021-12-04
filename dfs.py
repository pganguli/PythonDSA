(visited, parent, pre, post) = ({},{},{},{})

def DFSInitListGlobal(AList):
    # Initialization
    for i in AList.keys():
        visited[i] = False
        parent[i] = -1
        pre[i], post[i] = -1, -1
    return

def DFSListGlobal(AList, v, count):
    visited[v] = True

    pre[v] = count
    count += 1
    for k in AList[v]:
        if (not visited[k]):
            parent[k] = v
            DFSListGlobal(AList, k, count)
    post[v] = count
    count += 1
    return count
