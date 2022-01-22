arr_1 = [[1,3],[5,5],[2,7]]
arr_2 = [[1,3],[4,1],[10,12]]

def sol(arr1, arr2):

    answer = arr1                           # 합을 담을 list matrix 사이즈를 매개 변수로 받는 list matrix중 하나로 초기화

    for i in range(len(arr1)):              # list 를 index 0부터 끝까지 반복
        for i2 in range(len(arr1[i])):      # list i번째 index 인자(리스트)의 내부 index 숫자 만큼 반복
            sum0 = arr1[i][i2] + arr2[i][i2]# arr1 인자와 arr2 인자의 합
            answer[i][i2] = sum0            # 위의 두 인자 합을 answer list 의 해당 위치에 할당
    return answer                           # answer matrix 반환
result = sol(arr_1,arr_2)

print(result)
