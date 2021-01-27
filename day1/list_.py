a = []
print(a)
print(len(a))

a = []
a.append(4)
a.append(5.6)
a.append("hello")

print(a) # [4, 5.6, 'hello'] a[0] -> 4
print(len(a))


a = [5, 2.3, "hello"]
print(a[2])
print(a[-1])

print(a[1] == a[-2])

a = []
a = a + [3] # a.append(3)
a += [4] # a.append(4)
a += [5, 6, 7] # a.extend([5, 6, 7])

print(a)

a = [1, 2, 3]
b = [4, 5, 6]

a += b
print(a)


a = [1, 2, 3, 4, 5, 6]

print(a[2:5])
print(a[:5])
print(a[2:])
print(a[:])

a = [1, 2, 3]
b = [4, 5, 6]

b += a # 4 5 6 1 2 3
a += b # 1 2 3 4 5 6 1 2 3
print(a) # 123456123
print(a[2:6]) # 3456
print(a[6:]) # 123

# l = {1, 2}
# t = tuple(l)