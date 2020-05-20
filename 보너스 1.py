N = int(input())
count = 0
number = N

while True:
    new_num = int(number) // 10 + int(number) % 10
    number = str(int(number) // 10) + str(new_num % 10)
    if int(number) != N:
        count += 1
    else:
        break

print(count)