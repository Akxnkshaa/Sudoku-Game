import numpy as np

status = 'yes'
sudoku_puzzle = [[5,3,0,0,7,0,0,0,0],
                 [6,0,0,1,9,5,0,0,0],
                 [0,9,8,0,0,0,0,6,0],
                 [8,0,0,0,6,0,0,0,3],
                 [4,0,0,8,0,3,0,0,1],
                 [7,0,0,0,2,0,0,0,6],
                 [0,6,0,0,0,0,2,8,0],
                 [0,0,0,0,1,9,0,0,5],
                 [0,0,0,0,0,0,0,0,0]]


def possible(Row, Column, Num):
    global sudoku_puzzle

    for i in range(0, 9):
        if sudoku_puzzle[Row][i] == Num:
            return False

    for i in range(0, 9):
        if sudoku_puzzle[i][Column] == Num:
            return False

    x0 = (Column // 3) * 3
    y0 = (Row // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if sudoku_puzzle[y0 + i][x0 + j] == Num:
                return False

    return True

def solution():
    global sudoku_puzzle, status
    for Row in range(0, 9):
        for Column in range(0, 9):
            if sudoku_puzzle[Row][Column] == 0:  
                for Num in range(1, 10):
                    if possible(Row, Column, Num):
                        sudoku_puzzle[Row][Column] = Num
                        solution()
                        sudoku_puzzle[Row][Column] = 0
                return 
    

    print(np.matrix(sudoku_puzzle))

    if input('More possible solutions? (yes/no): ').lower() != 'yes':
        status = 'no'
        print("No more possible solutions.")
        exit()

if solution() is None:
    print("No possible solutions.") 
