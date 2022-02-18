import random

xartia = []
figures = ["J", "Q", "K"]
xarti = [i for i in range(1, 11)] + figures
color = ["H", "S", "C", "D"]
tenorfigures = []
counter = [0, 0, 0]
ans=input("Should P1 start with a 10/figure? Y/N ")
ans2=input("Activate auto-round? Y/N ")
for i in range(0,100):
    pointer=0
    for i in xarti:
        pointer += 1 
        for j in color:
            xartia.append([i,j])
            if pointer >= 10 and (ans=="Y" or ans=="y"):
                tenorfigures.append([i,j])
    random.shuffle(xartia)
    random.shuffle(tenorfigures)
    player1=[]
    sum1=0
    turn1=0
    print("P1 Cards:")
    while sum1<16:
        sum1=0
        if turn1==0 and (ans=="Y" or ans=="y"):
            player1.append(tenorfigures.pop())
            turn1=1
        else:
            player1.append(xartia.pop())
        print(player1)
        for card in player1:
            if card[0] in figures:
                sum1=sum1+10
            else:
                sum1=sum1+card[0]
        print(sum1)
    if sum1>21:
        print("P2 wins!")
        counter[1] += 1
    else:
        print("P2 joins the game")
        player2=[]
        sum2=0
        print("P2 Cards:")
        while sum2<16:
            sum2=0
            player2.append(xartia.pop())
            print(player2)
            for card in player2:
                if card[0] in figures:
                    sum2=sum2+10
                else:
                    sum2=sum2+card[0]
            print(sum2)
        if sum2>21:
            sum2=0
        if sum1>sum2:
            print("P1 wins!")
            counter[0] += 1
        elif sum2>sum1:
            print("P2 wins!")
            counter[1] += 1
        else:
            print("draw!")
            counter[2] += 1
    if ans2!="Y" and ans2!="y":
        R=input("Press enter to start the next round. ")
print("Player1 wins:")
print(counter[0])
print("Player2 wins:")
print(counter[1])
print("Draws:")
print(counter[2])
