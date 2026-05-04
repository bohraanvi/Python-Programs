nums=list(map(int,input().split()))
k=int(input())
from collections import Counter
print([i[0] for i in Counter(nums).most_common(k)])