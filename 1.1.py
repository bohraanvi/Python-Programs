a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if b==0:
        return "Division by zero not allowed"
    return a/b

print("Addition:", add(a,b))
print("Subtraction:", sub(a,b))
print("Multiplication:", mul(a,b))
print("Division:", div(a,b))