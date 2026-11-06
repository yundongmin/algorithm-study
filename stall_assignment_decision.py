import sys 

# 1. 입력 받기 및 마구간 좌표 오름차순 정렬
# n: 마구간 개수 (예:5)
# c: 배치할 말의 마릿수 (예:3)

n,c=map(int,input().split())
coords = [int(input()) for _ in range(n)]

# 수직선 상에서 거리를 계산하기 위해 좌표를 오름차순으로 정렬합니다.
coords.sort()

# 2. 결정 함수 (Count 함수) 정의
# 두 말 상이의 거리를 최소 min_dist 이상으로 띄웠을 때,
# 최대 몇 마리의 말을 마구간에 배치할 수 있는지 세어 반환합니다.

def count_horses(min_dist):
    cnt =1                  # 첫 번째 말은 무조건 맨 첫 번째 마구간(coords[0])에 넣음
    last_pos = coords[0]    #  가장 최근에 말을 배치한 무구간의 좌표

    # 두 번째 마구간부터 끝까지 확인
    for i in range(1, n):
        # 직전 말과의 거리가 기준 거리(min_dist) 이상 확보되었는가?
        if coords[i] - last_pos >= min_dist:
            cnt += 1                # 말을 추가로 배치
            last_pos = coords[i]    # 가장 최근에 말을 놓은 위치 갱신
            
    return cnt

# 3. 이분탐색(결정 알고리즘) 범위 설정
# lt: 말 사이의 최소 간격(최소1)
# rt: 말 사이의 최대 간격 (가장 먼 마구간과 첫 마구간의 거리 차이)

lt = 1
rt = coords[-1]-coords[0]
answer = 0

# 4. 이분 탐색
while lt <= rt:
    mid = (lt+rt) //2 #이번에 시험해 볼 말 사이의 최소 간격

    # mid 간격 이상을 유지하면서 C마리 이상 배치할 수 있는가?
    if count_horses(mid) >=c:
        answer = mid # 배치가 가능하므로 일단 정답 후보로 저장
        lt = mid+1  # 간격을 더 넓힐 수 있는지 확인하기 위해 오른쪾 탐색
    else:
        rt = mid-1 # C 마리를 다 채우지 못했으므로 간격을 좁히기 위해 왼쪽 탐색