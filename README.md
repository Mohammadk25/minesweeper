# Minesweeper Game

Welcome to the Minesweeper game! This classic game challenges you to uncover all the safe cells without detonating any bombs.

## Table of Contents

- [Getting Started](#getting-started)
- [Gameplay](#gameplay)
- [Features](#features)
- [Levels of Difficulty](#levels-of-difficulty)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

1. **Clone the Repository:** Clone this repository to your local machine.

2. **Navigate to the Directory:** Open a terminal or command prompt and navigate to the directory where you cloned the repository.

3. **Run the Game:** Run the game by executing the Python script `minesweeper.py`.

   ```bash
   python minesweeper.py
# Gameplay

- **Choose Difficulty:** Select the difficulty level: easy, medium, or hard.
- **Enter Grid Size:** Enter the size of the grid. For easy difficulty, the size is fixed at 9x9.
- **Revealing Cells:** Enter the row (A to I) and column (1 to 9) to reveal a cell.
- **Objective:** Uncover all non-bomb cells without detonating any bombs.
- **Winning:** You win the game by uncovering all safe cells.
- **Losing:** The game ends if you detonate a bomb.

# Features

- **Random Bomb Placement:** Bombs are randomly placed on the grid.
- **Grid Display:** Display the grid with the location of bombs and uncovered cells.
- **Recursive Reveal:** Automatically reveals adjacent cells with no adjacent bombs.
- **Win/Loss Detection:** Detects when all safe cells are uncovered or a bomb is detonated.

# Levels of Difficulty

- **Easy:** Fixed 9x9 grid with a predefined bomb layout.
- **Medium:** Randomly generated grid with a moderate number of bombs.
- **Hard:** Randomly generated grid with a high number of bombs. Bombs can move after each move.
