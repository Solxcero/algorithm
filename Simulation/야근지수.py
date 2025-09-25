from collections import Counter

def solution(n, works):
    if sum(works) <= n:
        return 0

    cnt = Counter(works)
    heights = sorted(cnt, reverse=True)  # 서로 다른 작업량 내림차순
    i = 0

    while n > 0 and i < len(heights):
        h = heights[i] 
        c = cnt[h]
        nh = heights[i+1] if i+1 < len(heights) else 0
        need = (h - nh) * c  # h를 nh까지 일괄 내리는 데 필요한 시간

        if n >= need:
            # c개 전부 nh까지 내린다
            cnt[h] -= c
            cnt[nh] += c
            print(cnt)
            n -= need
            i += 1
        else:
            # nh까지는 못 가므로 q, r로 균등 분배
            q, r = divmod(n, c)
            newh = h - q
            cnt[h] -= c
            cnt[newh] += c - r
            cnt[newh - 1] += r
            print(cnt)
            n = 0

    # 제곱합 계산
    ans = 0
    for h, c in cnt.items():
        if h > 0 and c > 0:
            ans += (h*h) * c
    return ans

works = [4, 3, 3]
n = 4
print(solution(n, works))