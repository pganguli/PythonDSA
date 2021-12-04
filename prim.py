def primlist2(WList):
    infinity = 1 + max([d for u in WList.keys() for (v,d) in WList[u]])

    (visited,distance,nbr) = ({},{},{})
    for v in WList.keys():
        (visited[v] ,distance[v] ,nbr[v]) = (False,infinity,-1)
    visited[0] = True
    for (v,d) in WList[0]:
        (distance[v],nbr[v]) = (d,0)
    for i in range(1,len(WList.keys())):
        nextd = min([distance[v] for v in WList.keys() if not visited[v]])
        nextvlist = [v for v in WList.keys() if (not visited[v]) and distance[v] == nextd]
        if nextvlist == []:
            break
        nextv = min(nextvlist)
        visited[nextv] = True
        for (v,d) in WList[nextv]:
            if not visited[v]:
                (distance[v],nbr[v]) = (min(distance[v], d), nextv)
    return (nbr)
