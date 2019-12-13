a = int(input('enter a no.'))
b = 0
def limit(a,b):
    for i in range(1,a+1):
        if(i%3==0 or i%5==0):
            b = b + i
    print(b)
limit(a,b)
