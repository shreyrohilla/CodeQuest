import sys
no_of_test_cases = int(sys.stdin.readline().rstrip())
for i in range(no_of_test_cases):
    sentence = str(sys.stdin.readline().rstrip())
    reverced_sentence = sentence[::-1]
    # interate backwards :)
    print (reverced_sentence)
