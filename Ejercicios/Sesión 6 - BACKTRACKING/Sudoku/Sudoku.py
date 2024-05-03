def es_factible(sudoku, fila, columna, num):
    #comprobar la fila
    for i in range(9):
        if sudoku[fila][i] == num:
            return False

    #comprobar la columna
    for i in range(9):
        if sudoku[i][columna] == num:
            return False

    #comprobar el subcuadro 3x3
    inicio_fila = (fila // 3) * 3
    inicio_columna = (columna // 3) * 3
    for i in range(3):
        for j in range(3):
            if sudoku[inicio_fila + i][inicio_columna + j] == num:
                return False
    return True

def resolver_sudoku(sudoku):
    for fila in range(9):
        for columna in range(9):
            if sudoku[fila][columna] == 0:
                for num in range(1, 10):
                    if es_factible(sudoku, fila, columna, num):
                        sudoku[fila][columna] = num

                        if resolver_sudoku(sudoku):
                            return True
                        sudoku[fila][columna] = 0
                return False
    return True

#entrada
sudoku = []

for i in range(9):
    fila = list(map(int, input().strip().split()))
    sudoku.append(fila)

resolver_sudoku(sudoku)
for fila in sudoku:
    print(" ".join(map(str, fila)))
