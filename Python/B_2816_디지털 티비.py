n = int(input())

channels = [input() for _ in range(n)]

pointer_idx = 0
idx_1 = channels.index("KBS1")
for _ in range(idx_1):
    print(1, end="")
    pointer_idx += 1

for _ in range(idx_1):
    print(4, end="")
    channels[pointer_idx - 1], channels[pointer_idx] = channels[pointer_idx], channels[pointer_idx - 1]
    pointer_idx -= 1

idx_2 = channels.index("KBS2")
for _ in range(idx_2):
    print(1, end="")
    pointer_idx += 1

for _ in range(idx_2 - 1):
    print(4, end="")
    channels[pointer_idx - 1], channels[pointer_idx] = channels[pointer_idx], channels[pointer_idx - 1]
    pointer_idx -= 1