def solution(my_string, letter):
    answer= "".join(a for a in my_string if a != letter )
    return answer