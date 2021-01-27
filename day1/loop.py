for i in range(4):
    print(i)

a = [1, 2, 3]
b = [4, 5, 6]

a = [3, 5, 2, 1]
for i in range(len(a)):
    if (a[i] == 2):
        print(i)

a= [1, 2]
# print(list(enumerate(a))[0]) 
b, c = list(enumerate(a))[1]
print(c)

a = [3, 5, 2, 1]
for index, value in enumerate(a):
    if (value == 2):
        print(index)

a = [3, 5, 2, 1]
for index, value in enumerate(a):
    if (value == 2):
        print(index)
        break
    print(index)