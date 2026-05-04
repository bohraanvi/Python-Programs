n=int(input("Enter length of series"))
def fib(n):
    a,b=0,1
    while a<=n:
        yield a
        a,b=b,a+b

for i in fib(n):
    print(i)