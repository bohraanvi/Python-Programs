s=input("ENTER A STRING")
res=""
for i in range(len(s)):
    temp=""
    for j in range(i,len(s)):
        if s[j] in temp:
            break
        temp+=s[j]
    if len(temp)>len(res):
        res=temp
print(len(res))