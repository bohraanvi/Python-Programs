lst = input("Enter elements: ").split()
n = len(lst)

for i in range(1<<n):
    subset=[]
    for j in range(n):
        if i&(1<<j):
            subset.append(lst[j])
    print(subset)