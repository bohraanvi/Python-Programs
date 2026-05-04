import math

print("1 Circle")
print("2 Rectangle")
print("3 Triangle")
print("4 Square")
print("5 Parallelogram")
print("6 Cube")
print("7 Cuboid")
print("8 Sphere")
print("9 Cylinder")
print("10 Cone")

ch = int(input("Enter choice: "))

match ch:
    case 1:
        r=float(input("Radius: "))
        print(math.pi*r*r)
    case 2:
        l=float(input())
        b=float(input())
        print(l*b)
    case 3:
        b=float(input())
        h=float(input())
        print(0.5*b*h)
    case 4:
        a=float(input())
        print(a*a)
    case 5:
        b=float(input())
        h=float(input())
        print(b*h)
    case 6:
        a=float(input())
        print(a**3)
    case 7:
        l=float(input())
        b=float(input())
        h=float(input())
        print(l*b*h)
    case 8:
        r=float(input())
        print(4/3*math.pi*r**3)
    case 9:
        r=float(input())
        h=float(input())
        print(math.pi*r*r*h)
    case 10:
        r=float(input())
        h=float(input())
        print(1/3*math.pi*r*r*h)