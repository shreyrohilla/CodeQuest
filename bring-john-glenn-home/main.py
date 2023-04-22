import sys
import math

no_of_test_cases = int(sys.stdin.readline().rstrip())
for i in range(no_of_test_cases):
    variables_list = (sys.stdin.readline().rstrip().split(" "))
    
    x = float(variables_list[0])
    y = float(variables_list[1])
    h = float(variables_list[2])
    n = int(variables_list[3])

    for i in range(n):
        x_calc = (h)+(x)

        y_calc = (y)+(h)*(math.sin(x)/(x))
        
        y = y_calc
        x = x_calc
    print (f'{round(y, 3)}')