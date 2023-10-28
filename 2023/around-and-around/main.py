import sys
import math

e_radius = (40075/2)/math.pi
# print (e_radius)
test_cases = int(sys.stdin.readline().rstrip())
# print (test_cases)
for i in range (test_cases):
    altitude = int(sys.stdin.readline().rstrip())
    # print (altitude)

    rad_altitude = altitude + e_radius

    new_circ = rad_altitude*2*math.pi

    print (round (new_circ, 1))

