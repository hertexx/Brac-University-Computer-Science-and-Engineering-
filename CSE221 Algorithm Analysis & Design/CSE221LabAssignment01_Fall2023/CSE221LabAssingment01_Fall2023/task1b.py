input_file = open('input1b.txt', 'r')
output_file = open('output1b.txt', 'w')

n = input_file.readline()
ln=int(n)
for i in range(ln):
    s = input_file.readline().split()
    if s[2]=='+':
        output_file.write('The result of {} {} {} is {}\n'.format(s[1],s[2],s[3],int(s[1])+int(s[3])))
    elif s[2]=='-':
        output_file.write('The result of {} {} {} is {}\n'.format(s[1],s[2],s[3],int(s[1])-int(s[3])))
    elif s[2]=='/':
        output_file.write('The result of {} {} {} is {}\n'.format(s[1],s[2],s[3],int(s[1])/int(s[3])))
    elif s[2]=='*':
        output_file.write('The result of {} {} {} is {}\n'.format(s[1],s[2],s[3],int(s[1])*int(s[3])))
input_file.close()
output_file.close()
#First lines gives the number of times we need to perform calculation
#Then reading each line and spliting it with the .split() built-in funtion and
#compairing the operator in string form for match and then just operating it
#and direct passing it in output file.