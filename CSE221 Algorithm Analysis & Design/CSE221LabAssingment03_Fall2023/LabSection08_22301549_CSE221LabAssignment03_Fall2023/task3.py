inp = open("input3.txt", "r")
out = open("output3.txt", "w")
N = inp.readline().split()
arr = list(map(int, inp.readline().split()))
def maxCnt(arr):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    left, cntL = maxCnt(arr[:mid])
    right, cntR = maxCnt(arr[mid:])
    sortedArray, cnt = pairCnt(left, right)
    totalCnt = cntL + cntR + cnt
    return sortedArray, totalCnt

def pairCnt(left, right):
    lst = []
    cnt = 0
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            lst.append(left[i])
            cnt += len(right) - j
            i += 1
        else:
            lst.append(right[j])
            j += 1
    lst.extend(left[i:])
    lst.extend(right[j:])

    return lst, cnt

sortedArray, cnt = maxCnt(arr)
out.write(str(cnt))
out.close()
#I have used the divide and conquer approach to Solue the problem.
# The 'maxCnt' function performs merge sort using left and right subarrays.
# It is uses the 'pairCnt'funtion to check if left array's element is greater than
# right and increment the count variable. It append the count in total is obtain by adding the counts from the left and right subarrays and
# adding the counts from the left and right subarrays and sorting helps to find all kinds of posssible pairs.