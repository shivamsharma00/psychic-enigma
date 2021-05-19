# This script reverse the case of each alphabet in string.

def swap_case(s):
    a = ''
    for i in range(len(s)):
        if s[i].isupper():
            a += s[i].lower()
        else:
            a += s[i].upper()
    
    print(a)


s = 'HacDJD saD'
swap_case(s)