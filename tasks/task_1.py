a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for i in a:
   if i < 5:
       print(i, end = " ")

print(list(filter(lambda elem: elem < 5, a)))

print([i for i in a if i < 5])
