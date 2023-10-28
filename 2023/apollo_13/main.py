import sys
import math

cases = int(sys.stdin.readline().rstrip())
# print (cases)

for i in range(cases):
    angles_list = (sys.stdin.readline().rstrip().split(" "))
    # print (angles_list)

    # new_angles = 0

    ans = ''

    for i in range(len(angles_list)):
        # print (i)
        j = angles_list[i]
        # print (j)

        new_angles = float(j) - 180

        if new_angles < 0:
            new_angles += 360

        # print(new_angles)

        ans += str(f'{new_angles:06.2f}') + ' '
    print (ans.strip())
