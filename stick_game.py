def main():
    global sticks
    sticks = int(input("How many sticks are there on the table initially (10-100)? " ))
    while sticks > 1:
        print("There are {} sticks on a table".format(sticks))
        print("Player 1: ")
        player_turn()
        if player_choice > 0 and player_choice < 4:
            sticks_left()
        else:
            print("Enter valid number")
            continue
        if sticks > 1:
            while True:
                print("There are {} sticks on a table".format(sticks))
                print("Player 2:")
                player_turn()
                if player_choice > 0 and player_choice < 4:
                    sticks_left()
                    break
                else:
                    print("Enter valid number")
                    continue
        else:
            print("Player 2! You have to take the last stick and you lose")
            break
    else:
        print("Player 1! You have to take the last stick and you lose")

def player_turn():
    global player_choice
    while True:
        try:
            player_choice = int(input("How many sticks do you take (1-3)? "))
        except ValueError:
            print("That's not an int!")
        else:
            break

def sticks_left():
    global sticks
    sticks -= player_choice

if __name__ == '__main__':
    main()
