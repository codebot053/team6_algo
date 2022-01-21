def solution(left, right):
    answer = 0
    for i in range(left, right + 1): #left 부터 right까지 1씩 증가하는 for문
        count = 0                    #약수의 개수를 담기 위한 변수
        for j in range(1, i + 1):    #1부터 i까지 증가하며 약수를 찾아냅니다.
            if i % j == 0:           #나누어 떨어지는 수는 약수
                count += 1           #약수라면 개수 증가
        if count % 2 == 0:           #개수가 홀수인지 짝수인지 판별
            answer += i              #짝수라면 +i
        else:
            answer -= i              #홀수라면 -i
    return answer

def solution(absolutes, signs):
    answer = 0
    for number, sign in zip(absolutes, signs): #number에 대한 합을 구할때 absolute, sign의 묶음을 위한 zip 함수
        if sign == True:                       #sign이 +/양수라면
            answer += number                   #number에 absolute를 더한다
        else:                                  #sign이 -/음수라면
            answer -= number                   #number에서 해당 absolute를 뺀다
    return answer