class stack :
    l = []
    size = 0

    def push( self, a ):
        self.l.append( a )
        self.size += 1

    def pop( self ):
        if self.size > 0 :
            self.l.remove(self.l[-1])
            self.size -=  1
        else:
            print("Stack is empty")

    def top( self ):
        if self.size > 0:
            return self.l[-1]

    def empty( self ):
        return not bool(self.size)


if __name__ == '__main__' :
    s  = stack();
    s.push('a')
    s.push(10)
    print( s.top() )
    s.pop()
    print( s.top() )
    s.pop()

