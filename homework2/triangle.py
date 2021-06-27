def type_of_triangle(a, b, c):
    if( a > b ):
        a, b = b, a
    if( b > c ):
        b, c = c, b

    if( a + b <=  c ):
        print('No Triangle')
    else:
        a *= a
        b *= b
        c *= c
        if( c == a + b ):
            print('Right Triangle')
        elif( c > a + b ):
            print('Obtuse Triangle')
        else:
            print('Acute Triangle')

a = int(input())
b = int(input())
c = int(input())

type_of_triangle(a, b, c)


