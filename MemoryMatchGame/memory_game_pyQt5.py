import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel, QMessageBox
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont

class MemoryMatchGameQT(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Memory Match Game")
        self.setFixedSize(500, 500)

        self.attempts = 0
        self.matches = 0
        self.first_choice = None
        self.second_choice = None

        self.cards = list("AABBCCDDEEFFGGHH")
        random.shuffle(self.cards)
        self.buttons = []

        self.grid = QGridLayout()
        self.setLayout(self.grid)

        self.attempt_label = QLabel(f"Attempts: {self.attempts}")
        self.attempt_label.setFont(QFont("Arial", 14))
        self.attempt_label.setAlignment(Qt.AlignCenter)
        self.grid.addWidget(self.attempt_label, 0, 0, 1, 4)

        # Create buttons
        self.revealed = [False]*16
        for i in range(16):
            btn = QPushButton("*")
            btn.setFont(QFont("Arial", 20))
            btn.setFixedSize(80, 80)
            btn.clicked.connect(lambda checked, idx=i: self.flip_card(idx))
            self.buttons.append(btn)
            row = (i//4)+1
            col = i%4
            self.grid.addWidget(btn, row, col)

        # Restart button
        self.restart_btn = QPushButton("Restart Game")
        self.restart_btn.clicked.connect(self.restart_game)
        self.grid.addWidget(self.restart_btn, 5, 0, 1, 4)

    def flip_card(self, idx):
        if self.revealed[idx] or self.second_choice is not None:
            return

        self.buttons[idx].setText(self.cards[idx])
        self.revealed[idx] = True

        if self.first_choice is None:
            self.first_choice = idx
        else:
            self.second_choice = idx
            self.attempts += 1
            self.attempt_label.setText(f"Attempts: {self.attempts}")
            QTimer.singleShot(700, self.check_match)

    def check_match(self):
        if self.cards[self.first_choice] == self.cards[self.second_choice]:
            self.buttons[self.first_choice].setStyleSheet("background-color: lightgreen")
            self.buttons[self.second_choice].setStyleSheet("background-color: lightgreen")
            self.matches += 1
            if self.matches == 8:
                QMessageBox.information(self, "Congratulations!", f"You won in {self.attempts} attempts!")
        else:
            self.buttons[self.first_choice].setText("*")
            self.buttons[self.second_choice].setText("*")
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
        self.attempt_label.setText(f"Attempts: {self.attempts}")
        self.revealed = [False]*16
        for btn in self.buttons:
            btn.setText("*")
            btn.setStyleSheet("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = MemoryMatchGameQT()
    game.show()
    sys.exit(app.exec_())
