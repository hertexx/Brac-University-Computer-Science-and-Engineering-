inp = open("input5.txt", "r")
out = open("output5.txt", "w")
N = int(inp.readline())
arr = list(map(int, inp.readline().split()))
def quicksort(a, p, r):
    if p<r:
        q = partition(a, p, r)
        quicksort(a, p, q-1)
        quicksort(a,q+1,r)
def partition(a, p, r):
    x = a[r]
    i = p-1
    for j in range(p, r, 1):
        if a[j] < x:
            i +=1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[r] = a[r], a[i+1]
    return i+1

quicksort(arr, 0, N - 1)
arr = list(map(str, arr))
out.write(" ".join(arr))
inp.close()
out.close()
# It reads the input values from "input5.txt," which includes the size 'N' and the integer array 'arr.'
# The 'quicksort' function recursively sorts the array 'arr' using the quicksort algorithm.
# It selects a pivot element and partitions the array into two subarrays, then recursively sorts these subarrays.
# The 'partition' function chooses a pivot element, rearranges the elements in 'arr' such that elements less than
# the pivot are on the left, and elements greater than the pivot are on the right. It returns the index of the pivot  element.
# After sorting, the code converts the sorted array into a list of strings and writes them to "output5.txt" in ascending order.