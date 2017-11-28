import os
from sys import platform

graph = [None, None, None]
graph[0] = [i for i in range(1, 4)]
graph[1] = [i for i in range(4, 7)]
graph[2] = [i for i in range(7, 10)]


class BColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def print_grid(clear=True):
    if clear:
        if platform == "linux" or platform == "linux2":
            os.system('clear')
        elif platform == 'win32':
            os.system('cls')
        elif platform == 'darwin':
            pass
    else:
        print()
    print()
    print()
    print()
    print("\t\t\t_{%s}_|_{%s}_|_{%s}_" % (graph[0][0], graph[0][1], graph[0][2]))
    print("\t\t\t_{%s}_|_{%s}_|_{%s}_" % (graph[1][0], graph[1][1], graph[1][2]))
    print("\t\t\t_{%s}_|_{%s}_|_{%s}_" % (graph[2][0], graph[2][1], graph[2][2]))
    print()


def print_instructions(players):
    print('*'*60)
    print("%s is [X], %s is [O]. Each player will take a turn." % (players[0], players[1]))
    print("The Tic Tac Toe board is a 3x3 square, the game is broken up into a grid pattern, as follows:")
    print_grid(False)
    print("To place your mark, just type a number [1-9]")
    print('*'*60)
    response = input("Press any key to continue: ")



def set_mark(index, value):
    internal_index = 0
    if index in range(1, 4):
        graph_index = 0
        internal_index = index - 1
    elif index in range(4, 7):
        graph_index = 1
        internal_index = index - 4
    else:
        graph_index = 2
        internal_index = index - 7

    if graph[graph_index][internal_index] != index:
        response = input("This box has already been selected, please select another [Enter to continue]:")

        return False
    else:
        graph[graph_index][internal_index] = value
        return True


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
            player_index = n % 2
            player_mark = BColors.OKGREEN + 'X' + BColors.ENDC \
                if player_index == 0 \
                else BColors.FAIL + 'O' + BColors.ENDC

            # Loop until they put in a number
            is_number = False
            while not is_number:
                print_grid()
                try:
                    player_move = int(input('%s, select your move [1-9] : ' % players[player_index]))
                    is_number = True
                except ValueError:
                    is_number = False

            # Set successful = False if they didn't chose 1-9
            if player_move in range(1, 10):
                # The player chose a range 1-9, now let's see if we can successfully mark this selection
                successful = set_mark(player_move, player_mark)

        # Check to see if a player has won
        # move to the next

        pass

    print_grid()


main()


