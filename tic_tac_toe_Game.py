
def checkWin(xState,zState):
    wins =  [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[6,4,2],[0,4,8]]
    for win in wins :
        if xState[win[0]] == 1 and xState[win[1]] == 1 and xState[win[2]] == 1 :
            print (" x won the match ")
            return 1
    for win in wins :
        if zState[win[0]] == 1 and zState[win[1]] == 1 and zState[win[2]] == 1 :
            print(" y won the match ")
            return 0
    # no winner yet
    return -1






def playBoard (xState, zState, ) :
    zero =  f"{"X" if xState[0] else ("O" if zState[0] else 0)}"
    one =  f"{"X " if xState[1] else ("O" if zState[1] else 1)}"
    two = f"{"X" if xState[2] else ("O" if zState[2] else 2)}"
    three = f"{"X" if xState[3] else ("O" if zState[3] else 3)}"
    four = f"{"X" if xState[4] else ("O" if zState[4] else 4)}"
    five = f"{"X" if xState[5] else ("O" if zState[5] else 5)}"
    six = f"{"X" if xState[6] else ("O" if zState[6] else 6)}"
    seven = f"{"X" if xState[7] else ("O" if zState[7] else 7)}"
    eight = f"{"X" if xState[8] else ("O" if zState[8] else 8)}"

    print(f"{zero } | {one} | {two} ")
    print(f"--|---|---")
    print(f"{three} | {four} | {five} ")
    print(f"--|---|---")
    print(f"{six} | {seven} | {eight} ")





if __name__ == "__main__":

    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0, ]
    zState = [0, 0, 0, 0, 0, 0, 0, 0, 0,]
    turn = 1# 1 for x 0 for "O"


    print("welcome to tic tac toe")

    while(True):
        playBoard(xState,zState)

        if(turn == 1):
            print(" x's turn ")
            print ("---------------")
            value = int(input("Enter a value: "))
            xState[value]=1
            turn = turn - 1
        else :
            print("O's turn ")
            print("----------------")
            value = int(input("Enter a value: "))
            zState[value]=1
            turn =  1-turn
        cwin = checkWin(xState,zState)



        if (cwin!= -1 ) :
            print("match over")
            break





















