def sum_of_digits(n):
    sum = 0
    while(n):
        sum += n % 10
        n  //= 10
    return sum

n = int(input())
print(n)
while( n >= 10 ):
    n = sum_of_digits(n)
    print(n)
