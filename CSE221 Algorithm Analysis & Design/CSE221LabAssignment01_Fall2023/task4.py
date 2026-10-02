input_file = open('input4.txt', 'r')
output_file = open('output4.txt', 'w')

n = input_file.readline()
ln = int(n)
dic={}
for i in range(ln):
    s=input_file.readline().split()
    if s[0] not in dic.keys():
        dic[s[0]]=[]
        dic[s[0]].append((s[6],s[4]))
    else:
        dic[s[0]].append((s[6],s[4]))
mk=list(dic.keys())
for i in range(len(mk)-1):
    for j in range(i,len(mk)):
        if mk[i]>mk[j]:
            mk[i],mk[j]=mk[j],mk[i]
nDic={i:dic[i] for i in mk}
for key,val in nDic.items():
    for i in range(len(val)-1):
        flag=False
        for j in range(len(val)-i-1):
            if val[j][0]<val[j+1][0]:
                val[j],val[j+1]=val[j+1],val[j]
                flag=True      
        if not flag:
            break
for key,val in nDic.items():
    for v in val:
        output_file.write('{} will Departure from {} at {}.\n'.format(key,v[1],v[0]))
input_file.close()
output_file.close()
#First line gives the number of input and which means no. of loop iterated
#dictonary is used to store data, where the train name is key and the val is (time,location) in tuple respectively for all input lines.
#the dictonary is then sorted firstly by keys where it keys are first taken in a list 
#and sorted then new dictonary created and stored.Than the dictonary values are sorted with recent departure at first 
#and no change for similar time and the data is written in the output file.