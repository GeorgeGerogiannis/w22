import random

ans = input("Execute? Y/N ")
ans2 = input("Enable turn-by-turn mode? Y/N ")
while ans == "Y" or ans == "y":
    sum = 0
    for j in range(0,100):
        rings = [1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,3 ,3 ,3 ,3 ,3 ,3 ,3 ,3 ,3] #1 = megalo, 2 = mesaio, 3 = mikro
        blocks = [[[100, 101, 102], [103, 104, 105], [106, 107, 108]], [[109, 110, 111], [112, 113, 114], [115, 116, 117]], [[118, 119, 120], [121, 122, 123], [124, 125, 126]]]
        end = 0
        count = 0
        while end == 0:
            r_rng = random.randint(0,26 - count)
            b_row = random.randint(0,2)
            b_col = random.randint(0,2)
            if rings[r_rng] != blocks[b_row][b_col][rings[r_rng] - 1]:
                blocks[b_row][b_col][rings[r_rng] - 1] = rings[r_rng]
                count += 1
                del rings[r_rng]
                for i in range(0,2):
                    if (blocks[b_row][0][i] == blocks[b_row][1][i] == blocks[b_row][2][i]) or (blocks[0][b_col][i] == blocks[1][b_col][i] == blocks[2][b_col][i]) or (blocks[b_row][0][0] == 1 and blocks[b_row][1][1] == 2 and blocks[b_row][2][2] == 3) or (blocks[b_row][0][2] == 3 and blocks[b_row][1][1] == 2 and blocks[b_row][2][0] == 1) or (blocks[0][b_col][2] == 3 and blocks[1][b_col][1] == 2 and blocks[2][b_col][0] == 1) or (blocks[0][b_col][0] == 1 and blocks[1][b_col][1] == 2 and blocks[2][b_col][2] == 3):
                        end = 1
                    else:
                        if b_row == b_col:
                            if (blocks[0][0][i] == blocks[1][1][i] == blocks[2][2][i]) or (blocks[0][0][0] == 1 and blocks[1][1][1] == 2 and blocks[2][2][2] == 3) or (blocks[0][0][2] == 3 and blocks[1][1][1] == 2 and blocks[2][2][0] == 1):
                                end = 1
                        elif b_row + b_col == 2:
                            if (blocks[0][2][i] == blocks[1][1][i] == blocks[2][0][i]) or (blocks[0][2][0] == 1 and blocks[1][1][1] == 2 and blocks[2][0][2] == 3) or (blocks[0][2][2] == 3 and blocks[1][1][1] == 2 and blocks[2][0][0] == 1):
                                end = 1
            for r in blocks:
                for c in r:
                    print(c,end = " ")
                print()
            if ans2 == "Y" or ans2 == "y":
                turn = input("Next Turn...")
            else:
                print("Next Turn")
        sum += count
    m_o = int(sum / (j + 1))
    print(m_o)
    ans = input("Restart? Y/N ")
