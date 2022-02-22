import itertools
from math import floor


def prime(n):
    if n<=1:
        return False
    else:
        for p in range(2,floor((n**0.5)+1)):
            if n % p == 0:
                return False
        return True
def solution(numbers):
    num_list = []
    numbers = list(numbers)
    cnt = 0

    for i in range(1,len(numbers)+1):
        temp = list(set(itertools.permutations(numbers,i)))
        for t in temp:
            temp_item = int(''.join(t))
            if temp_item in num_list:
                continue;
            else:
                num_list.append(temp_item)
    for n in num_list: #리스트 내부 수 루프
        if prime(n):
            print(n)
            cnt +=1

    return cnt