a = input('enter anything')
b = ''
c = len(a)
def d(a,b,c):
    while c > 0:
        b = b + a[c - 1]
        c = c - 1
    if (b == a):
        print('palindrome')
    else:
        print('not palindrome')
d(a,b,c)