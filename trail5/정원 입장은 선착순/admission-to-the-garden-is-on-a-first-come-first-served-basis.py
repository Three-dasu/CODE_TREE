N = int(input())
a, t = [], []
for _ in range(N):
    ai, ti = map(int, input().split())
    a.append(ai)
    t.append(ti)

import heapq as hf
"""
a에 도착해서 t동안 머무르는 N명의 사람들
누가 있다면 기다리자
여러명 대기중이면 번호순으로 입장
누가 제일 오래 기다리나

일단 a 기준으로 정렬은 해야하지 않나
시뮬레이션 하면서 먼가 대기할 일이 생기면 대기열 hq에 추가 (i, ai, ti)
이렇게 하면 시간 단위로 체크해야 하는데 그럼 10억번 봐야함

얘도 큐를 두개 쓰면 되겠구나

hq_a = 도착 순서, 도착 시간 우선순위용 (ai, ti, i)
hq_i = 대기열, 번호 우선순위용 (i, ai, ti)

1. hq_i가 있으면 거기서 pop, 없으면 hq_a에서 pop
    - 현재 시간 st에 t 더해서 예상 종료 시간 et 설정

2. 대기열(hq_i)가 있는지 확인
    - 없다면 다음 도착할 사람을 hq_a[0]로 확인 3번으로 진행
    - 있으면 a가 et 이하인 사람들 모두 대기열에 추가 (3-2와 동일)

3-1. aj >= et
    - hq_i가 비었으면 바로 입장. 다음 루프로

3-2. aj < et
    - pop하고 대기열 hq_i에 (i, ai, ti) 추가
    - 다음 사람도 보면서 (먼저 확인부터) a <= et까지 hq_i에 추가

    - 다음 루프로, 다음 루프 가기 전에 현재 시간 st를 et값으로 업데이트

4. 루프 하나 끝. 다음 루프로
"""

hq_a = []
hq_i = []

for i in range(N):
    hf.heappush(hq_a, (a[i], i, t[i]))
    # hf.heappush(hq_i, (i, a[i], t[i]))

wait = [0]*N

st = 0
while True:
    # print()
    # for ii, aa, tt in hq_i:
    #     print(ii+1, end=' ')
    # print('are waiting now')
    # print(wait)

    # 1. hq_i가 있으면 거기서 pop, 없으면 hq_a에서 pop
    #     - 현재 시간 st에 t 더해서 예상 종료 시간 et 설정
    
    if hq_i:
        ci, ca, ct = hf.heappop(hq_i)
        wait[ci] += st - ca
        # print(ci+1, 'pop from wait list')
        
        
    else:
        ca, ci, ct = hf.heappop(hq_a)
        # print(ci+1, 'pop from arrive list')
        # w.remove(ci)  # hq_a에서 뽑아낸 거면 대기 리스트에 없을테니

    gap = 0
    if st < ca: # 현재 시간(이전 루프의 종료 시간)이 이번사람 도착 시간보다 이르면 이 사람은 대기 안한거
        gap = ca-st
        # print('start at', st, 'but arrived at', ca, 'and the gap is', gap)
    
    et = st + gap + ct

    # print(ci+1, 'waited for', wait[ci], 'hours')
    # print(ci+1, 'entered at', st+gap, 'exit at', et)


    
    if not hq_i:
        if hq_a:
            na, nt, ni = hq_a[0]
            # 3-1 상황
            if na >= et:
                na, ni, nt = hf.heappop(hq_a)
                hf.heappush(hq_i, (ni, na, nt))
                # 여긴 대기자가 없는 상황, 굳이 이걸 할 필요가 없음. 주석처리
                # wait[ni] += et-na   # 도착 시간과 현재 종료 예상 시간으로 초기 대기시간 업데이트
                st = et
                continue
        else:               # 둘 다 빈 상황
            break
    

    while True:
        if not hq_a or hq_a[0][0] > et:
            break

        na, ni, nt = hf.heappop(hq_a)
        hf.heappush(hq_i, (ni, na, nt))
        if na >= et:
            break
        # 여기서도 하면 안되나...?? 되나...?
        # wait[ni] += et-na   # 도착 시간과 현재 종료 예상 시간으로 초기 대기시간 업데이트
            
    st = et

print(max(wait))