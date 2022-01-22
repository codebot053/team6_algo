
def solution(left, right):
    sum = 0
    for num in range(left,right+1):
        divisor = []
        for num2 in range(1,num+1): #1부터 n 까지 나눠보며 나머지 0 을 리스트 저장.
            if num % num2 == 0:
                divisor.append(num2)
        num_of_divisor = len(divisor)
        if num_of_divisor % 2 == 0:
            sum += num
        else:
            sum -= num
    answer = sum
    return answer

result_1 = solution(13,17)
result_2 = solution(24,27)

print(result_1,result_2)

