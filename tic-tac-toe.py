theBoard = {"7": "7" , "8": "8" , "9": "9" ,
            "4": "4" , "5": "5" , "6": "6" ,
            "1": "1" , "2": "2" , "3": "3" }

board_keys = []

for key in theBoard:
    board_keys.append(key)

def printBoard(board):
    print()
    print(board["7"] + "|" + board["8"] + "|" + board["9"])
    print("-+-+-")
    print(board["4"] + "|" + board["5"] + "|" + board["6"])
    print("-+-+-")
    print(board["1"] + "|" + board["2"] + "|" + board["3"])
    print()

def game():

    turn = "x"
    count = 0


    for i in range(10):
        printBoard(theBoard)
        print("It's your turn, " + turn + ". Move to which place?")

        move = input()        

        if theBoard[move] != "x" and theBoard[move] != "o":
            theBoard[move] = turn
            count += 1
        else:
            print()
            print("That place is already filled. Try another")
            continue
        
        if count >= 5:
            if theBoard["7"] == theBoard["8"] == theBoard["9"]: # across the top
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")                
                break
            elif theBoard["4"] == theBoard["5"] == theBoard["6"]: # across the middle
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard["1"] == theBoard["2"] == theBoard["3"]: # across the bottom
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard["1"] == theBoard["4"] == theBoard["7"]: # down the left side
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard["2"] == theBoard["5"] == theBoard["8"]: # down the middle
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard["3"] == theBoard["6"] == theBoard["9"]: # down the right side
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 
            elif theBoard["7"] == theBoard["5"] == theBoard["3"]: # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard["1"] == theBoard["5"] == theBoard["9"]: # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
        if count == 9:
            print("\nGame Over.\n")                
            print("It's a Tie!!")
            break
        if turn =="x":
            turn = "o"
        else:
            turn = "x" 
    
    restart = input("Do want to play Again?(y/n): ")
    if restart == "y" or restart == "Y":  
        for key in board_keys:
            theBoard[key] = str(key)
        
        game()

if __name__ == "__main__":
    game()