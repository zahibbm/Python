# method 1 -> Read
# toRead = open('vehicle.txt')
# toWrite = open('xVehicle.txt','w')
# data = toRead.read()
# toWrite.write(data)
# toRead.close()
# toWrite.close()

# method 2 -> Read Line
toRead = open('vehicle.txt')
##toWrite = open('vNames.txt','w')
total=0
for i in range(4):
    line = toRead.readline() 
    line = line.split()
    count = line[1]
    total+=int(count)
print(total)
toRead.close()
##toWrite.close()





