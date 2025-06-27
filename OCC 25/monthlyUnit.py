deviceCount=int(input('Device Count: '))
dayUnit=0
for device in range(deviceCount):
# for device in range(1,deviceCount+1):
# for device in range(deviceCount,0,-1):
# while deviceCount>0:
    count=int(input('Number of Devices: '))
    w=int(input('Watt : '))
    h=float(input('Hours: '))
    unit=w*h/1000*count
    dayUnit+=unit
    # deviceCount-=1
print('Monthly Unit:',dayUnit*30)