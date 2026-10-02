# Define the functions first
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x_root = find(x)
    y_root = find(y)

    if x_root == y_root:
        return

    if rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
        count[y_root] += count[x_root]
    elif rank[x_root] > rank[y_root]:
        parent[y_root] = x_root
        count[x_root] += count[y_root]
    else:
        parent[y_root] = x_root
        rank[x_root] += 1
        count[x_root] += count[y_root]

def size(x):
    return count[find(x)]

# Now you can use the functions
f=open('input3.txt','r')
n, k = map(int, f.readline().split())
parent = list(range(10 ** 5 + 1))
rank = [0] * (10 ** 5 + 1)
count = [1] * (10 ** 5 + 1)

parent[:n + 1] = list(range(n + 1))
rank[:n + 1] = [0] * (n + 1)
count[:n + 1] = [1] * (n + 1)
queries = [list(map(int, line.split())) for line in f]

f1=open('output3.txt','w')
for query in queries:
    if len(query) == 2: 
        x, y = query
        union(x, y)
        f1.write(str(size(x)) + '\n')

f1.close()
#The code implements a union-find data structure with path compression and union by rank. It reads input from "input3.txt," performs union operations based on the queries, and writes the size of sets after each union to "output3.txt." The data structure is initialized with arrays for parent pointers, ranks, and counts. The code efficiently maintains disjoint sets and outputs the sizes of sets as they are updated through union operations.