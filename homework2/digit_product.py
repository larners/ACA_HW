def digit_product(n):
    res = 1
    while(n) :
        if( n % 10 ) :
            res *= n % 10
        n  //= 10
    return res

n = int(input())
print(digit_product( n ))
