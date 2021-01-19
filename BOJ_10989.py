"""
수 정렬하기3
"""
import sys
n = int(sys.stdin.readline())
array = []
for _ in range(n):
    array.append(int(sys.stdin.readline()))
# 선택 정렬
for i in range(len(array)):
    min_index = i
    for j in range(i+1,len(array)):
        if array[min_index]>array[j]:
            min_index = j
    array[i],array[min_index]=array[min_index],array[i]

for ans1 in array:
    print(ans1)

# 삽입 정렬
for i in range(1,len(array)):
  for j in range(i,0,-1):
    if array[j]<array[j-1]:
      array[j],array[j-1]=array[j-1],array[j]
    else:
      break

for ans2 in array:
  print(ans2)

# 퀵 정렬
def quick_sort(array,start,end):
  if start>=end:
    return
  pivot = start
  left = start + 1
  right = end
  while left<=right:
    while left<=end and array[left]<=array[pivot]:
      left+=1
    while right>start and array[right]>=array[pivot]:
      right-=1
    if left>right:
      array[right],array[pivot]=array[pivot],array[right]
    else:
      array[left],array[right]=array[right],array[left]
  quick_sort(array,start,right-1)
  quick_sort(array,right+1,end)

quick_sort(array,0,len(array)-1)
for ans3 in array:
  print(ans3) 

# 계수 정렬
count = [0]*(max(array)+1)
for i in range(len(array)):
  count[array[i]]+=1
for i in range(len(count)):
  for j in range(count[i]):
    print(i,end='\n')

# 파이썬 정렬 라이브러리
result=sorted(array)
for ans4 in array:
  print(ans4)