def four_dig_sum( num ) :
    sum = 0
    while( num != 0 ) :
        sum += num % 10
        num = num // 10
    return sum

num = int( input() )
print( four_dig_sum(num)  )

