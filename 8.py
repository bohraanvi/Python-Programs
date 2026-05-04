print("Enter a list")
lst = list(map(int, input().split()))
new=[]
for i in lst:
    if i not in new:
        new.append(i)
print(new)