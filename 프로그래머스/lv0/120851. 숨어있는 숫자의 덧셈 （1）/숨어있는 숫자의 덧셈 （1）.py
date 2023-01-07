def solution(my_string):
    answer = 0
    for x in list(my_string):
        try: answer += int(x)  
        except: ValueError
    return answer
  