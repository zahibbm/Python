file=open('student.txt','r')
line=file.readline()
found='இல்லை'
findIndex=input('Index: ')
while line:
    index=line.split(',')[0]
    if index==findIndex:
        found='ஆம்'
        break
    line=file.readline()
print(found)
file.close()