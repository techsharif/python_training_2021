# # 01
# l = [4, 2, 7, 4, 9, 1, 4]
# print(l)
# print(l[:])
# print(l[1:4])
# print(l[1:4:2])
# print(l[1:4:-1])
# print(l[::-1])
# print(l[:4:-1])
# print(l[3::-1])
# l = l[:4]
# l = l[::-1]


# # 02
# l1 = [1, 2]
# l2 = [3, 4]
# l3 = [l1, l2]
# print(l3) 
# print(l3[1][1])

# l2[1] = 7
# print(l1)
# print(l2)
# print(l3)

# l4 = [l2, l1]
# l5 = [l3, l4]

# print(l4)
# print(l5)

# l1[1] = 5
# print(l5)

# l5[1][1][1] = 9
# print(l4)
# print(l5)



# l1 = [1, 2]
# l2 = [3, 4]
# l3 = [l1, l2]
# l4 = [l1[:], l2[:]]
# l1[1] = 7
# print(l3)
# print(l4)

# l1 = [1, 2]
# l2 = l1
# l3 = l1[:] # [1, 2]
# print(id(l1))
# print(id(l2))
# print(id(l3))


# l1 = [1,2]
# l2 = [l1, l1]
# # print(l2)
# l3 = l2
# l4 = l2[:]
# # print(l3) #1,2   1,2 
# # print(l4) #1,2   1,2
# l2[1] = [3, 4]
# l1[1] = 7
# print(l3) # [1, 2]  [3, 4]
# print(l4) # [1, 2]  [1, 2]




# # 03
# import copy

# l1 = [1, 2]
# l2 = [3, 4]
# l3 = copy.deepcopy([l1, l2]) # l3 = [l1, l2]
# print(l3)
# print(l3[1][1])

# l2[1] = 7
# print(l1)
# print(l2)
# print(l3)

# l4 = copy.deepcopy([l2, l1])
# l5 = copy.deepcopy([l3, l4])

# print(l4)
# print(l5)

# l1[1] = 5
# print(l5)

# l5[1][1][1] = 9
# print(l4)
# print(l5)