inp = open('input1b.txt', 'r')
out = open('output1b.txt', 'w')
n, s = map(int, inp.readline().split())
lst = list(map(int, inp.readline().split()))
i, j = 0, 1
while True:
    if i == n-1:
        out.write('IMPOSSIBLE')
        break
    elif lst[i]+lst[j] == s:
        out.write(str(i+1)+' '+str(j+1))
        break
    if j == n-1:
        j = i+1
        i += 1
    j += 1
inp.close()
out.close()
# As we can see the loop runs with O(n) solution. Similarly, as in 1a built-in
# funtion are used and values are stored. Here, initially i starts from 0 and j from 1
# as index in lst list, as j is increased by 1 if sum of elem in index i and j not match.
# When j reaches last index j is set to i and i is increased by 1. If i reaches last index
# then impossible to solve or no solution. As no elem give the stored sum 's'.