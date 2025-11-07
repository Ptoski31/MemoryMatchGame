import tkinter as tk
import random
import time
from tkinter import messagebox

# ----------------------------
# Memory Match Game (GUI)
# ----------------------------
class MemoryGameGUI:
    def __init__(self, root, size=4):
        self.root = root
        self.root.title("Memory Match Game")
        self.size = size
        self.buttons = {}
        self.first_choice = None
        self.second_choice = None
        self.matches_found = 0
        self.total_pairs = (size * size) // 2
        self.attempts = 0

        # Generate shuffled board
        letters = [chr(65 + i) for i in range(self.total_pairs)] * 2
        random.shuffle(letters)
        self.board = [letters[i * size:(i + 1) * size] for i in range(size)]

        # GUI setup
        self.create_widgets()

    # ----------------------------
    # Create game grid and UI
    # ----------------------------
    def create_widgets(self):
        header = tk.Label(self.root, text="🧠 Memory Match Game", font=("Helvetica", 18, "bold"), fg="blue")
        header.grid(row=0, column=0, columnspan=self.size, pady=10)

        self.status_label = tk.Label(self.root, text="Find all matching pairs!", font=("Helvetica", 12))
        self.status_label.grid(row=1, column=0, columnspan=self.size, pady=(0, 10))

        for r in range(self.size):
            for c in range(self.size):
                btn = tk.Button(
                    self.root, text="❓", width=8, height=3,
                    font=("Helvetica", 16, "bold"),
                    command=lambda row=r, col=c: self.reveal_card(row, col)
                )
                btn.grid(row=r + 2, column=c, padx=5, pady=5)
                self.buttons[(r, c)] = btn

    # ----------------------------
    # Reveal card on click
    # ----------------------------
    def reveal_card(self, row, col):
        # Prevent clicking the same card twice or too fast
        if self.first_choice and self.second_choice:
            return
        btn = self.buttons[(row, col)]
        value = self.board[row][col]
        btn.config(text=value, state="disabled", disabledforeground="black", bg="lightyellow")

        if not self.first_choice:
            self.first_choice = (row, col)
        else:
            self.second_choice = (row, col)
            self.root.after(700, self.check_match)  # small delay to show second card

    # ----------------------------
    # Check if two revealed cards match
    # ----------------------------
    def check_match(self):
        r1, c1 = self.first_choice
        r2, c2 = self.second_choice
        v1 = self.board[r1][c1]
        v2 = self.board[r2][c2]
        self.attempts += 1

        if v1 == v2:
            self.status_label.config(text=f"✅ Match found! Total matches: {self.matches_found + 1}")
            self.buttons[(r1, c1)].config(bg="lightgreen")
            self.buttons[(r2, c2)].config(bg="lightgreen")
            self.matches_found += 1
        else:
            self.status_label.config(text="❌ Not a match. Try again!")
            self.root.after(500, lambda: self.hide_cards(r1, c1, r2, c2))

        self.first_choice = None
        self.second_choice = None

        # Check for game completion
        if self.matches_found == self.total_pairs:
            self.end_game()

    # ----------------------------
    # Hide non-matching cards again
    # ----------------------------
    def hide_cards(self, r1, c1, r2, c2):
        for (r, c) in [(r1, c1), (r2, c2)]:
            btn = self.buttons[(r, c)]
            btn.config(text="❓", state="normal", bg="SystemButtonFace")

    # ----------------------------
    # Game end dialog
    # ----------------------------
    def end_game(self):
        messagebox.showinfo(
            "Congratulations!",
            f"🎉 You matched all pairs in {self.attempts} attempts!"
        )
        self.root.destroy()


# ----------------------------
# Run the game
# ----------------------------
if __name__ == "__main__":
    root = tk.Tk()
    game = MemoryGameGUI(root)
    root.mainloop()
