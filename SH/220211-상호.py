def solution(participant, completion):
    answer = ''
    dict = {}
    for i in participant:
        dict[i] = dict.get(i, 0) + 1
    for i in completion:
        dict[i] = dict.get(i, 0) - 1

    for key, value in dict.items():
        if value != 0:
            answer = ''.join(key)
    return answer