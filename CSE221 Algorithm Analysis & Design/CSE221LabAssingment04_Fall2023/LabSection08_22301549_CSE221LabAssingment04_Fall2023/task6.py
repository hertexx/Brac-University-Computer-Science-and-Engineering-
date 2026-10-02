inp = open("input6.txt", "r")
out = open("output6.txt", "w")
N = inp.read().split("\n")
R, H = map(int, N[0].split())
graphSet = [list(i) for i in N[1:]]
def DFS_FloodFill(r, c, rs, cs, gSet):
    if r < 0 or r >= rs or c < 0 or c >= cs or gSet[r][c] == '#':
        return 0
    cnt = 0
    if gSet[r][c] == 'D':
        cnt += 1
    gSet[r][c] = '#'
    cnt += DFS_FloodFill(r + 1, c, rs, cs, gSet)
    cnt += DFS_FloodFill(r - 1, c, rs, cs, gSet)
    cnt += DFS_FloodFill(r, c + 1, rs, cs, gSet)
    cnt += DFS_FloodFill(r, c - 1, rs, cs, gSet)
    return cnt
def countdiamonds(rows, cols, G):
    maxDiamonds = 0
    for r in range(rows):
        for c in range(cols):
            if G[r][c] == '.':
                diamond = DFS_FloodFill(r, c, rows, cols, G)
                maxDiamonds = max(maxDiamonds, diamond)
    return maxDiamonds
result = countdiamonds(R, H, graphSet)
out.write(str(result))
inp.close()
out.close()
# The code employs Depth-First Search (DFS) for flood-fill exploration to find
# the maximum number of diamonds that can be collected in a 2D grid with obstacles.
# It iterates through the grid, marking and counting connected regions of diamonds for
# each empty cell. The maximum count across all starting positions is calculated,
# and the result is printed as the maximum number of diamonds attainable.
# The code ensures that obstacles ('#') prevent movement, and each diamond is counted only once.





