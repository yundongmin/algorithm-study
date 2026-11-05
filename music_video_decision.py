import sys

# 1. 노래 개수 N과 목표 DBD 장수 M, 그리고 곡 길이 리스트 입력

n,m = map(int, input().split())
songs= list(map(int,input().split()))

# 2. 결정 함수: DVD 용량이 capacity 일때 필요한 총 장수 계산
# DVD 1장의 용량이 capacity 일때, 필요한 총 DVD 장수를 반환합니다.

def count_dvd(capacity):
    cnt = 1         # 첫 번째 DVD를 준비하고 시작
    current_sum = 0 # 현재 DVD에 담긴 곡들의 총 재생 시간
    for song in songs:
        if current_sum + song > capacity:
            cnt += 1
            current_sum = song
        else:
            current_sum += song
    return cnt

# 3. 이분 탐색 범위 설정
lt = max(songs)
rt = sum(songs)
answer = 0

# 4. 이분 탐색 수행
while lt <= rt:
    mid = (lt+rt) // 2
    if count_dvd(mid) <= m:
        answer = mid
        rt = mid-1
    else:
        lt = mid + 1

# 5. r
print(answer)