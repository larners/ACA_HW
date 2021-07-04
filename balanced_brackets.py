import stack

def balanced_brackets( exp ):
    s = stack.stack()
    result = True
    for _, symbol in enumerate( exp ):
        if '{' == symbol or '(' == symbol or '[' == symbol or '<' == symbol:
            s.push( symbol )
        elif '}' == symbol and '{' == s.top():
            s.pop()
        elif ')' == symbol and '(' == s.top():
            s.pop()
        elif ']' == symbol and '[' == s.top():
            s.pop()
        elif '>' == symbol and '<' == s.top():
            s.pop()
        elif '}' == symbol or ')' == symbol or ']' == symbol or '>' == symbol:
            result = False
            break

    if not s.empty():
        result = False

    return result

def balanced_brackets_alternative( exp ):
    OPEN = ( '{', '(', '[', '<' )
    CLOSE = ( '}', ')', ']', '>' )

    s = stack.stack()
    result = True
    for _, symbol in enumerate( exp ):
        if symbol in OPEN:
            s.push( symbol )
        if symbol in CLOSE:
            pos = CLOSE.index( symbol )
            if s.top() == OPEN[pos]:
                s.pop()
            else:
                result = False
                break

    if not s.empty():
        result = False

    return result

# balanced_brackets vs balanced_brackets_alternative ????

if __name__ == '__main__':
    print( balanced_brackets("[()]{}{[()()]()}" ))
    print(balanced_brackets( "int main() {\n\tfor (int i = 0; i  10; ++i) {\n\t\t//some code\n\t}\n}\n}" ) )
    
    print( balanced_brackets_1("[()]{}{[()()]()}" ))
    print(balanced_brackets_1( "int main() {\n\tfor (int i = 0; i  10; ++i) {\n\t\t//some code\n\t}\n}\n}" ) )


