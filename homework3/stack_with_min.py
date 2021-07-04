class stack :
    l = []
    size = 0
    min_el = float('inf')

    def push( self, a ):
        self.l.append( a )
        self.size += 1
        if( a < self.min_el ):
            self.min_el = a

    def pop( self ):
        el = self.min_el - 1
        if self.size > 0 :
            el = self.l[-2]
            del self.l[-1]
            self.size -=  1
        else:
            print("Stack is empty")
        if el == self.min_el:
            self.min_el = min( self.l )

    def top( self ):
        if self.size > 0:
            return self.l[-1]

    def empty( self ):
        return not bool(self.size)

    def getMin( self ):
        return self.min_el


if __name__ == '__main__' :
    s  = stack();
    s.push(10)
    s.push(10)
    s.push(1)
    s.push(0)
    s.push(10)
    print(s.getMin())
    print( s.top() )
    s.pop()
    print( s.top() )
    s.pop()

