s = input("Enter a string")
print(sum(1 for i in s if i in "aeiouAEIOU"))