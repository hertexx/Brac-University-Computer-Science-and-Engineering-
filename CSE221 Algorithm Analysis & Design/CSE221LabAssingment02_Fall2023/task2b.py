inp = open('input2b.txt', 'r')
out = open('output2b.txt', 'w')
n = int(inp.readline())
lst1 = list(map(int, inp.readline().split()))
m = int(inp.readline())
lst2 = list(map(int, inp.readline().split()))
maxLen = max(n, m)
a = []
i, j = 0, 0
while True:
    if i == n:
        a += lst2[j:]
        break
    elif j == m:
        a += lst1[i:]
        break
    elif lst1[i] < lst2[j]:
        a.append(lst1[i])
        i += 1
    elif lst1[i] > lst2[j]:
        a.append(lst2[j])
        j += 1
    elif lst1[i] == lst2[j]:
        a.append(lst1[i])
        a.append(lst2[j])
        i += 1
        j += 1
for i in a:
    out.writelines(str(i)+" ")
inp.close()
out.close()
# Built-in funtion as map to convert the variables in the string into integer
# after splitting with .spilt() and stored in a list. A while loop is used with 2 iterator i and j
# for the 2 sorted data list stored in variable lst1 and lst2 elem in them are compared with index i and j
# respectively and stored in a new list with variable 'a'. If any list reaches its last index before the other
# then the other list remaining elements are pasted to "a" and writen in the output file.