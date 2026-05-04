import sys

a=25
b=3.14
c=3+4j
d=True
e="Python Programming"

print(a,type(a),sys.getsizeof(a))
print(b,type(b),sys.getsizeof(b))
print(c,type(c),sys.getsizeof(c))
print(d,type(d),sys.getsizeof(d))
print(e,type(e),sys.getsizeof(e))

print(c.real)
print(c.imag)
print(abs(c))

x=True
y=False
print(x and y)
print(x or y)
print(not x)

i=10
print(float(i))
print(int(3.5))
print(str(i))
print(int("20"))
print(int(True))
print(complex(i))