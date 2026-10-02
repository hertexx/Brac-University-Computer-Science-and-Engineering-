inp = open('input4.txt', 'r')
out = open('output4.txt', 'w')
n, m = list(map(int, inp.readline().split()))
a = []
for i in range(n):
    a.append(list(map(int, inp.readline().split())))
a.sort(key=lambda x: x[0])
cnt = 0
eTime = [-1]*m
for i in range(n):
    for j in range(m):
        if a[i][0] >= eTime[j]:
            eTime[j] = a[i][1]
            cnt += 1
            break
out.write(str(cnt)+'\n')
inp.close()
out.close()
# The first readline is split and stored in n and m respectively, a set loop to store the time interval in set as tuple in list 'a'.
# Then it is sorted by fist element start of a set interval. The to find the number of completed task we take a list where we
# store the end of doing task for a person 'm' is the no. of person. Then a nested loop, where the loop iterates for n and m respectively
# so we compair the set of intervals with time in the eTime for m people where it's initially from -1 and increase as each person gets work
# and cnt increases and when all possible time compared then the cnt is written in the output file.