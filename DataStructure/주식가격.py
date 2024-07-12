def solution(prices):
    answer = []
    for i in range(len(prices)):
        tmp = 0
        for j in range(i+1,len(prices)):
            if prices[i] <= prices[j]:
                tmp+=1
            else:
                tmp += 1
                break  # 효율성 테스트 통과하려면 break. 문 있어야 함
        answer.append(tmp)
        
    return answer