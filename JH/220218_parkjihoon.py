def solution(s):
    answer_li = []
    s_list = list(s)
    nums = ['zero','one','two','three','four','five',
              'six','seven','eight','nine']
    n_hash = []
    s_sum = 0
    for i_n,num in enumerate(nums): # 문자의 해시값을 저장한 리스트 생성
        n_li = list(num)
        n_hash_sum =0
        for n_chr in n_li:
            hash_val = hash(n_chr)
            n_hash_sum += hash_val
        n_hash.append(n_hash_sum)
    for i_s in s_list:
        try:
            test = int(i_s)
            answer_li.append(i_s)
        except ValueError:
            s_hash = hash(i_s)
            s_sum += s_hash
        if s_sum in n_hash:
            answer_li.append(str(n_hash.index(s_sum)))
            s_sum = 0
    a_sum = ''
    for i_a in answer_li:
        a_sum += i_a
    answer = int(a_sum)

    return answer