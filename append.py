a = input('enter anything')
b = []
str(b.extend(a))
def g(b):
    c = input('enter anything or type quit')
    if (c!='quit'):
        b.extend(c)
        
    if (c=='quit'):
        print('You entered quit')
        exit()
    d = input('enter anything')
    if d in b:
        return(d ,' is in the list')
    else:
        return('it isnt in the list')
print(g(b))

