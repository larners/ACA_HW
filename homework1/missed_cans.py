def missed_cans( num_1, num_2 ):
    sum = num_1 + num_2 - 1
    return sum - num_1, sum - num_2

cans_num_1 = int( input( 'the number of cans the first man : ' ) )
cans_num_2 = int( input( 'the number of cans the second man : ' ) )
missed1, missed2 = missed_cans(cans_num_1, cans_num_2)
print(missed1)
print(missed2)
