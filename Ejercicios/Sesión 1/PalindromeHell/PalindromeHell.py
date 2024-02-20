def checkPalindrome(word):
    lengthDividedBy2 = len(word) / 2
    lengthDividedBy2Floor = int(lengthDividedBy2)
    for i in range(lengthDividedBy2Floor):
        if word[i] != word[len(word) - (i + 1)]:
            return False
    return True


n = input().strip()

ana = 0
monica = 0
pointer = 0

for p in range(int(n)):

    w = input().strip()

    if checkPalindrome(w):
        if pointer % 2 == 0:
            ana += 1
        elif pointer % 2 == 1:
            monica += 1

    pointer += 1

if ana > monica:
    print(str(ana) + " " + str(monica) + " ANA")
elif monica > ana:
    print(str(ana) + " " + str(monica) + " MONICA")
else:
    print(str(ana) + " " + str(monica) + " EMPATE")

