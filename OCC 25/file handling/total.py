file=open('marks.txt','w')
stuCount=int(input('No of Students: '))
for i in range(stuCount):
    m1 = int(input())   
    m2 = int(input())
    m3 = int(input())
    avg=(m1+m2+m3)/3
    file.write('%d %d %d %.1f\n'%(m1,m2,m3,avg))
# file.write(str(m1)+' '+str(m2)+' '+str(m3)+' '+str(avg))
file.close()
