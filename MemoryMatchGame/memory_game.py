import random
import time

# ----------------------------
# ANSI color codes
# ----------------------------
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
RESET = "\033[0m"

# ----------------------------
# Function: Create game board
# ----------------------------
def create_board(size=4):
    """
    Create and shuffle a game board with pairs of letters.
    Default is 4x4 (16 cards → 8 pairs).
    """
    num_pairs = (size * size) // 2
    letters = [chr(65 + i) for i in range(num_pairs)] * 2
    random.shuffle(letters)
    board = [letters[i * size:(i + 1) * size] for i in range(size)]
    return board

# ----------------------------
# Function: Display the board
# ----------------------------
def display_board(board, revealed):
    """
    Display the current state of the board.
    'revealed' is a set of tuples for coordinates that are face-up.
    """
    size = len(board)
    print(CYAN + "\nBoard:" + RESET)
    print("   " + "  ".join(str(i) for i in range(size)))
    print("  " + "-" * (size * 3))
    for r in range(size):
        row = []
        for c in range(size):
            if (r, c) in revealed:
                row.append(GREEN + board[r][c] + RESET)
            else:
                row.append("*")
        print(f"{r} | " + "  ".join(row))
    print()

# ----------------------------
# Function: Handle one turn
# ----------------------------
def handle_turn(board, revealed, size):
    try:
        first = tuple(int(x) for x in input(YELLOW + "Enter first card (row col): " + RESET).split())
        if len(first) != 2 or any(x < 0 or x >= size for x in first) or first in revealed:
            print(RED + "⚠ Invalid first card selection. Try again." + RESET)
            return False

        second = tuple(int(x) for x in input(YELLOW + "Enter second card (row col): " + RESET).split())
        if len(second) != 2 or any(x < 0 or x >= size for x in second) or second == first or second in revealed:
            print(RED + "⚠ Invalid second card selection. Try again." + RESET)
            return False

        # Show selected cards temporarily
        display_board(board, revealed | {first, second})

        # Check for match
        if board[first[0]][first[1]] == board[second[0]][second[1]]:
            print(GREEN + "✅ It's a match!\n" + RESET)
            revealed.update([first, second])
            return True
        else:
            print(RED + "❌ Not a match.\n" + RESET)
            time.sleep(1)
            return False

    except ValueError:
        print(RED + "⚠ Invalid input. Enter two numbers separated by space." + RESET)
        return False
    except Exception as e:
        print(RED + f"⚠ Unexpected error: {e}" + RESET)
        return False

# ----------------------------
# Main Game Function
# ----------------------------
def play_game():
    size = 4
    board = create_board(size)
    revealed = set()
    attempts = 0

    print(MAGENTA + "\n=== Welcome to the Memory Match Game ===" + RESET)
    print(CYAN + "Find all matching pairs!" + RESET)
    print(YELLOW + "Enter coordinates as: row column (e.g., 1 2)\n" + RESET)

    while len(revealed) < size * size:
        display_board(board, revealed)
        handle_turn(board, revealed, size)
        attempts += 1

    print(GREEN + f"\n🎉 Congratulations! You matched all pairs in {attempts} attempts!" + RESET)
    print(CYAN + "Thanks for playing!\n" + RESET)

# ----------------------------
# Program Entry Point
# ----------------------------
if __name__ == "__main__":
    try:
        play_game()
    except KeyboardInterrupt:
        print(RED + "\n\nGame interrupted by user. Exiting safely..." + RESET)
    except Exception as e:
        print(RED + f"\nCritical error: {e}" + RESET)
