N = int(input())

digits = 1
start_number = 1
cnt = 9

while N > digits * cnt:
    N -= digits * cnt
    digits += 1
    start_number *= 10
    cnt *= 10

goal_number = start_number + (N - 1) // digits
pos = (N - 1) % digits
print(str(goal_number)[pos])