words=input().split()
d={}
for w in words:
    key="".join(sorted(w))
    d.setdefault(key,[]).append(w)
print(list(d.values()))