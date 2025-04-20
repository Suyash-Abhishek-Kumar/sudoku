# Sudoku Game & Solver 🎮🧩

A feature-rich, interactive Sudoku game built with Python and Pygame.  
Play randomly generated Sudoku puzzles, check your answers, or let the built-in solver show you the solution.  
Perfect for both casual players and puzzle enthusiasts!

---

## ✨ Features

- **Interactive Gameplay**: Play Sudoku with a clean, intuitive GUI.  
- **Puzzle Generator**: Instantly generate new, solvable Sudoku puzzles.  
- **Solver**: Stuck? Let the AI solver complete the puzzle for you.  
- **Answer Checker**: Check if your solution is correct at any time.  
- **Custom Buttons**: Easy-to-use controls for generating puzzles, solving, and checking answers.
- **Polished Visuals**: Custom fonts, colors, and an application icon for an enhanced experience.

---

## 📸 Screenshots

<img src="https://github.com/user-attachments/assets/5d261cfb-77fb-4dfb-8820-19ef6caccb81" alt="screenshot1" width="300"/>

<img src="https://github.com/user-attachments/assets/2862420a-dc16-4212-abd4-a957238f182a" alt="screenshot2" width="300"/>

---

## 🛠 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Suyash-Abhishek-Kumar/sudoku.git
cd sudoku
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

Run the main game file:

```bash
python gui.py
```

---

## 🎮 Controls

- **Generate**: Create a new Sudoku puzzle.
- **Solve**: Instantly solve the current puzzle.
- **Check**: Verify if your current solution is correct.
- **Input**: Click on a cell and type a number (1-9) to fill it in.

---

## 📁 Project Structure

```
sudoku/
├── gui.py            # Main file to launch the game (GUI)
├── solver.py         # Sudoku solver class (logic and algorithms)
├── generator.py      # Sudoku generator class (inherits from solver)
├── buttons.py        # Button class for GUI controls
├── colors.py         # Color definitions and utilities
├── sudoku_icon.png   # Application icon
├── requirements.txt  # List of required Python modules
├── fonts/            # Custom fonts used in the game
```

---

## 📦 Dependencies

- Python 3.x  
- `pygame` (and other modules listed in `requirements.txt`)

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

## 🧠 How It Works

- **Puzzle Generation**: Each new game generates a unique, solvable Sudoku puzzle.
- **Manual Play**: Fill in the grid with your answers using your mouse and keyboard.
- **Solver**: Use the "Solve" button to watch the AI instantly complete the puzzle.
- **Check Answers**: Use the "Check" button to validate your current solution.
- **Repeat**: Generate as many new puzzles as you like!

---

## 🎨 Customization

- **Colors & Fonts**: Modify `colors.py` and the `fonts/` folder to change the look and feel.
- **Buttons**: Add or modify buttons in `buttons.py` for more controls or features.

---

## 🙏 Acknowledgements

Created and maintained by **Suyash Abhishek Kumar**.

Enjoy solving and mastering Sudoku! 🧩✨
```
