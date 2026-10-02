inp= open("input1b.txt", "r")
out = open("output1b.txt", "w")

N, M = map(int,inp.readline().split())
indeg = [0]*(N+1)
dic = {i:[] for i in range(1, N+1)}
for i in range(1, M):
    n1,n2 = map(int,inp.readline().split())
    arr = dic[n1]
    arr.append(n2)
    indeg[n2] = indeg[n2]+1
def TopoSortBFS(G, indeg):
    cnt = 0
    q1 = []
    q2 = []
    for i in G:
        if indeg[i] == 0:
            q1.append(i)
    while q1:
        el = q1.pop()
        cnt+=1
        q2.append(el)
        for j in G[el]:
            indeg[j] = indeg[j]-1
            if indeg[j] == 0:
                q1.append(j)
    if cnt!= len(G):
        return ["IMPOSSIBLE"]
    else:
        return q2
    
result = TopoSortBFS(dic,indeg)
out.write(" ".join(list(map(str, result))))
inp.close()
out.close()
#This code reads a directed graph from "input1b.txt," where each line represents an edge, and performs a topological sort using Breadth-First Search (BFS). The graph is represented as an adjacency list in the dictionary 'dic.' The code initializes an indegree array and a queue to perform BFS, updating indegrees as vertices are processed. If a valid topological ordering is possible, the result is written to "output1b.txt"; otherwise, "IMPOSSIBLE" is written. The script uses queue-based BFS to ensure topological order while handling dependencies.





