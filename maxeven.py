a = int(input('enter a no.'))
b = int(input('enter a no.'))
c = int(input('enter a no.'))
def d(a,b,c):
    if(a>b and a>c):
        print (a, 'is greatest')
    elif (b > a and b > c):
            print(b, 'is greatest')
    elif (c>a and c>b):
            print(c, 'is greatest')
    else:
        print('some numbers are equal')
def e(a,b,c):
    if(a%2==0):
        print(a, 'is even')
    else:
        print(a,'is odd')
    if (b % 2 == 0):
        print(b, 'is even')
    else:
        print(b,'is odd')
    if (c % 2 == 0):
        print(c, 'is even')
    else:
        print (c,'is odd')
d(a,b,c)
e(a,b,c)
