def arithmetic_prog(a1, a2, n) :
    d = a2 - a1
    return a1 + (n-1) * d

a1 = int( input('First elem : ') )
a2 = int( input('Second elem : ') )
n = int( input('n : ') )

print(arithmetic_prog( a1, a2, n ) )
