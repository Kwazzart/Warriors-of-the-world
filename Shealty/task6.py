x1 = int(input('enter x1: '))
y1 = int(input('enter y1: '))
x2 = int(input('enter x2: '))
y2 = int(input('enter y2: '))
distance = round((x1 - x2)**2 +
(x2 - y2)**2, 3)
print('distance between points is: ' + str(distance))