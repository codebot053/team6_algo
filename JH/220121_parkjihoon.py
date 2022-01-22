arr_1 = [1,3,5,5]
arr_2 = [True,True,True,False]

def solution(absolutes, signs): # 매개변수 (절댓값,boolean)
    answer = 0                  # 합을 담을 변수 초기화
    for index,num in enumerate(absolutes):
    # 내장함수를 이용해서 인덱스와 변수를 동시에 호출하는 루프
        if signs[index] == 1:
        # 인덱스 번호의 boolean이 참이면 양수
            answer += num
        else:
        # 참이 아닐경우 음수
            answer -= num
    return answer

result = solution(arr_1,arr_2)
print(result)
