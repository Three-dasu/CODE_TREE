import heapq as hf
"""
주어진 수열을 앞부터 읽으면서 홀수 번째 원소 읽을 때, 지금까지 수들 중 중앙값 출력

길이가 항상 홀수라 정말 딱 가운데 인덱스 구하면 됨 (//2 + 1)
그냥 힙큐에 하나씩 넣으면서 하면 될 듯 이게 왜 하드야
분명 뭔가 있다

근데 힙큐는 엄밀히 말하면 오름차순 정렬이 아니잖아아아아
1 3 2 일 수도 있는데, 역시 하드 문제 ㄷㄷ
오름차순의 인덱스 중앙 말고 중앙값을 구하는 다른 비법소스가 있나

이거도 다 해놓고 하나씩 빼면서 계산하고 마지막에 역순으로 출력 하는가봄
아닌데, 순서대로 빼야 하는데
그럼 리스트 역순으로 읽으면서 값 찾아서 삭제를 해야 하나?
값을 찾아서 빼는거면 이건 오히려 treeset 문제 아니야?

최소힙 하나 최대힙 하나 총 두개를 쓰면 된다네요~~
"""
T = int(input())
for _ in range(T):
    m = int(input())
    lst = list(map(int, input().split()))
    hq_mn = []  # 음수로 최대힙
    hq_mx = []  # 양수로 최소힙

    for i, n in enumerate(lst):
        # 처음이면 일단 mn에
        if not hq_mn:
            hf.heappush(hq_mn, -n)
            print(n, end=' ')
            continue
        
        curr = -hq_mn[0]
        curr2 = hq_mx[0] if hq_mx else 2**31

        # 현 중앙값보다 작음 -> mn에 넣기
        if n < curr:
            # print("현 중앙값보다 작음 -> mn에 넣기")
            if len(hq_mn) > len(hq_mx):     # mn이 길면
                hf.heappop(hq_mn)           # 현재 중앙값 뽑고
                hf.heappush(hq_mx, curr)    # mx에 현재 중앙값 추가
            hf.heappush(hq_mn, -n)          # mn에 n 추가
        
        # 현 중앙값이상 mx 최소값 이하 -> 길이 기준 삽입
        elif curr <= n <= curr2:
            # print("현 중앙값이상 mx 최소값 이하 -> 길이 기준 삽입")
            if len(hq_mn) == len(hq_mx):    # mn mx 길이가 같으면
                hf.heappush(hq_mn, -n)      # mn에 추가
            else:
                hf.heappush(hq_mx, n)       # mn이 길면 mx에 추가
        
        # mx 최소보다 큼 -> mx에 넣긴 해야함
        else:
            # print("mx 최소보다 큼 -> mx에 넣긴 해야함")
            if len(hq_mn) == len(hq_mx):        # mn mx 길이가 같으면
                n_from_mx = hf.heappop(hq_mx)   # mx의 최소를
                hf.heappush(hq_mn, -n_from_mx)  # mn에 추가
            hf.heappush(hq_mx, n)               # 새로운 값은 mx에
            
        if len(hq_mn) == len(hq_mx) + 1:
            print(-hq_mn[0], end=' ')

        # print(hq_mn, hq_mx)
    print()
        
