import random
N = 5
A_list = [3,3,5,5,5]

count = 0
for i_1 in range(N):
    for i_2 in range(i_1+1, N):
        if A_list[i_1] != A_list[i_2]:
            continue
        if i_1 < i_2:
            count += 1

print(count)