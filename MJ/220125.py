def solution(participant, completion):
    for c in completion:
        participant.remove(c)
    return participant[0]