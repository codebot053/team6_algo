def solution(array, commands):

    answer = []

    # commands에 있는 command(i, j, k)를 추출한다.

    for command in commands:

        i, j, k = command[0], command[1], command[2]

        slice = array[i-1:j] # array에서 slice 실행

        slice.sort() # 실행한 slice를 sort를 통해 list 정렬

        answer.append(slice[k-1]) # k번째에 있는 수를 indexing 한다

    return answer



