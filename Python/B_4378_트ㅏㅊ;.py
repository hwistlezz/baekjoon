keyboard = "`1234567890-=QWERTYUIOP[]\ASDFGHJKL;'ZXCVBNM,./"

while True:
    try:
        s = input()
    except EOFError:
        break

    ans = []
    for ch in s:
        if ch == ' ':
            ans.append(' ')
        else:
            idx = keyboard.find(ch)  # ch의 위치
            ans.append(keyboard[idx-1])# 왼쪽 키

    print(''.join(ans))