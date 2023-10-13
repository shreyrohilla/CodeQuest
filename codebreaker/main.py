import sys

letter_count = {'A': 0, 'B': 0, 'C': 0,
                'D': 0, 'E': 0, 'F': 0, 
                'G': 0, 'H': 0, 'I': 0, 
                'J': 0, 'K': 0, 'L': 0,
                'M': 0, 'N': 0, 'O': 0, 
                'P': 0, 'Q': 0, 'R': 0, 
                'S': 0, 'T': 0, 'U': 0, 
                'V': 0, 'W': 0, 'X': 0, 
                'Y': 0, 'Z': 0}

cases = int(sys.stdin.readline().rstrip())
for i in range(cases):

    sentences_count = int(sys.stdin.readline().rstrip())
    sentences = ''
    for j in range(sentences_count): 
        sentences += (sys.stdin.readline().rstrip())

    new_sentence = ''
    for chr in sentences:
        if chr.isalpha():
            new_sentence += chr.upper()

    # print(new_sentence)

    for char in (new_sentence):
        letter_count[char] += 1
    
    # print(letter_count)

    total_letters = len(new_sentence)

    for letter, count in letter_count.items():
        frequency = count / total_letters
        print(f"{letter}: {frequency:.2%}")

    letter_count = {'A': 0, 'B': 0, 'C': 0,
                    'D': 0, 'E': 0, 'F': 0, 
                    'G': 0, 'H': 0, 'I': 0, 
                    'J': 0, 'K': 0, 'L': 0,
                    'M': 0, 'N': 0, 'O': 0, 
                    'P': 0, 'Q': 0, 'R': 0, 
                    'S': 0, 'T': 0, 'U': 0, 
                    'V': 0, 'W': 0, 'X': 0, 
                    'Y': 0, 'Z': 0}
    # print (letter_count)
