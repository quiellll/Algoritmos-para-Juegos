def is_feasible(sdk, row, col, num):

    for y in range(9):
        if sdk[row][y] == num:
            return False

    for x in range(9):
        if sdk[x][col] == num:
            return False

    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for n in range(3):
        for m in range(3):
            if sdk[row_start + n][col_start + m] == num:
                return False

    return True


def solve(sdk):

    for row in range(9):
        for col in range(9):

            if sdk[row][col] == 0:
                for num in range(1, 10):

                    if is_feasible(sdk, row, col, num):
                        sdk[row][col] = num

                        if solve(sdk):
                            return True

                        sdk[row][col] = 0

                return False

    return True


sudoku = []

for i in range(9):
    insert_row = list(map(int, input().strip().split()))
    sudoku.append(insert_row)

solve(sudoku)
for r in sudoku:
    print(" ".join(map(str, r)))
