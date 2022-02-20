def solution(id_list, report, k):
    answer = []
    rep_dict ={}

    report = set(report)
    for i in id_list: # 유저수 만큼 리포트 요청 dict 초기화
        rep_dict[i] = []
        answer.append(0)
    for r_item in report:
        r_user=r_item.split()[0] # 신고한 유저
        b_user=r_item.split()[1] # 신고 받은 유저
        rep_dict[b_user].append(id_list.index(r_user))
    for r_log in rep_dict.values():
        if len(r_log) == k:
            for r_log_item in r_log:
                answer[r_log_item] += 1
    return answer