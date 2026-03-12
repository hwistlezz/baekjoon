n = int(input())
s = input()

b_cnt = s.count("bigdata")
s_cnt = s.count("security")

if b_cnt > s_cnt:
    print("bigdata?")
elif b_cnt < s_cnt:
    print("security!")
else:
    print("bigdata? security!")