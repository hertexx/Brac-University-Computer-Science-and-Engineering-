input_file = open('input2.txt', 'r')
output_file = open('output2.txt', 'w')

s = input_file.readline()
ln=int(s)
a = list(map(int, input_file.readline().split()))
for i in range(ln-1):
    flag=False
    for j in range(ln-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            flag=True
    if not flag:
        break
for k in a:
    output_file.write(str(k)+' ')
input_file.close()
output_file.close()
#First line gives no. of integers to compair and also use for loop iteration
#and the integer values are in a list where map and split built in funtion is used to convert after reading it from file.
# We used bubble sort where a flag is used to check if any swap made while passing through the array
#If no swap made in a pass, the loop brakes as array already sorted.