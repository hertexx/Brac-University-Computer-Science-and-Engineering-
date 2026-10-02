inp = open('input2.txt', 'r')
out = open('output2.txt', 'w')
N = int(inp.readline())
arr = list(map(int, inp.readline().split()))
def maxC(arr):
    if len(arr) <= 1:
        return arr[0]
    else:
        mid = len(arr)//2
        a1 = maxC(arr[:mid])
        a2 = maxC(arr[mid:])
        return max(a1, a2)
a = maxC(arr)
out.write(str(a))
inp.close()
out.close()
#The given code reads an input file named 'input2.txt' to obtain an integer 'N'  a list of integers 'arr.'
# It then defines a recursive function 'maxC' to find the maximum element in the list.
# The 'maxC' function splits the list in half until it reaches lists with one or zero elements,
# returning the maximum value of those individual lists. Finally, it computes the maximum of
# the maximum values from both halves (a1 and a2) and stores it in 'a'. This process continues recursively
# until the function reaches the base case with only one element, which is the maximum value in the entire 'arr.'
# The result 'a' is then written to an output file 'output2.txt.'