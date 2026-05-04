print("Enter a list")
t = tuple(map(int, input().split()))
print(sum(1 for i in t if i % 2 == 0))