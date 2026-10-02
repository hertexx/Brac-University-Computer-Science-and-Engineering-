inp= open("input1a.txt", "r")
out = open("output1a.txt", "w")

N, M = map(int,inp.readline().split())
indeg = [0]*(N+1)
dic = {i:[] for i in range(N+1)}
for i in range(1, M):
    n1, n2 = map(int,inp.readline().split())
    arr = dic[n1]
    arr.append(n2)
    indeg[n2] = indeg[n2]+1
    
def DFS(G, u, time, visited, s_time, e_time,stack):
    s_time[u] = time
    time += 1
    visited[u] = True
    stack[u] = True
    cycle_detected = False
    for v in G[u]:
        if not visited[v]:
            time, e_time, cycle_detected = DFS(G, v, time, visited, s_time, e_time, stack)
            if cycle_detected:
                break
        elif stack[v]:
            cycle_detected = True
            break
    e_time[u] = time
    time += 1
    stack[u] = False
    return time, e_time, cycle_detected

def isCycle(G):
    num_vertices = len(G)
    visited = [False] * num_vertices
    s_time = [False] * num_vertices
    e_time = {i:[] for i in range(num_vertices)}
    stack = [False] * num_vertices
    time = 1
    cycle_detected = False
    for u in G:
        if not visited[u]:
            time, e_time, cycle_detected = DFS(G, u, time, visited, s_time, e_time, stack)
            if cycle_detected:
                break

    return e_time, cycle_detected

end_times, cycle = isCycle(dic)
if not cycle:
    result = [key for key, value in sorted(end_times.items(), key=lambda item: item[1], reverse=True)]
    result.remove(0)
    out.write(" ".join(list(map(str, result))))
else:
    out.write("IMPOSSIBLE")
    
inp.close()
out.close()
#This code reads a directed graph from an input file, detects cycles using depth-first search, and writes either a topological ordering of vertices (if there is no cycle) or "IMPOSSIBLE" to an output file. It employs DFS to find finishing times for each vertex and sorts them in descending order, excluding the starting vertex. The resulting order represents a valid topological ordering of the graph. If a cycle is detected during DFS, the code outputs "IMPOSSIBLE" indicating the impossibility of a topological ordering.





