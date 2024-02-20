t = input().strip().split()
vowels = "aeiouAEIOU"

candidates = int(t[0])
v = 0

for i in range(candidates + 1):

    name = input().strip().split()

    if i == 0:
        v = len([char for char in str(name) if char in vowels])

    else:
        vc = len([char for char in str(name) if char in vowels])
        if vc == v:
            print("ITS A MATCH!")
        else:
            print("NEXT!")
