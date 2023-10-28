import sys
no_of_test_cases = int(sys.stdin.readline().rstrip())
# print(f'--------------------------debug starting ------------------------------')
for i in range(no_of_test_cases):
    strand = str(sys.stdin.readline().rstrip())
    # print(f'working on strand={strand}')

    n_byte_str = ''
    n_word = ''

    for nucleotides in strand:
        if nucleotides == "A" or nucleotides == "T":
            n_bit = '0'
        if nucleotides == "G" or nucleotides == "C":
            n_bit = '1'
        
        n_byte_str += n_bit

        if (len(n_byte_str) == 7):
            b_int = int(n_byte_str, 2)
            # print(f'ascii integer={b_int}')
            a_char=chr(b_int)
            # print(f'ascii char={a_char}')
            n_word += a_char

            n_byte_str = ''

    print (f'{n_word}')

    # print('nucleotide list =',*n_list)

    # b_int = int('1001001', 2)
    # print(f'ascii integer={b_int}')
    # a_char=chr(b_int)
    # print(f'ascii char={a_char}')

    # print (int('112',10))




