def findMax(n1,n2):
    if n1>n2:
        return n1
    return n2
n1=int(input())
n2=int(input())
n3=int(input())
temp=findMax(n1,n2)
print(findMax(temp,n3))
print(findMax(findMax(n1,n2),n3))






