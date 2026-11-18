# Player = "X" or "O"

def create_board() -> list:
    """Creates a 3x3 board"""
    return [
        [' ', ' ', ' '], 
        [' ', ' ', ' '], 
        [' ', ' ', ' ']
    ]


def display_board(board: list) -> None:
    """Prints the board in current state"""
    for i in range(len(board)):
        # Add a column between each record
        print("ǀ".join(board[i])) # using a "Latin letter dental click" because i thought the pipe looked too tall

        # Seperator between rows
        if i + 1 != len(board):
            print("—+—+—") # em dashes to hide the gaps between symbols


def get_player_move(player: str) -> tuple[int, int]:
    """Ask the user for their move"""
    try:
        row = int(input(f"({player}) Enter the row of your move: "))
        column = int(input(f"({player}) Enter the column of your move: "))
    except TypeError, ValueError:
        print("Please enter an integer")
        row, column = get_player_move(player)

    return row, column


def is_valid_move(board: list, row: int, col: int) -> bool:
    """Checks if something is in the given position"""
    if row < 0 or col < 0:
        return False
    
    try:
        if board[row][col] == " ":
            return True
        return False
    except IndexError:
        return False


def make_move(board: list, row: int, col: int, player: str) -> None:
    """Make the users move on the board"""
    board[row][col] = player


def check_rows(board: list, player: str) -> bool:
    """Check each row to see if someone won"""
    for i in range(len(board)):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True
    return False


def check_columns(board: list, player: str) -> bool:
    """Check each column to see if player won"""
    for i in range(len(board)):
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
    return False


def check_diagonals(board: list, player: str) -> bool:
    """Check each diagonal to see if player won"""
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    elif board[2][0] == player and board[1][1] == player and board[0][2] == player:
        return True
    return False


def check_winner(board: list, player: str) -> bool:
    """Runs already made checks to see if player won"""
    return (
        check_columns(board, player) or
        check_diagonals(board, player) or
        check_rows(board, player)
    )


def check_draw(board: str) -> bool:
    """Checks if it's still possible for a player to win"""
    # check winner
    if check_winner(board, player = "O") or check_winner(board, player = "X"):
        return False

    # Check for more avaliable moves
    for i in range(len(board)):
        if " " in board[i]:
            return False

    # Must be a draw if all spaces are filled and nobody has won
    return True


def switch_player(player: str) -> str:
    """Swaps the players so both people get to play"""
    return "O" if player == "X" else "X"


def play_game(player: str) -> None:
    """Start the game and play untill someone wins or there is a tie"""
    board = create_board()

    while check_winner(board, "O") == False and check_winner(board, "X") == False and check_draw(board) == False:
        print() # empty space
        display_board(board)

        while True:
            row, col = get_player_move(player)
            if is_valid_move(board, row, col):
                break
            else:
                print("Please enter a valid move")
                
        make_move(board, row, col, player)
        player = switch_player(player)

    print("\nGame over!")
    if check_draw(board):
        print("It's a draw!")
    else:
        print(f"{player} wins!")


def main():
    """Main wrapper for the game"""
    print(
        "Welcome to naughts and crosses"
        "\nGet 3 in a row of the same type to win!"
        "\nWe use co-ordinates to place symbols (top left is 0,0 and bottom right is 2,2)"
    )

    while True:
        player = input("Who should go first (X or O)? ").upper()
        if player == "O" or player == "X":
            break
        else:
            print("Please enter either 'O' or 'X'")
    
    play_game(player)
        
    new_game_choice = input("\nWould you like to play a new game (y/n)? ").lower()
    if new_game_choice == 'y':
        main()
    else:
        print("Bye!")


if __name__ == '__main__':
    main()