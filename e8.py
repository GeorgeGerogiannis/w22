import random
rows, cols = (0, 0)
while rows <= 1 and cols <= 1:
    rows = int(input('Select number of rows: '))
    cols = int(input('Select number of columns: '))
points = [0, 0]
for i in range(0,100):
    chessboard = [["#" for i in range(cols)] for j in range(rows)]

    A_row = random.randint(0,rows - 1)
    A_col = random.randint(0,cols - 1)
    P_row = random.randint(0,rows - 1)
    P_col = random.randint(0,cols - 1)
    while A_row == P_row and A_col == P_col:
        P_row = random.randint(0,rows - 1)
        P_col = random.randint(0,cols - 1)
    chessboard[A_row][A_col] = "Α"
    chessboard[P_row][P_col] = "Π"
    
    for r in chessboard:
        for c in r:
            print(c,end = " ")
        print()
    if A_row == P_row or A_col == P_col:
        print("Π wins!")
        points[0] += 1
    elif (abs(A_row - A_col) == abs(P_row - P_col) and abs(A_row - P_row) == abs(A_col - P_col)) or abs(A_row - P_row) == abs(A_col - P_col):
        print("Α wins!")
        points[1] += 1
    else:
        print("No winner")
print("Π points:", points[0])
print("Α points:", points[1])
