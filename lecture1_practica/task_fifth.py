N = int(input())

numbers = list(range(2, N + 1))

for n in numbers:
    for i in numbers:
        if n != i and i % n == 0:
            numbers.remove(i)

print(numbers)