n = int(input())
power = 1
for i in range(n+1):
    if( 3**i > n ):
        print(power)
        break
    power = 3**i

