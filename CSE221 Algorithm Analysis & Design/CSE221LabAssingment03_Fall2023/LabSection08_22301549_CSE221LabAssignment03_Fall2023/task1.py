inp = open('input1.txt', 'r')
out = open('output1.txt', 'w')
n = int(inp.readline())
lst = list(map(int, inp.readline().split()))
def merge(a, b):
    lst1 = a
    n = len(a)
    lst2 = b
    m = len(b)
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
    return a
def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr)//2
        a1 = mergeSort(arr[:mid])  # write the parameter
        a2 = mergeSort(arr[mid:])  # write the parameter
        return merge(a1, a2)
a = mergeSort(lst)
for i in a:
    out.writelines(str(i)+" ")
inp.close()
out.close()
# It reads input data from 'input1.txt', where the first line specifies the number of elements (n),
# and the second line contains the list of integers to be sorted. The mergeSort function recursively divides
# the input list into smaller sublists until each sublist contains only one element (base case).
# The merge function is responsible for merging two sorted sublists into a single sorted list.
# It iterates through the sublists, comparing elements and merging them in ascending order while handling duplicate elements.
# The mergeSort function returns the sorted list, which is then written to 'output1.txt' with each element separated by a space.
