

def f(a):
    d=''
    length=len(a)
    while length>0:
        #print(a[length-1])
        d = d + a[length - 1]
        length=length-1
    print (d)

print('start')
c='shyam'
f(c)
print('over')