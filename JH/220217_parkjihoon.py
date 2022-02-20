def solution(lottos, win_nums):
    cnt_c = 0  # 맞춘 번호 저장
    cnt_z = 0
    answer = []
    for m_num in lottos:
        if m_num in win_nums:
            cnt_c += 1
        elif m_num == 0:
            cnt_z += 1
    h_score = 7 - (cnt_c + cnt_z)
    l_score = 7 - cnt_c
    if l_score == 7:
        l_score = 6
    if h_score == 7:
        h_score = 6

    answer.append(h_score)
    answer.append(l_score)
    return answer