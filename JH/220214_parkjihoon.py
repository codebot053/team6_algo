s1 ="a"
s2 ="ababcdcdababcdcd"
s3 ="abcabcdede"
s4 ="abcabcabcabcdededededede"
s5 ="xababcdcdababcdcd"
def solution(s):
    answer_li = []
    temp = []
    cnt = 1
    answer = 1000
    if len(s) == 1:
        answer = len(s)
    for i in range(1,(len(s) //2)+1):
        for s_ in range(0,len(s),i):
            if s_+(i*2)-i < len(s):
                if s[s_:s_+i] == s[(s_+i):(s_+(i*2))]: #다음번째 문자열과 같을때
                    temp_s = s[s_:s_+i]
                    cnt +=1
                else:                                   #다음 문자열과 다를때
                    if cnt > 1:             #기존에 카운트가 1보다 클때
                        temp.append(str(cnt))
                        temp.append(temp_s)
                        cnt = 1
                    else:               #기존 카운트가 1보다 작거나 같을때
                        temp.append(s[s_:s_+i])
            else:
                if cnt>1:
                    temp.append(str(cnt))
                temp.append(s[s_:])
                cnt =1
        answer_li.append("".join(temp))
        temp = []
    for a_s in answer_li:
        if answer > len(a_s):
            answer = len(a_s)
    return answer

print(solution(s1))
print(solution(s2))
print(solution(s3))
print(solution(s4))
print(solution(s5))