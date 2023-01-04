def solution(price):
    p = [100000,300000,500000]
    r = [1, 0.95, 0.90, 0.80]
    answer = int(price * r[sum(price >= i for i in p)])
    return answer