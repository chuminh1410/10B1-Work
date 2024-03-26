import tkinter as tk
from tkinter import messagebox

def print_board(board):
    # Function to print the Sudoku board
    for row in board:
        print(" ".join(map(str, row)))

def is_valid(board, row, col, num):
    # Check if placing 'num' at board[row][col] is valid
    # within the rules of Sudoku
    if num in board[row] or num in [board[i][col] for i in range(9)]:
        return False

    # Check the 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def find_empty_location(board):
    # Find an empty (0) cell in the Sudoku board
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None

def solve_sudoku_step_by_step(board, delay):
    # Backtracking algorithm to solve Sudoku with a delay between steps
    empty_location = find_empty_location(board)

    if not empty_location:
        return True  # All cells filled, puzzle solved

    row, col = empty_location

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            update_entry(row, col, num)
            root.update()
            root.after(delay)  # Introduce a delay between steps

            if solve_sudoku_step_by_step(board, delay):
                return True

            board[row][col] = 0
            update_entry(row, col, 0)
            root.update()
            root.after(delay)  # Introduce a delay between steps

    return False

def display_solution_with_delay(delay):
    # Function to display the Sudoku solution step by step with a delay
    if solve_sudoku_step_by_step(sudoku_board, delay):
        messagebox.showinfo("Sudoku Solved", "Sudoku puzzle solved!")
    else:
        messagebox.showinfo("No Solution", "No solution exists.")

def update_entry(row, col, value):
    # Function to update the Tkinter Entry widget
    entry_var[row][col].set(value)

# Example Sudoku board (0 represents empty cells)
sudoku_board = [
    [1, 0, 0, 0, 0, 7, 0, 9, 0],
    [0, 3, 0, 0, 0, 0, 0, 0, 8],
    [0, 0, 9, 6, 0, 0, 5, 0, 0],
    [0, 0, 5, 3, 0, 0, 9, 0, 0],
    [0, 1, 0, 0, 8, 0, 0, 0, 2],
    [6, 0, 0, 0, 0, 4, 0, 0, 0],
    [3, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 4, 0, 0, 0, 0, 0, 0, 7],
    [0, 0, 7, 0, 0, 0, 3, 0, 0]
]

# Initialize Tkinter
root = tk.Tk()
root.title("Sudoku Solver")

# Create a 9x9 grid of Entry widgets
entry_var = [[tk.StringVar() for _ in range(9)] for _ in range(9)]
entries = [[tk.Entry(root, width=2, font=('Arial', 16), textvariable=entry_var[i][j], justify='center') for j in range(9)] for i in range(9)]

# Place the Entry widgets on the grid
for i in range(9):
    for j in range(9):
        entries[i][j].grid(row=i, column=j)

# Button to display the solution with a delay
solve_button = tk.Button(root, text="Solve with Delay", command=lambda: display_solution_with_delay(200))
solve_button.grid(row=9, columnspan=9)

# Run the Tkinter main loop
root.mainloop()
