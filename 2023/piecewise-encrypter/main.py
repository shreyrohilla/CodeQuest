import sys
import re
no_of_test_cases = int(sys.stdin.readline().rstrip())
# print (no_of_test_cases)

for i in range (no_of_test_cases):

    word = (sys.stdin.readline().rstrip())

    letters = list(word)
    # print(letters)

    
    letter_values = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
    
    # for i in range(len(letters)):
    #     j = letters[i]
    #     l_numb = letter_values[j]
    # print(j, l_numb)
    for i in word:
        # j = letters[i]
        l_numb = letter_values[i]
        print(i, l_numb)
    