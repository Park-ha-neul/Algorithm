num1 = int(input().strip())
num2 = input().strip()

for i in reversed(num2):
    print(num1 * int(i))
print(num1 * int(num2))