#palindrome
def a(b):
    c=0
    d=len(b)-1
    while d>= c:
        if(b[c]!=b[d]):
            return False
        c = c + 1
        d = d -1
    return True
g = input('enter anything')
h = a(g)
if h == True:
    print()   #used to skip 1 line
    print('Palindrome')
else:
    print()
    print('Not Palindrome')
