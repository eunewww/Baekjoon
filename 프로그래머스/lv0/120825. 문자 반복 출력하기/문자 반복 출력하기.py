def solution(my_string, n):
    answer = "".join(a*n for a in my_string)
    return answer