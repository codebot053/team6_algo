array,commands = [1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]

def solution(array, commands):
    answer = []
    for com in commands:
        temp_array = array[com[0]-1:com[1]]
        temp_array.sort()
        temp_int = temp_array[com[2]-1]
        answer.append(temp_int)
    return answer

print(solution(array,commands))