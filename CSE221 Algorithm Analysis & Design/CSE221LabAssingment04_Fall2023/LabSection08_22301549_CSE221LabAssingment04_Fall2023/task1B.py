inp = open("input1B.txt", "r")
out = open("output1B.txt", "w")
n = list(map(int, inp.readline().split()))
a = [0]*n[1]
def graphIt(i, j, v):
    if type([0]) != type(a[i]):
        a[i] = []
        a[i] += [(j, v)]
    else:
        a[i] += [(j, v)]
for i in range(n[1]):
    ind = list(map(int, inp.readline().split()))
    graphIt(ind[0], ind[1], ind[2])
print(a)
for i in range(n[0]+1):
    if a[i] == 0:
        out.write("{}:".format(i))
    else:
        out.write("{}:".format(i))
        for j in a[i]:
            out.write("{}".format(j))
    print()
    out.write('\n')
inp.close()
out.close()
#The code reads a weighted directed graph from an input file and
#constructs an adjacency list named 'a.' The graphIt function appends edges and
#their weights to the list. The script then prints the resulting adjacency list to
#an output file, formatted with vertices and their associated edges. The final output
#represents the weighted directed graph using an adjacency list.