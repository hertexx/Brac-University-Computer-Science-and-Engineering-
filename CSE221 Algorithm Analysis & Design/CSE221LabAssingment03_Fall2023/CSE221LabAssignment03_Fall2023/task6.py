inp = open("input6.txt", "r")
out = open("output6.txt", "w")
na = int(inp.readline().split()[0])
arr = list(map(int, inp.readline().split()))
nq = int(inp.readline().split()[0])
def partition(a,p,r):
    x = a[r]
    i = p-1
    for j in range(p, r, 1):
        if a[j]<x:
            i +=1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[r] = a[r], a[i+1]
    return i+1

def smallest(a, k):
    p = 0
    r = len(a)-1

    while p <= r:
            pivotIdx = partition(a,p,r)
            if pivotIdx==k-1:
                return a[pivotIdx]
            elif pivotIdx>k-1:
                r = pivotIdx-1
            else:
                p = pivotIdx+1
    return None


for i in range(nq):
  result = smallest(arr, int(inp.readline()))
  out.write(str(result) + "\n")
inp.close()
out.close()
#The code reads an array 'arr' and a list of queries from "input6.txt."
# It employs the quickselect algorithm to find the kth smallest element in 'arr'
# for each query. The 'partition' function partitions the array, and 'findkSmallest'
# repeatedly applies this partitioning to determine the kth smallest element.
# The results of the queries are written to "output6.txt," and the code closes the
# input and output files.