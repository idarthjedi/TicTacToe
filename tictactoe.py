import os


def print_grid():
    os.system('cls')
    print("\t\t\t_{1}_ _{2}_ _{3}_")
    print("\t\t\t_{4}_|_{5}_|_{6}_")
    print("\t\t\t_{7}_|_{8}_|_{9}_")
    print('')


def print_instructions(players):
    print('*'*60)
    print("%s is [X], %s is [O]. Each player will take a turn." % (players[0], players[1]))
    print("The Tic Tac Toe board is a 3x3 square, it looks like this:")
    print("The game is broken up into a grid pattern, as follows:")
    print('')
    print("\t\t\t_{1}_ _{2}_ _{3}_")
    print("\t\t\t_{4}_|_{5}_|_{6}_")
    print("\t\t\t_{7}_|_{8}_|_{9}_")
    print('')
    print("To place your mark, just type a number [1-9]")
    print('*'*60)
    response = input("Press any key to continue: ")


def main():
    # Collect the player names
    players = list()

    for x in range(2):
        prompt = input("Please enter a player name: ")
        players.append(prompt)

    # Print introduction to players
    print("Welcome to Tic Tac Toe %s and %s!  May the odds be ever in your favor!" % (players[0], players[1]))
    prompt = input("Would you like to see instructions: [y/N]: ")
    if (prompt == 'y') or (prompt == 'Y'):
        print_instructions(players)

    # Loop through each Player for 3 iterations
    for n in range(1, 10):
        successful = False
        # Loop until player puts in a valid number 1-9
        while not successful:
            # Even mod %2 = 0
            player = players[n % 2]

            # Loop until they put in a number
            is_number = False
            while not is_number:
                print_grid()
                try:
                    player_move = int(input('%s, select your move [1-9] : ' % player))
                    is_number = True
                except ValueError:
                    is_number = False

            # Set successful = False if they didn't chose 1-9
            if player_move in range(1, 10):
                successful = True

        # Replace the { Num }
        # Check to see if a player has won
        # move to the next
        pass


main()


