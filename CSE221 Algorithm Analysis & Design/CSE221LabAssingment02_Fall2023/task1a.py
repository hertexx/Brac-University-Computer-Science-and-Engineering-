inp = open('input1a.txt', 'r')
out = open('output1a.txt', 'w')
n, s = map(int, inp.readline().split())
lst = list(map(int, inp.readline().split()))
for i in range(n):
    flag = False
    for j in range(i+1, n):
        if lst[i]+lst[j] == s:
            flag = True
            out.write(str(i+1)+' '+str(j+1))
            break
    if flag:
        break
    elif i == n-1 and not flag:
        out.write('IMPOSSIBLE\n')
inp.close()
out.close()
# We used the map and .split() built-in funtion to the string read lines from the file in form of list.
# Furthermore, we used a nested for loop checking O(n^2), both loop iterates for n times.
# For inner loop it starts from i to n, where the 'i' is the first loop index.
# The loop breaks once it gets the s, by summing the i and j index in lst list that should sum to 's'
# And the output is written the outfile file.