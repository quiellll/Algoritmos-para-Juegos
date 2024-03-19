def checkPalindrome(word):
    lengthDividedBy2 = len(word) / 2
    lengthDividedBy2Floor = int(lengthDividedBy2)
    for i in range(lengthDividedBy2Floor):
        if word[i] != word[len(word) - (i + 1)]:
            return False
    return True


n = input().strip()

winner = "EMPATE"
ended = False

ana = 0
monica = 0
pointer = 0

for p in range(int(n)):

    w = input().strip()

    if pointer % 2 == 0:
        if checkPalindrome(w):
            ana += 1
        elif ended is False:
            winner = "MONICA"
            ended = True
    elif pointer % 2 == 1:
        if checkPalindrome(w):
            monica += 1
        elif ended is False:
            winner = "ANA"
            ended = True

    pointer += 1


print(str(ana) + " " + str(monica) + " " + str(winner))
