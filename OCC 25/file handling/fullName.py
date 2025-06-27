file = open('name.txt','w')
x=int(input())
file.write(str(x*10))
# for i in range(10):
#     fname = input('First Name : ')
#     lname = input('Last Name : ')
#     fullname = fname + ' ' + lname
#     file.write(fullname) 
file.close()
