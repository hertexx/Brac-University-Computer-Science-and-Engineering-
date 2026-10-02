inp = open('input2a.txt', 'r')
out = open('output2a.txt', 'w')
n = int(inp.readline())
lst1 = list(map(int, inp.readline().split()))
m = int(inp.readline())
lst2 = list(map(int, inp.readline().split()))
a = []
i, j = 0, 0
while i < n and j < m:
    if lst1[i] <= lst2[j]:
        a.append(lst1[i])
        i += 1
    else:
        a.append(lst2[j])
        j += 1
while i < n:
    a.append(lst1[i])
    i += 1

while j < m:
    a.append(lst2[j])
    j += 1
for i in a:
    out.writelines(str(i)+" ")
inp.close()
out.close()
# Built-in funtion as map to convert the variables in the string into integer after splitting with .spilt()
# and stored in a list. The code merges two sorted lists efficiently by iterating through both lists
# with two pointers, comparing elements at each step. It appends the smaller element to the merged list,
# incrementing the corresponding pointer. This process continues until both input lists are fully traversed.
# Any remaining elements in either list are then appended to the merged list and pass to be written in the output file by loop.