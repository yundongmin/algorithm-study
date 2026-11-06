import sys 

# 1. 회의 개수 N 입력 받기
n=int(input())

# 2. 각 회의의 (시작 시간, 끝나는 시간) 입력 받기

meetings = []

for _ in range(n):
    start, end = map(int, input().split())
    meetings.append((start, end))

# 3. 끝나는 시간 (x[1]) 기준 오름차순 정렬, 끝나는 시간이 같다면 시작 시간 (x[0]) 기준 정렬
meetings.sort(key=lambda x: (x[1], x[0]))

# 4. 회의실 배정 시뮬레이션
cnt = 0         # 배정한 회의의 총 개수 
end_time = 0    # 직전 회의가 끝난 시각 (처음엔 0시)

for start, end in meetings:
    # 이번 회의이 시작 시간이 이전 회의 종료 시간 이후라면 배정 가능
    if start >= end_time:
        cnt += 1        # 회의 배정
        end_time = end  # 회의실이 비는 시각을 이번 회의의 종료 시간으로 갱신

# 5. 최대 진행 가능한 회의 수 출력
print(cnt)