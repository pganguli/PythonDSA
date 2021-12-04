def bellmanfordlist(WList,s):
    infinity = 1 + len(WList.keys()) * max([d for u in WList.keys() for (v,d) in WList[u]])

    distance = {}
    for v in WList.keys():
        distance[v] = infinity
    distance[s] = 0

    for i in WList.keys():
        for u in WList.keys():
            for (v,d) in WList[u]:
                distance[v] = min(distance[v], distance[u] + d)
    return distance
