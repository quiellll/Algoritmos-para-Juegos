def printSol(s):
    for i in range(len(s)):
        if sol[i] != 0:
            print(sol[i], "Billete(s) de ", cand[i], " euros")


def isNotSol(v):
    return v > 0


def isFeasible(v, cv):
    return v // cv != 0


def greedyCoins(v, c, s):
    currentCoin = 0

    while isNotSol(v):
        if not isFeasible(v, c[currentCoin]):
            currentCoin += 1
        else:
            s[currentCoin] += 1
            v -= c[currentCoin]
    return s


cand = [500, 200, 100, 50, 20, 10, 5, 2, 1]
value = 437
sol = [0] * len(cand)

greedyCoins(value, cand, sol)
printSol(sol)
