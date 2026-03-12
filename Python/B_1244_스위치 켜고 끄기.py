switch_num = int(input())
switch = list(map(int, input().split()))

student_num = int(input())
student_info = []
for _ in range(student_num):
    gender, num = map(int, input().split())
    student_info.append((gender, num))

for gender, num in student_info:
    if gender == 1:  # 남자
        for i in range(num-1, switch_num, num):  # step=num
            if switch[i] == 0:
                switch[i] = 1
            elif switch[i] == 1:
                switch[i] = 0
    elif gender == 2:  #  여자
        is_symmetry = True
        count = 0
        i = 1
        while is_symmetry and 0 <= (num-1 - i) and (num-1 + i) < switch_num:
            if switch[num-1 - i] == switch[num-1 + i]:
                is_symmetry = True
                count += 1
            else:
                is_symmetry = False

            i += 1

        for x in range((num - count - 1), (num + count)):
            # swap
            if switch[x] == 0:
                switch[x] = 1
            elif switch[x] == 1:
                switch[x] = 0

cnt = 0
for i in range(len(switch)):
    print(switch[i], end=" ")
    cnt += 1

    if cnt == 20:
        print()
        cnt = 0