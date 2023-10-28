import sys
import math
cases = int(sys.stdin.readline().rstrip())
for i in range(cases):
    input = sys.stdin.readline().rstrip()
    seperate_numbers= input.split(" ")
    # print (seperate_numbers)
    int_numbers = [int(n) for n in seperate_numbers]
    added_numb=int(seperate_numbers[0])+int(seperate_numbers[1])
    mult_numb=int(seperate_numbers[0])*int(seperate_numbers[1])
    print (f"{added_numb} {mult_numb}")
