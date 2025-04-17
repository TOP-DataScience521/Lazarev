binary = {'0', '1', 'b'}
sequence = input().lower()
if set(sequence) | binary == binary and 'b' not in set(sequence[2:]) and (sequence[:2] in {'00', '01', '10', '11', 'b0', 'b1'} or sequence[:2] == '0b' and len(sequence) > 2):
    print('да')
else:
    print('нет')


# b111111111111111111111111101
# да


# b11111111111b111111111111101
# нет

