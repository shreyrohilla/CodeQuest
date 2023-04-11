# R > S
# P > R
# S > P

import sys
no_of_test_cases = int(sys.stdin.readline().rstrip())
# print (no_of_test_cases)

for i in range (no_of_test_cases):
    all_hands = (sys.stdin.readline().rstrip().split())
    # print (all_hands)

    hand_count = {'R': 0, 'P': 0, 'S': 0}

    for i in range(len(all_hands)):
        j = all_hands[i]
        hand_count[j] += 1

    # print (hand_count)
        
    if hand_count['R'] >= 1 and hand_count['S'] >= 1 and hand_count['P'] >= 1:
        hand_count['R'] = 0
        hand_count['P'] = 0
        hand_count['S'] = 0
    if hand_count['R'] > 0:
        hand_count['S'] = 0
    if hand_count['P'] > 0:
        hand_count ['R'] = 0
    if hand_count['S'] > 0:
        hand_count['P'] = 0

    # print(hand_count)

    if hand_count['R'] > 1 or hand_count['S'] > 1 or hand_count['P'] > 1:
        print ("NO WINNER")
    elif hand_count['R'] == 1:
        print ("ROCK")
    elif hand_count['P'] == 1:
        print ("PAPER")
    elif hand_count['S'] == 1:
        print ("SCISSORS")
    else:
        print ("NO WINNER")
