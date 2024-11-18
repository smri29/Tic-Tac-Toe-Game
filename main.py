def print_board(board):
    """Display the Tic Tac Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board):
    """Check for a winner or tie."""
    # Check rows, columns, and diagonals
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    # Check for a tie
    for row in board:
        if " " in row:
            return None  # Game is still ongoing

    return "Tie"


def tic_tac_toe():
    """Main game loop for Tic Tac Toe."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("Welcome to Tic Tac Toe!")
    print("Player 1 is 'X' and Player 2 is 'O'.\n")

    for turn in range(9):  # Maximum of 9 turns in a 3x3 grid
        print_board(board)
        print(f"\n{current_player}'s turn.")

        while True:
            try:
                row = int(input("Enter the row (0, 1, or 2): "))
                col = int(input("Enter the column (0, 1, or 2): "))

                if row < 0 or row > 2 or col < 0 or col > 2:
                    print("Invalid position! Please choose a row and column between 0 and 2.")
                    continue

                if board[row][col] != " ":
                    print("That spot is already taken! Try again.")
                    continue

                board[row][col] = current_player
                break
            except ValueError:
                print("Invalid input! Please enter numbers only.")

        # Check if there is a winner
        result = check_winner(board)
        if result:
            print_board(board)
            if result == "Tie":
                print("\nIt's a tie!")
            else:
                print(f"\nPlayer {'1' if result == 'X' else '2'} ({result}) wins!")
            return

        # Switch player
        current_player = "O" if current_player == "X" else "X"

    print("\nIt's a tie!")


# Start the game
tic_tac_toe()
