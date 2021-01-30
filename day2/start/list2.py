t1 = [2, 9, 4]
t2 = [3, 1]

t1.append(6)
print(t1)

t1.extend(t2)
print(t1)

t1.sort()
print(t1)

x = t1.pop(2)
print(t1, x)

t1.remove(6)
print(t1)

