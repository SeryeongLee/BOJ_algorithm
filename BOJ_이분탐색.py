# 1920 수 찾기

# 입력받기
n = int(input())
array=list(map(int,input().split()))
# 이진탐색은 정렬돼야 함
array.sort()
m = int(input())
check=list(map(int,input().split()))

# 이진탐색
def binary_search(array,target,start,end):
    while start<=end:
        mid=(start+end)/2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid]==target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작을 때
        elif array[mid]>target:
            end = mid-1
        else:
            start=mid+1
    return None

# 손님이 부품 확인
for i in check:
    # 해당 부품이 존재하는지 확인
    answer = binary_search(array,i,0,n-1)
    if result != None:
        print('1',end='')
    else:
        print('0',end='')

# 1654 랜선 자르기

# 입력받기
import sys
k,n = list(map(int,input().split(' ')))
array = [int(sys.stdin.readline()) for _ in range(k)]

# 이진탐색 위한 시작점, 끝점 설정
start = 0
end = max(array)

# 이진 탐색 수행(반복적)
result=0
while start<=end:
    mid=(start+end)/2
    count=0 # 랜선 수 초기값 설정
    for i in array:
        count+=i//mid # 나눈 랜선 수
    # 랜선 수가 부족한 경우 더 많이 자르기(왼쪽 부분 탐색)
    if count < n:
        end=mid-1
    # 랜선 수가 충분한 경우 덜 자르기(오른쪽 부분 탐색)
    else:
        result=mid
        start=mid+1
print(result)

# 2805 나무 자르기
n, m = list(map(int, input().split()))
array = list(map(int, input().split()))

# 이진탐색을 위한 시작점, 끝점 설정
start = 0
end = max(array)

# 이진 탐색
result=0
while start<=end:
    mid=(start+end)/2
    total=0
    for i in array:
        if i>mid:
            total += i - mid
    if total<m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
print(result)
