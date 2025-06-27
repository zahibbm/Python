sum=0
count=0
marks = int(input('Marks: '))
while marks != -1:
    count+=1
    sum+=marks
    marks = int(input('Marks: '))
print(sum/count)