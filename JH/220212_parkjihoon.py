def solution(participant, completion):
    answer = ''
    participant.sort() # 파라미터로 받는 리스트 내부의 문자열을
    completion.sort()  # 알파벳 순으로 정렬
    for i in range(len(completion)):
        # 완주하지 못한 선수 리스트 속의 인자 숫자 만큼 반복
        if participant[i] != completion[i]:
            # 서로 같은 인덱스의 인자를 비교해서 다르면 참가자 리스트의
            # 해당인자를 출력
            answer = participant[i]
            return answer
        # 반복문이 끝나도 없는경우는 참가자 리스트의
        # 마지막 인자를 출력
    answer = participant[-1]
    return answer