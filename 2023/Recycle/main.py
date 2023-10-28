import sys

#python3 main.py < recycleSamples/1.in

#run = "python3 main.py < 1.in"
cases = int(sys.stdin.readline().rstrip())
# numOfLines = int(sys.stdin.readline().rstrip())

for i in range(cases):
  input = sys.stdin.readline().rstrip()
  #numOfLines = int(sys.stdin.readline().rstrip())

  seperate_numbers=input.split(" ")
  # print(seperate_numbers[0])
  # print(f'and here is the second number {seperate_numbers[1]}')
  aluminum_cans_weight= float(seperate_numbers[0])
  #print(f' weight of cans {aluminum_cans_weight}')
  plastic_bottles_weight= float(seperate_numbers[1])
#  print(f' weight of plastic bottles {plastic_bottles_weight}')
  glass_bottles_weight= float(seperate_numbers[2])
 # print(f' weight of glass bottles {glass_bottles_weight}')
# Conversion rates
  ALUMINUM_CAN_RATE = 31
  PLASTIC_BOTTLE_RATE = 15
  GLASS_BOTTLE_RATE = 0.5

# Rebate rates
  ALUMINUM_CAN_REBATE = 0.05
  PLASTIC_BOTTLE_REBATE = 0.1
  GLASS_BOTTLE_REBATE = 0.2

# Take input from user
# aluminum_cans_weight = float(input("Enter weight of aluminum cans (in pounds): "))
# plastic_bottles_weight = float(input("Enter weight of plastic bottles (in pounds): "))
# glass_bottles_weight = float(input("Enter weight of glass bottles (in pounds, must be even): "))

# Calculate total number of items based on weight
  total_aluminum_cans = int(aluminum_cans_weight * ALUMINUM_CAN_RATE)
  total_plastic_bottles = int(plastic_bottles_weight * PLASTIC_BOTTLE_RATE)
  total_glass_bottles = int(glass_bottles_weight * GLASS_BOTTLE_RATE)

# Calculate total rebate amount
  total_rebate = (total_aluminum_cans * ALUMINUM_CAN_REBATE) + (total_plastic_bottles * PLASTIC_BOTTLE_REBATE) + (total_glass_bottles * GLASS_BOTTLE_REBATE)

# Print the rebate amount
  print(f"${total_rebate:.2f}")
