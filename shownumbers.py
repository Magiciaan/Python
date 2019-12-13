a = int(input('enter a no.'))
def limit(a):
        for i in range (a+1):
            if(i%2==0):
                print(i, 'Even')
            else:
                print(i, 'odd')
limit(a)