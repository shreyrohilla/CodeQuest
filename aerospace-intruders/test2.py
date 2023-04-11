import sys

L1=[[4,5,6,7], [0,7,2,8]]

# print(L1[2])

# for value in L1:
#     print(value)

print(L1)
L1.sort(key=lambda x:x[3], reverse=True)
print(L1)
