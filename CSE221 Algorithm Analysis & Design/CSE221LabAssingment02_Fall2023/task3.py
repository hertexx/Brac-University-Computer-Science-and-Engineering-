inp = open('input3.txt', 'r')
out = open('output3.txt', 'w')
n = int(inp.readline())
a = []
for i in range(n):
    a.append(tuple(map(int, inp.readline().split())))
a.sort(key=lambda x: x[1])
intCom = [a[0]]
interval = a[0][-1]
for elem in a:
    if elem[0] >= interval:
        interval = elem[1]
        intCom.append(elem)
n = len(intCom)
out.write(str(n)+'\n')
for i in intCom:
    out.write(str(i[0])+' '+str(i[1])+'\n')
inp.close()
out.close()
# First line from the file gives the number of interval time variables available.
# And so we read that number of times from the file and turn it into integer values
# and store it as tuple in a list as names "a". Then it was sorted using .sort() funtion according to the end time interval.
# And initially the end of first set is taken as limit then comparing the sets of interval with the start of each
# task and if equal or greater then it is chosen and add to the 'intCom' variable and the interval time is updated
# as the end time of the chosen set end time interval and at last the 'intCom' is written in the output file as asked.
