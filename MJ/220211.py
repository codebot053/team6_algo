from collections import Counter

def solution(participant, completion):
    p = Counter(participant)
    c = Counter(completion)
    p.subtract(c)
    return p.most_common()[0][0]

# 다른 사람풀이
# def solution(participant, completion):
#     answer = ''
#     temp = 0
#     dic = {}
#     for part in participant:
#         dic[hash(part)] = part
#         temp += int(hash(part))
#     for com in completion:
#         temp -= hash(com)
#     answer = dic[temp]

#     return answer

print(solution(["leo", "kiki", "eden"],	["eden", "kiki"]))