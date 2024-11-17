input = input().strip().split()

A, B = map(int, input)
if A > B:
    print('>')
elif A < B:
    print('<')
else:
    print('==')