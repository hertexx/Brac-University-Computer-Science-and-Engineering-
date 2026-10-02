class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n
        self.num_sets = n

    def find(self, a: int) -> int:
        to_update = []
        while a != self.parent[a]:
            to_update.append(a)
            a = self.parent[a]
        for b in to_update:
            self.parent[b] = a
        return a

    def merge(self, a: int, b: int) -> bool:
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return False
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.num_sets -= 1
        self.parent[b] = a
        self.size[a] += self.size[b]
        return True

    def set_size(self, a: int) -> int:
        return self.size[self.find(a)]

with open('input4.txt', 'r') as f:
    n, m = map(int, f.readline().strip().split())
    edges = [tuple(map(int, line.strip().split())) for line in f]

edges.sort(key=lambda x: x[2] if len(x) > 2 else float('inf'))
uf = UnionFind(n)
total_cost = 0
for u, v, w in edges:
    if uf.merge(u - 1, v - 1):
        total_cost += w
        if uf.num_sets == 1:
            break
with open('output4.txt', 'w') as f:
    f.write(str(total_cost))
#The code implements Kruskal's algorithm for finding the minimum spanning tree of a graph. It utilizes a `UnionFind` class for efficient disjoint set operations. Input is read from "input4.txt," where edges are sorted by weight and added to the spanning tree if they connect previously unconnected components. The total cost of the minimum spanning tree is written to "output4.txt." The algorithm terminates when all nodes are part of a single connected component.