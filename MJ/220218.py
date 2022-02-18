def solution(s):
    chars = ['zero','one','two','three','four','five','six','seven','eight','nine']
    ans = ''

    while len(s) > 0:
        if s[0].isdecimal():
            ans = ans + s[0]
            s = s[1:]
        else:
            for i in range(10):
                c = chars[i]
                d = len(c)
                if s[:d] == c:
                    ans = ans + str(i)
                    s = s[d:]
                    break

    return int(ans)