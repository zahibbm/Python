factors=open('factors.txt','w')
num = int(input())
t=1
# factors.write('%d -> '%(num))
factors.write('{} ->\t'.format(num))
while t<=num:
    if num%t==0:
        # factors.write('%d\t'%(t))
        factors.write('{}\t'.format(t))
    t+=1
factors.close()