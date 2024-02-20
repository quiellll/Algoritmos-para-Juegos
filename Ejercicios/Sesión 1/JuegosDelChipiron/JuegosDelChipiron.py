i = input().strip().split()

for c in range(int(i[0])):
    whitespace = int(int(i[0]) - (int(c) + 1))

    for w in range(whitespace):
        print(str(i[2]), end="")
    for f in range(int(c) + 1):
        print(str(i[1]), end="")

    print("\n".strip())
