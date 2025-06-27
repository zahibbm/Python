def rList():
    list=input('Enter a List:').split(',')
    for t in range(len(list)):
        list[t]=int(list[t])
    return list
print(rList())