a = set(map(int,input("Enter set 1: ").split()))
b = set(map(int,input("Enter set 2: ").split()))

def union(a,b):
    return a|b

def intersection(a,b):
    return a&b

def difference(a,b):
    return a-b

def sym_diff(a,b):
    return a^b

print("Union:", union(a,b))
print("Intersection:", intersection(a,b))
print("Difference:", difference(a,b))
print("Symmetric Difference:", sym_diff(a,b))

print("Subset:", a.issubset(b))
print("Superset:", a.issuperset(b))

x = int(input("Enter element to check: "))
print("Exists:", x in a)

print("Size of set:", len(a))

lst = list(map(int,input("Enter list: ").split()))
print("Converted set:", set(lst))

def powerset(s):
    s=list(s)
    n=len(s)
    for i in range(1<<n):
        subset=[s[j] for j in range(n) if i&(1<<j)]
        print(subset)

print("Power set:")
powerset(a)