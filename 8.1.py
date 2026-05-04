a=int(input("Side a: "))
b=int(input("Side b: "))
c=int(input("Side c: "))

if a+b>c and a+c>b and b+c>a:
    print("Valid Triangle")
    if a==b==c:
        print("Equilateral")
    elif a==b or b==c or a==c:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Not a valid triangle")