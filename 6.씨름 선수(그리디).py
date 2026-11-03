import sys

# 1. 지원자 수 N 입력 받기 
n= int(input())

# 2. 각 지원자의 (키, 몸무게) 정보 입력
applicants = []
for _ in range(n):
    height, weight = map(int, input().split())
    applicants.append((height, weight))

# 3. 키를 기준으로 내림차순(큰 순서대로) 정렬
# reverse=True를 주면 숫자부터 정렬됩니다.
applicants.sort(key=lambda x: x[0], reverse=True)

# 4. 그리디 판별
cnt = 0
max_weight = 0

for height, weight in applicants:
    # 나보다 키가 컸던 앞사람들의 최고 몸무게보다 내가 더 무겁다면 몸무게
    if weight > max_weight:
        cnt += 1                # 합격
        max_weight = weight     # 최고 몸무게 기록 갱신

# 5. 선발된 인원 출력
print(cnt)