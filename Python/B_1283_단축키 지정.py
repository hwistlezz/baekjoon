n = int(input())
options = [input() for _ in range(n)]
used = [False] * 26

for options_idx in range(n):  # 옵션(줄)마다
    words = options[options_idx].split()
    find = False
    ans = ""
    # 1) 각 단어의 첫 글자 검사
    for i in range(len(words)):  # 각 단어마다 첫 글자 검사
        letter_idx = ord(words[i][0].lower()) - ord('a')  # 첫 글자 인덱스
        if used[letter_idx]:
            ans += words[i] + " "
            continue
        else:
            ans += "[" + words[i][0] + "]" + words[i][1:] + " "

            # 나머지 단어들 ans에 추가
            for rest_idx  in range(i + 1, len(words)):
                ans += words[rest_idx ] + " "

            find = True
            used[letter_idx] = True
            break

    if find:
        print(ans.rstrip())
        continue

    # 2) 각 단어의 두번째 ~ 마지막 글자까지 단어 순서대로 검사
    ans = ""  # ans 초기화
    for i in range(len(words)):  # 각 단어마다 ("abc" "def" "ghi")
        ans += words[i][0]
        for char_pos in range(1, len(words[i])):  # 단어의 길이만큼 (단어 첫글자 제외) ("abc")
            letter_idx = ord(words[i][char_pos].lower()) - ord('a')
            if used[letter_idx]:
                ans += words[i][char_pos]
                continue
            else:
                ans += "[" + words[i][char_pos] + "]" + words[i][char_pos + 1:] + " "

                # 나머지 단어들 ans에 추가
                for rest_idx in range(i + 1, len(words)):
                    ans += words[rest_idx] + " "

                find = True
                used[letter_idx] = True
                break

        if not find:
            ans += " "
        else:  # find
            print(ans.rstrip())
            break

    if not find:
        print(ans.rstrip())