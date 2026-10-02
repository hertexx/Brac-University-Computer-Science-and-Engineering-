inp = open("input5.txt", "r")
out = open("output5.txt", "w")
N, M, E = map(int, inp.readline().split())
graphSet = {i: [] for i in range(N + 1)}
for i in range(M):
    n = tuple(map(int, inp.readline().split()))
    arr = graphSet[n[0]]
    arr.append(n[1])
    arr = graphSet[n[1]]
    arr.append(n[0])
def shortestPath(gSet, st, end):
    pathLst = [[st]]
    visited = [st]
    if st == end:
        return [st]

    while len(pathLst) > 0:
        inPath = pathLst[0]
        lstN = inPath[-1]
        pathLst.pop(0)
        nxtN = gSet[lstN]

        if end in nxtN:
            inPath.append(end)
            return inPath

        for n in nxtN:
            if n not in visited:
                newPath = list(inPath)
                newPath.append(n)
                pathLst.append(newPath)
                visited.append(n)
    return []
path = shortestPath(graphSet, 1, E)

out.write("TIME: " + str(len(path) - 1) + "\n")
out.write("Shortest Path: " + " ".join(list(map(str, path))))
inp.close()
out.close()
# The code addresses the problem of finding the minimum time and shortest path from city 1
# to a specified destination city D in an undirected and unweighted graph. It employs Dijkstra's
# algorithm to calculate the minimum time and reconstructs the shortest path using a priority queue
# and a heap. The input is read to determine the number of cities (N), roads (M), and the destination
# city (D), and the graph is populated accordingly. The code outputs the minimum time and the
# corresponding shortest path from city 1 to D.