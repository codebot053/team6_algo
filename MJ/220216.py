from collections import Counter

def solution(id_list, report, k):
    # 결과값에 맞는 사이즈의 빈 리스트 생성
    answer = [0]*len(id_list)
    
    # 리포트 중복 제거
    re_list = list(set(report))
    
    # 나중에 사용할 키값저장
    key_dict = {}
    for idx, name in enumerate(id_list):
        key_dict[name] = idx
    
    # 누가 누굴 신고했는지에대한 리스트값 딕셔너리
    id_dict = {}
    # 딕셔너리에 키값저장
    for id in id_list:
        id_dict[id] = []
    
    # 신고당한 사람들 리스트
    reported_list = []
    # 밴리스트
    banned_list = []
    
    # 딕셔너리 밸류값 저장 및 신고 리스트 저장
    for re in re_list:
        reporter,reported = re.split()
        id_dict[reporter].append(reported)
        reported_list.append(reported)

    # 신고리스트를 카운트하여 밴리스트 생성
    cnt_re = dict(Counter(reported_list))
    for key, value in cnt_re.items():
        if value >= k:
            banned_list.append(key)

    # 밴리스트에 있으면 정답리스트에 값 추가
    for key, value in id_dict.items():
        for b in banned_list:
            if b in value:
                answer[key_dict[key]] += 1

    return answer


id1, re1 = ["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
id2, re2 = ["con", "ryan"],	["ryan con", "ryan con", "ryan con", "ryan con"]

k1, k2 = 2, 3

print(solution(id1, re1, k1))
print(solution(id2, re2, k2))


# re_list = list(set(re1))

# answer = [0] * len(id1)
# print(answer)

# key_dict = {}
# for idx, name in enumerate(id1):
#     key_dict[name] = idx

# print(key_dict)

# id_dict = {}
# reported_list = []
# banned_list = []

# for id in id1:
#     id_dict[id] = []

# print(id_dict)

# for re in re_list:
#     reporter,reported = re.split()
#     id_dict[reporter].append(reported)
#     reported_list.append(reported)

# cnt_re = dict(Counter(reported_list))
# for key, value in cnt_re.items():
#     if value >= k:
#         banned_list.append(key)

# print(id_dict)

# print(banned_list)

# for key, value in id_dict.items():
#     for b in banned_list:
#         if b in value:
#             answer[key_dict[key]] += 1

# print(answer)


