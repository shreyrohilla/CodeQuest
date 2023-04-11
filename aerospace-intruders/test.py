import sys
import re

myList = [[504, 1, 2, 12], [5, 3, 77], [12, 104, 34]]
print("The input list is:", myList)
myList.sort(key=lambda inner_list:inner_list[2])
print("The sorted list is:", myList)

data = [[1,2,3], [4,5,6]]
data.sort (key= lambda x:x[1], reverse=False)
print(data)

output = []
for i in data:
    sublist = []
    for j in i:
        sublist.append(j)
    output.append(sublist)
print(output)