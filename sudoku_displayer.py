sudoku = [
    [0, 0, 0, 0, 6, 4, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 3, 9, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 2, 0, 6, 0],
    [0, 8, 0, 4, 0, 0, 0, 0, 0],
    [3, 5, 0, 6, 0, 0, 0, 7, 0],
    [0, 0, 2, 0, 0, 0, 1, 0, 3],
    [0, 0, 1, 0, 5, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 0]
]

counter = 0
for i in sudoku:
    if counter % 3 == 0: 
        print("- - - - - - - - - - - - - - - -")
    for j in range(1, 9):
        if j == 3 or j == 7:
            sudoku[counter].insert(j, "|")
        
    print(*i, sep="  ")
    counter += 1
    if counter == 9 : 
        print("- - - - - - - - - - - - - - - -")
