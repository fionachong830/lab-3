x=int(input('input a number'))
isprime=False
if x%2==0:
    if x==2:
        print(x,'is a prime number')
        isprime=True
else:
    if x%3==0:
        if x==3:
            print(x,'is a prime number')
            isprime=True
    else:
        if x%round(math.sqrt(x))!=0:
            print(x,'is a prime number')
            isprime=True
if isprime==False:
    print(x,'is not a prime number')
