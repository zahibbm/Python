file=open('student.txt','r')
line=file.readline()
result='No Result Found!'
findIndex=input('Index: ')
while line:
    index,name=line.split(',')
    # index=line.split(',')[0]
    # name=line.split(',')[1]
    if index==findIndex:
        result=name
        break
    line=file.readline()
print(result)
file.close()