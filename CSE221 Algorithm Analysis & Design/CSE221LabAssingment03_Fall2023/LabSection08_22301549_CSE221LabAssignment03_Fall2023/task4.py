inp = open("input4.txt", "r")
out = open("output4.txt", "w")
N = int(inp.readline())
arr = list(map(int, inp.readline().split()))
def maxF(arr):
    if len(arr) <= 1:
        return arr, int(arr[0])
    mid = len(arr) // 2
    left, maxVal = maxF(arr[:mid])
    right, maxVal = maxF(arr[mid:])
    maxFindA, val = maxFindVal(left, right, maxVal)
    return maxFindA, val
def maxFindVal(left, right, maxVal):
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        exp = (left[i] + right[j]*right[j])
        maxVal = max(maxVal, (left[i] + right[j]*right[j]))
        if left[i] <= right[j]:
            i += 1
        else:
            j += 1
    return left+right, maxVal
sortedA, maxV = maxF(arr)
out.write(str(maxV))
inp.close()
out.close()
#It reads the input values from "input4.txt" and stores the array size 'N' and the elements in 'arr.'
#The 'maxF' function recursively divides the 'arr' into left and right subarrays and
# computes the maximum value within those subarrays. It returns both the subarray and the maximum value within it.
#The 'maxFindVal' function finds the maximum value across two subarrays by iterating through both subarrays
# and comparing the expressions at each position. It updates the 'maxVal' as it goes.
#The 'maxF' function then combines the results from the left and right subarrays and returns the overall maximum value
# along with the subarray that contributes to it.The code finally writes the maximum value to "output4.txt."