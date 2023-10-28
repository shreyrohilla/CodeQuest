import sys
no_of_test_cases = int(sys.stdin.readline().rstrip())
for i in range(no_of_test_cases):
    words = (sys.stdin.readline().rstrip().split('|'))
    word_1 = words[0]
    word_2 = words[1]
    if word_1 == word_2:
        print (f"{word_1}|{word_2} = NOT AN ANAGRAM")
    elif sorted(word_1) == sorted(word_2):
        print (f"{word_1}|{word_2} = ANAGRAM")
    else:
        print (f"{word_1}|{word_2} = NOT AN ANAGRAM")

