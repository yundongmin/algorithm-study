import sys

# 1. 창고 가로 길이 L과 각 열의 상자 높이 리스트 입력
L = int(input())
boxes = list(map(int, input().split()))

# 2.높이 조정 횟수 M 입력
M = int(input())

# 3. 매 턴 마다 정렬 후 최고 높이에서 최저 높이로 상자 1개 이동 (M번 반복)
for _ in range(M):
    boxes.sort()        # 오름차순 정렬 : 맨 앞(0번)이 최저, 맨 뒤(-1번)가 최고
    boxes[-1] -= 1      # 가장 높은 곳에서 상자 하나 꺼냄
    boxes[0] += 1       # 가장 낮은 곳에 상자 하나 얹음

# 4. M번의 조정이 모두 끝난 후 마지막 정렬 수행
boxes.sort()

# 5. 가장 높은 곳과 가장 낮은 곳의 차이 출력
print(boxes[-1] - boxes[0])
