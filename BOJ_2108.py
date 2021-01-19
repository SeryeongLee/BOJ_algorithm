"""
통계학
"""
import sys
from collections import Counter

# 입력받기
n = int(sys.stdin.readline())
numbers = []
for _ in range(n):
    numbers.append(int(sys.stdin.readline()))

# 1. mean
def mean(a):
    return round(sum(a)/len(a))

# 2. median
def median(a):
    a.sort()
    mid = a[len(a)//2]
    return mid

# 3. mode
def mode(a):
    c = Counter(a)
    order = c.most_common()
    maximum = order[0][1]

    mode = []
    for num in order:
        if num[1]==maximum:
            mode.append(num[0])
    return mode[1]


# 4. range
def ranges(a):
    return max(a)-min(a)

print(mean(numbers))
print(median(numbers))
print(mode(numbers))
print(ranges(numbers))
