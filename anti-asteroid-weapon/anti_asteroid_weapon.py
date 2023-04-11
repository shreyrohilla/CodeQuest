import sys
import math
def distance(x, y):
    return math.sqrt(x**2 + y**2)
#run = "python3 main.py < 1.in"
cases = int(sys.stdin.readline().rstrip())
# numOfLines = int(sys.stdin.readline().rstrip())
# f4ate_numbers=input.split(" ")
for i in range(cases):
    # input = sys.stdin.readline().rstrip()
    # #numOfLines = int(sys.stdin.readline().rstrip())
    # seperate_numbers=input.split(" ")
    a = int((sys.stdin.readline().rstrip()))
    coords = []
    for j in range(a):
        x, y = map(int, input().split())
        coords.append((x, y))
        # x, y =map(coords.split(" "))   
        # print (x, y)
        #coords.append((x,y))
    coords.sort(key=lambda a: distance(a[0], a[1]))
    for a in coords:
        print (f"{a[0]} {a[1]}")

