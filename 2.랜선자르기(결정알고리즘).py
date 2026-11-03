import sys

# 1. 랜선 개수 k와 필요한 랜선 개수 N 입력 받기
# lines : k개의 기존 랜선 길이들을 담은 리스트

k, n = map(int, input().split())
lines = [int(input()) for _ in range(k)]

# 2. 결정 함수 (Count 함수) 정의
# 길이 len_unit으로 잘랐을 때 총 몇개의 랜선이 나오는지 계산

def count_lan(len_unit):
    cnt = 0
    for x in lines:
        cnt += (x// len_unit) # 각 랜선에서 나오는 토막 수 누적
    return cnt

# 3. 이분 탐색 (결정 알고리즘) 범위 설정
# 자를 수 있는 최소 길이는 1cm
# 자를 수 있는 최대 길이는 가지고 있는 랜선 중 최갯값
lt = 1
rt = max(lines)
answer = 0 # 조건을 만족하는 최대 길이를 저장할 변수

# 4. 이분 탐색 수행

while lt <= rt:
    mid = (lt+rt) // 2 # 이번에 시도해 볼 랜선의 길이 

    # mid 길이로 잘랐을 때 N개이상을 만들 수 있는가?
    if count_lan(mid) >= n:
        answer = mid # 일단 N개 이상 만들 수있으므로 정답 후보로 저장
        lt = mid + 1 # 더 긴 길이로도 가능한지 확인하기 위해 오른쪽 탐색
    else: 
        rt = mid - 1 # N개를 채우지 못했으므로 길이를 줄이기 위해 왼쪽 탐색

# 5. N개를 만들 수있는 최대 길이 출력\
print(answer)


def Count(len):
    cnt=0
    for x in Line:
        cnt+=(x//len)  # : 만들어 낼수있는 작은 토막의 개수 802 // 182 때의 몫의 개수
    return cnt

k, n = map(int, input().split())
Line = []
res=0
lt=1
rt=largest=0

for i in range(k):
    tmp=int(input())
    Line.append(tmp)
    largest=max(largest, tmp)

lt = 1
rt = largest

while lt <=rt:
    mid=(lt+rt) //2 # mid가 한개의 랜선의 길이

    if Count(mid)>=n:
        res=mid
        lt=mid+1
    else:
        rt=mid-1