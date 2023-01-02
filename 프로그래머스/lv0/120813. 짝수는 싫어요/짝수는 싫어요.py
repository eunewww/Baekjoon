def solution(n):
    answer = [2*i+1 for i in range(n//2 + n%2)]
    return answer
