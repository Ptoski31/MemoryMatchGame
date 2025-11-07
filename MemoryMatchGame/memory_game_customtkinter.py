import customtkinter as ctk
import random
from tkinter import messagebox

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class MemoryMatchGameCTK:
    def __init__(self, root):
        self.root = root
        self.root.title("Memory Match Game")
        self.attempts = 0
        self.matches = 0
        self.first_choice = None
        self.second_choice = None

        self.cards = list("AABBCCDDEEFFGGHH")
        random.shuffle(self.cards)
        self.buttons = []

        # Attempts label
        self.attempt_label = ctk.CTkLabel(self.root, text=f"Attempts: {self.attempts}", font=("Arial", 16))
        self.attempt_label.grid(row=0, column=0, columnspan=4, pady=10)

        # Restart button
        self.restart_btn = ctk.CTkButton(self.root, text="Restart Game", command=self.restart_game)
        self.restart_btn.grid(row=5, column=0, columnspan=4, pady=10)

        # Create buttons
        self.revealed = [False] * 16
        for i in range(16):
            btn = ctk.CTkButton(self.root, text="*", font=("Arial", 20), width=80, height=80,
                                command=lambda idx=i: self.flip_card(idx))
            btn.grid(row=(i//4)+1, column=i%4, padx=5, pady=5)
            self.buttons.append(btn)

    def flip_card(self, idx):
        if self.revealed[idx] or self.second_choice is not None:
            return

        self.buttons[idx].configure(text=self.cards[idx])
        self.revealed[idx] = True

        if self.first_choice is None:
            self.first_choice = idx
        else:
            self.second_choice = idx
            self.attempts += 1
            self.attempt_label.configure(text=f"Attempts: {self.attempts}")
            self.root.after(700, self.check_match)

    def check_match(self):
        if self.cards[self.first_choice] == self.cards[self.second_choice]:
            self.buttons[self.first_choice].configure(fg_color="green")
            self.buttons[self.second_choice].configure(fg_color="green")
            self.matches += 1
            if self.matches == 8:
                messagebox.showinfo("Congratulations!", f"You won in {self.attempts} attempts!")
        else:
            self.buttons[self.first_choice].configure(text="*", fg_color=None)
            self.buttons[self.second_choice].configure(text="*", fg_color=None)
            self.revealed[self.first_choice] = False
            self.revealed[self.second_choice] = False

        self.first_choice = None
        self.second_choice = None

    def restart_game(self):
        random.shuffle(self.cards)
        self.attempts = 0
        self.matches = 0
        self.first_choice = None
        self.second_choice = None
        self.attempt_label.configure(text=f"Attempts: {self.attempts}")
        self.revealed = [False] * 16
        for btn in self.buttons:
            btn.configure(text="*", fg_color=None)


if __name__ == "__main__":
    root = ctk.CTk()
    game = MemoryMatchGameCTK(root)
    root.mainloop()
