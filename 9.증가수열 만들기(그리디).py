import sys

# 1. 수열 길이 N과 수열 입력
n=int(input())
a=list(map(int, input().split()))

# 2. 양 끝 포인터와 상태 변수 초기화 
lt = 0
rt = n-1
last = 0        # 마지막으로 증가수열 에 추가한 값(초기값은 0)
res_str = ""    # 'L' 또는 'R' 을 기록할 문자열

# 3. 투 포인터 그리디 탐색
while lt <= rt:
    tmp =[] # 직전값 (last)보다 킅 숫자들을 임시로 모을 후보 바구니

    # 왼쪽 끝 숫자가 직전값보다 큰지 확인
    if a[lt]>last:
        tmp.append((a[lt], 'L'))

    # 오른쪽 끝 숫자가 직전 값보다 큰지 확인 (단, lt와 rt가 같은 칸일 때는 중복 방지)
    if lt < rt and a[rt] > last:
        tmp.append((a[rt],'R'))

    # 후보가 전혀 없다면 더 이상 증가수열을 만들 수 없으므로 종료
    if len(tmp) ==0:
        break
    # 숫자 크기를 기준으로 오름차순 정렬 (더 작은 값을 우선 선택)
    tmp.sort()

    # 가장 작은 값을 증가 수열의 가음 숫자로 선택
    chosen_val, chosen_dir = tmp[0]
    
    last = chosen_val
    res_str += chosen_dir

    # 선택된 방향에 맞추어 포인터 이동
    if chosen_dir =='L':
        lt += 1
    else:
        rt -= 1
# 4. 최대 증가수열 길이 및 선택 방향 문자열 출력
print(len(res_str))
print(res_str)