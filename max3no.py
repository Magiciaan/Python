a = int(input('enter a no.'))
b = int(input('enter a no.'))
c = int(input('enter a no.'))
def d(a,b,c):
    if(a>b and a>c):
        print(a, 'is greater')
    elif(b>a and b>c):
        print(b,'is greater')
    elif(c>a and c>b):
        print(c, 'is greater')
    else:
        print('no. are similar')
d(a,b,c)