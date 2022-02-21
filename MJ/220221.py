import itertools

n1 = '17'
n2 = '011'

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def solution(numbers):
    p_list = []
    int_list = []
    cnt = 0

    for i in range(1,len(numbers)+1):
        for p in set(itertools.permutations(list(numbers), i)):
            p_list.append(p)

    for p in p_list:
        a = ''.join(p)
        int_list.append(int(a))

    int_list = set(int_list)

    for i in int_list:
        if is_prime(i):
            cnt += 1

    return cnt

print(solution('17'))
print(solution('011'))


numbers = '011'


# p_list = []
# int_list = []
# cnt = 0

# for i in range(1,len(numbers)+1):
#     for p in set(itertools.permutations(list(numbers), i)):
#         p_list.append(p)

# for p in p_list:
#     a = ''.join(p)
#     int_list.append(int(a))

# str_list = set(int_list)

# for i in int_list:
#     if is_prime(i):
#         cnt += 1

