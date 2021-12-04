def dijkstralist(WList,s):
    infinity = 1 + len(WList.keys()) * max([d for u in WList.keys() for (v,d) in WList[u]])

    (visited,distance) = ({},{})
    for v in WList.keys():
        (visited[v],distance[v]) = (False, infinity)
    distance[s] = 0
    for u in WList.keys():
        nextd = min([distance[v] for v in WList.keys() if not visited[v]])
        nextvlist = [v for v in WList.keys() if (not visited[v]) and distance[v] == nextd]
        if nextvlist == []:
            break
        nextv = min(nextvlist)
        visited[nextv] = True
        for (v,d) in WList[nextv]:
            if not visited[v]:
                distance[v] = min(distance[v], distance[nextv]+d)
    return distance
