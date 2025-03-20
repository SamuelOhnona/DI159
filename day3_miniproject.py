#Mini Chellenge, Tic Tac Toe 

# Step 1: Initialize the Tic-Tac-Toe board using coordinates

# Create the board as a dictionary with keys as coordinates ( "A1", "B2")
board = {
    "A1": " ", "A2": " ", "A3": " ",
    "B1": " ", "B2": " ", "B3": " ",
    "C1": " ", "C2": " ", "C3": " "
}

#Print the board
def print_board():
    print("\n   1   2   3 ")
    print("A  {} | {} | {} ".format(board["A1"], board["A2"], board["A3"])) #format to insert value in case
    print("  ---+---+---")
    print("B  {} | {} | {} ".format(board["B1"], board["B2"], board["B3"]))
    print("  ---+---+---")
    print("C  {} | {} | {} ".format(board["C1"], board["C2"], board["C3"]))
    print("\n")

# Step 2: Function to get a valid coordinate from the player

def get_valid_coordinate():
     """Ask the player for a valid coordinate (e.g., 'A1', 'B2') and return it."""
     valid_coordinates = board.keys()  # The valid keys in the board dictionary
    
     while True:
        coord = input("Enter a coordinate (A1, B2, C3): ").upper()  # Convert to uppercase
        
        if coord in valid_coordinates:
            return coord  # If valid, return the coordinate
        else:
            print("Invalid coordinate! Please enter a valid one (A1 to C3).")  # Error message

# Step 3: Function to place a symbol ('X' or 'O') on the board

def place_symbol(player):
    """Ask the player for a coordinate and place their symbol on the board."""
    while True:
        coord = get_valid_coordinate()  # Get a valid coordinate from the player
        
        if board[coord] == " ":  # Check if the space is free
            board[coord] = player  # Place the symbol (X or O) on the board
            print_board()  # Print the updated board
            break  # Exit the loop if the move was successful
        else:
            print(f"The space {coord} is already taken! Choose another one.")  # Error if the space is occupied

# Step 4: Function to check if there is a winner

def check_winner():
    """Check if any player has won the game."""
    
    # Horizontal check
    for row in ['A', 'B', 'C']:
        if board[f'{row}1'] == board[f'{row}2'] == board[f'{row}3'] and board[f'{row}1'] != " ":
            return True  #horizontal winner
    
    # Vertical check
    for col in ['1', '2', '3']:
        if board[f'A{col}'] == board[f'B{col}'] == board[f'C{col}'] and board[f'A{col}'] != " ":
            return True  #vertical winner
    
    # Diagonal check top left to bottom right
    if board['A1'] == board['B2'] == board['C3'] and board['A1'] != " ":
        return True #diagonal winner
    
    # Diagonal check top right to bottom left
    if board['A3'] == board['B2'] == board['C1'] and board['A3'] != " ":
        return True #diagonal winner
    
    return False  # No winner

# Step 5: main game 

def tic_tac_toe():
    """Main function to run the Tic-Tac-Toe game."""
    global board  # We need to modify the board inside the function

    # Initialize the board
    board = {
        "A1": " ", "A2": " ", "A3": " ",
        "B1": " ", "B2": " ", "B3": " ",
        "C1": " ", "C2": " ", "C3": " "
    }

    print("Welcome to Tic-Tac-Toe!")
    print_board()

    players = ["X", "O"]  # Define the two players
    turn = 0  # To switch between players
    moves = 0  # Count the number of moves made

    while True:
        player = players[turn % 2] # Choose the current player
        print(f"Player {player}, it's your turn")

        place_symbol(player) #ask player to play
        moves += 1 #count the move turn

        #check if there is a winner
        if check_winner():
            print(f"Player {player} wins")
            break #end game

        #check for a tie
        if moves == 9: #all spaces are filled but nobody won
            print("It's a tie")
            break #end game

        turn += 1
    print("Game Over, thanks for playing !!")

tic_tac_toe()







