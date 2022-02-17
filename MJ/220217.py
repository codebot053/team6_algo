def solution(lottos, win_nums):
    cnt = 0
    zeros = 0
    for l in lottos:
        if l in win_nums:
            cnt += 1
        if l == 0:
            zeros += 1
    answer = [min(7-cnt-zeros, 6), min(7-cnt, 6)]
    return answer

lottos, win_nums = [44, 1, 0, 0, 31, 25],	[31, 10, 45, 1, 6, 19]

