import numpy as np
inp = open("input1A.txt", "r")
out = open("output1A.txt", "w")
n = list(map(int, inp.readline().split()))

mat = np.zeros((n[0]+1, n[0]+1), dtype=int)
def graphIt(i, j, v):
    mat[i][j] = v
for i in range(n[1]):
    ind = list(map(int, inp.readline().split()))
    graphIt(ind[0], ind[1], ind[2])
for i in range(len(mat)):
    stat = map(str, mat[i])
    stat = " ".join(list(map(str, stat)))
    out.write(stat)
    if i < len(mat)-1:
        out.write('\n')
inp.close()
out.close()
# The code initializes a square NumPy array (adjacency matrix) of size (N+1) x (N+1) to store edge
# weights, with zeros as the default value. It reads input data specifying the number of
# vertices (N) and edges (M), and iteratively processes M lines to extract information about
# directed edges and their weights. The graphIt function updates the adjacency matrix with the
# provided edge weights. Finally, the script writes the resulting adjacency matrix to an output file,
# representing the weighted directed graph in the specified format.