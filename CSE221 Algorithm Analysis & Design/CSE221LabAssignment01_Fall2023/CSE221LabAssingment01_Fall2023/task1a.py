input_file = open('input1a.txt', 'r')
output_file = open('output1a.txt', 'w')

n = input_file.readline()
ln=int(n)
for i in range(ln):
    inp = input_file.readline()
    num=int(inp)
    if num%2==0:
        output_file.write(str(num)+' is an Even number.\n')
    else:
        output_file.write(str(num)+' is an Odd number.\n')
input_file.close()
output_file.close()
#From the first line in the input.txt we get the number of
#variables to compair, so iterating the loop that many times and
#reading the variables and mod it by 2 for 0 as multiple, that indicates Even
#orelse Odd.