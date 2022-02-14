s1 = "aabbaccc"	
s2 = "ababcdcdababcdcd"	
s3 = "abcabcdede"	
s4 = "abcabcabcabcdededededede"	
s5 = "xababcdcdababcdcd"	
s6 = "aaaaaaaaaaaabcd"


def solution(s):
    count = len(s)
    
    for i in range(1,(len(s)//2)+1):
        temp_list = [s[i*j:i*j+i] for j in range(len(s))]
        temp_list = list(filter(None, temp_list))
        # print(temp_list)
        temp_cnt = 1
        result_length = 0
        for j in range(1,len(temp_list)):
            if temp_list[j-1] == temp_list[j]:
                temp_cnt += 1
            else:
                # print(temp_cnt)
                if temp_cnt == 1:
                    result_length += i
                else:
                    result_length += len(str(temp_cnt)) + i
                    temp_cnt = 1
        # print(temp_cnt)
        if temp_cnt == 1:
            result_length += len(temp_list[-1])
        else:
            result_length += len(str(temp_cnt)) + i
            temp_cnt = 1
        # print(result_length)
        count = min(count, result_length)
    
    return count

print(solution(s1))
print(solution(s2))
print(solution(s3))
print(solution(s4))
print(solution(s5))
print(solution(s6))

s = "aabbaccc"
# while True:
# cnt = 0
# # i = 1
s_list1 = [s[i] for i in range(len(s))]
s_list1 = list(filter(None, s_list1))
i = 1

# print(str(i))
# print(s_list1)

# temp_cnt = 1
# result_length = 0

# for j in range(1,len(s_list1)):

#     if s_list1[j-1] == s_list1[j]:
#         temp_cnt += 1
#     else:
#         print(temp_cnt)
#         if temp_cnt == 1:
#             result_length += i
#         else:
#             result_length += len(str(i)) + i
#             temp_cnt = 1
# print(temp_cnt)
# result_length += len(str(i)) + i

# print(result_length)

# s_list2 = [s[2*i:2*i+2] for i in range(len(s))]
# s_list2 = list(filter(None, s_list2))

# print(s_list2)

# s_list3 = [s[3*i:3*i+3] for i in range(len(s))]
# s_list3 = list(filter(None, s_list3))
# print(s_list3)