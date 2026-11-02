input_file = open('input3.txt', 'r')
output_file = open('output3.txt', 'w')
n = input_file.readline()
ln = int(n)
st_id = list(map(int,input_file.readline().split()))
st_marks=list(map(int,input_file.readline().split()))
st_info=[(st_id[i],st_marks[i]) for i in range(ln)]
maxM=None
for i in range(ln):
    maxM=st_info[i][1]
    maxM2=None
    midx=i
    for j in range(i+1,ln):
        if st_info[j][1]>maxM and maxM2==None:
            maxM2=st_info[j][1]
            midx=j
        elif st_info[j][1]>maxM and st_info[j][1]>maxM2:
            maxM2=st_info[j][1]
            maxidx=j
    t=st_info[i]
    st_info[i]=st_info[midx]
    st_info[midx]=t
maxId=None
for k in range(ln):
    maxId=st_info[k]
    maxId2=None
    midx=k
    for h in range(k+1,ln):
        if st_info[h][1]!=maxId[1]:
            break
        elif st_info[h][0]<maxId[0] and maxId2==None and st_info[h][1]==maxId[1]:
            maxId2=st_info[h][0]
            midx=h
        elif st_info[h][0]<maxId[0] and maxId[0]>maxId2 and st_info[h][1]==maxId[1]:
            maxId2=st_info[h][0]
            haxidx=h
    t=st_info[k]
    st_info[k]=st_info[midx]
    st_info[midx]=t
for l in range(ln):
    output_file.write('ID: '+str(st_info[l][0])+' ')
    output_file.write('Mark: '+str(st_info[l][1])+'\n')                  
input_file.close()
output_file.close()
#A values of the id and marks for candidates is stored in a tuple and then is a list,
#by reading from the file and using map and split built-in funtion. Then for the minmum swap
#firstly max mark wised sorted by the first double loop where the first candidate mark is considered 
#as the max mark and stored in a variable, then compaired with the rest of the marks in the list 
#and in second variable the 2nd max marks is stored and compaired the postion of a candidate is only swap when
#with the 2nd max if only when higher marks. Simiarly sorted for id.