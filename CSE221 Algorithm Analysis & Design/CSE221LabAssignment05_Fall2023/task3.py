from collections import defaultdict
inp= open("input3.txt", "r")
out = open("output3.txt", "w")

N, M = map(int,inp.readline().split())

indeg = [0]*(N+1)
dic = {i:[] for i in range(N+1)}
for i in range(M-1):
    n1,n2 = map(int,inp.readline().split())
    arr = dic[n1]
    arr.append(n2)
    indeg[n2] = indeg[n2]+1
    
def DFS(G, v, visited, stack):
    visited[v] = True
    for i in G[v]:
        if not visited[i]:
            DFS(G, i, visited, stack)
    stack.append(v)

def transpose(G):
    transposed_G = {i:[] for i in range(len(G))}
    for i in G:
        for j in G[i]:
            transposed_G[j].append(i)
    return transposed_G

def SCC_DFS(G, v, visited, scc):
    visited[v] = True
    scc.append(v)
    for i in G[v]:
        if not visited[i]:
            SCC_DFS(G, i, visited, scc)

def SCC(G):
    stack = []
    visited = [False] * len(G)
    for i in range(len(G)):
        if not visited[i]:
            DFS(G, i, visited, stack)

    transposed = transpose(G)
    visited = [False] * len(G)
    scc_components = []

    while stack:
        v = stack.pop()
        if v!= 0:
            if not visited[v]:
                scc = []
                SCC_DFS(transposed, v, visited, scc)
                scc_components.append(scc)

    return scc_components

scc = SCC(dic)
for i in range(1,len(scc)):
    out.write(" ".join(list(map(str, scc[i]))))
    if i<len(scc):
        out.write("\n")
out.write(" ".join(list(map(str, scc[0]))))
inp.close()
out.close()
#This code reads a directed graph from "input3.txt," detects Strongly Connected Components (SCCs) using Depth-First Search (DFS), and writes the SCCs to "output3.txt." The graph is represented as an adjacency list in the dictionary 'dic.' The code performs a two-step process: first applying DFS on the original graph and then on the transposed graph using finishing times from the first step. The resulting SCCs are written to the output file, with each line representing a separate SCC. The first line contains the SCC containing the finishing vertex of the original DFS (vertex 0), and subsequent lines represent other SCCs. Note: The script assumes graph vertices are labeled from 1 to N.