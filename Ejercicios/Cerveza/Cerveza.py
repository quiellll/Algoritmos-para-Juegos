IBU = input()

match int(IBU):
    case num if 0 <= num <= 10:
        print('CRUZCAMPO')
    case num if 11 <= num <= 20:
        print('MALA')
    case num if 21 <= num <= 35:
        print('REGULAR')
    case num if 26 <= num <= 45:
        print('BUENA')
    case num if 46 <= num:
        print('MUY BUENA')
    case _:
        print('INVALIDO')
