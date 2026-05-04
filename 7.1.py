p = input("Enter password: ")

c1 = len(p) >= 8
c2 = any(i.isupper() for i in p)
c3 = any(i.islower() for i in p)
c4 = any(i.isdigit() for i in p)
c5 = any(i in "!@#$%^&*" for i in p)

count = sum([c1,c2,c3,c4,c5])

if count<=2:
    print("Weak")
elif count<=4:
    print("Moderate")
else:
    print("Strong")