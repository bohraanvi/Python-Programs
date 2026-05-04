print("ENTER A LIST")
nums=list(map(int,input().split()))
target=int(input())
d={}
for i in range(len(nums)):
    if target-nums[i] in d:
        print(d[target-nums[i]],i)
    d[nums[i]]=i