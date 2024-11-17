numbers = input().strip().split()

result = 0
for item in numbers:
    result += int(item)
print(result)