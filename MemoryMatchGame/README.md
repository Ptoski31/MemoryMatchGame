# Memory Match Game

**Project Type:** Python Game  
**Version:** Text-based (Console)  
**Assessment:** Assessment Two, Keele University Python Course

---

## Description

This is a **Memory Match Game** implemented in Python.  
Players try to find all matching pairs of cards in a console-based interface.  

The repository currently contains the **text-based version** of the game.  
A **GUI version** will be developed in a separate branch to enhance usability and visual experience.

---

## Features

- Console-based text game  
- Keeps track of player attempts  
- Simple and easy-to-play memory matching mechanics  
- Designed to be extended with a GUI in a separate branch

---

## Game Play Instructions

1. When the game starts, a board of hidden cards is displayed.  
2. Each turn, the player selects **two cards** to flip.  
3. If the cards match, they remain revealed.  
4. If the cards do not match, they are hidden again.  
5. The goal is to reveal all pairs in as few turns as possible.  
6. The game ends when all pairs are found, and the number of attempts is displayed.

### Example Board Layout
  1  2  3   4
A [] [] [] []
B [] [] [] []
C [] [] [] []
D [] [] [] []

- `[*]` represents a hidden card  
- Players select cards by row and column (e.g., `A1` and `B3`)  
- Matching cards are revealed as their letter/number pair  

---

## Installation & Usage

1. Clone the repository:

```bash
git clone https://github.com/your-username/MemoryMatchGame.git

2. Navigate to the Folder using
cd MemoryMatchGame

3. Run the game
memory_game.py

### Example Turn

1. Player selects `A1` and `B3`:

   1  2  3  4
A [X] [] [] []
B [] [] [O] []
C [] [] [] []
D [] [] [] []  


- `X` and `O` are the revealed cards  
- If they match, they stay revealed: `[X] [*] [*] [*]`  
- If they do not match, they are hidden again in the next turn: `[*] [*] [*] [*]`  
