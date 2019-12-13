a = input('enter anything')
def reverse(a):
    b = reverse(a)
    if(b==a):
        return 'true'
    else:
        return 'false'
reverse(a)