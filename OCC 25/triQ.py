a = int(input('Enter a value for A: '))
b = int(input('Enter a value for B: '))
c = int(input('Enter a value for C: '))
d1 = a**2 == b**2 + c**2
d2 = b**2 == a**2 + c**2
d3 = c**2 == a**2 + b**2
if d1 or d2 or d3:
    print('செங்கோண முக்கோணி')
else:
    print('செங்கோண முக்கோணியன்று')
