import sys
import re
no_of_test_cases = int(sys.stdin.readline().rstrip())
# print (no_of_test_cases)

# vowel = re.compile('a|e|i|o|u')
for i in range(no_of_test_cases):
    sentence = str(sys.stdin.readline().rstrip())
    # print(sentence)
    sentence_list = list(sentence)
    vowel_count = 0
    for c in sentence_list:
        # if vowel.match(c):
        if (c =='a' or c == 'e' or c == 'i' or c == 'o' or c == 'u'):
            vowel_count += 1
    print (vowel_count)
        


    # for 
    # vowel_count = sum([])
    # print((vowel_count))