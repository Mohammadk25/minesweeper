import random

def load_bombs_from_file(filename):
    bombs = {}
    with open(filename, 'r') as file:
        for line in file:
            x, y = map(int, line.strip().split(','))
            bombs[(x, y)] = 'B'
    return bombs

def place_bombs_randomly(size, bomb_count):
    bombs = {}
    while len(bombs) < bomb_count:
        x, y = random.randint(0, size - 1), random.randint(0, size - 1)
        if (x, y) not in bombs:
            bombs[(x, y)] = 'B'
    return bombs

def initialize_grid(size, bombs):
    grid = [['*' for _ in range(size)] for _ in range(size)]
    for x, y in bombs:
        grid[x][y] = 'B'  
    return grid

def display_grid(grid, reveal_bombs=False):
    size = len(grid)

    # Tens header 
    tens_header = '          ' + ''.join(['   ' if i < 9 else '   ' + str((i + 1) // 10) for i in range(size)])

    # Units header 
    units_header = ' ' + ''.join(['   ' + str((i + 1) % 10) if i < 9 else '   ' + str((i + 1) % 10) for i in range(size)])

    divider = '----' + '----' * size

    # Print the headers
    print(tens_header.rstrip())
    print(units_header.rstrip())
    print(divider)

    for i, row in enumerate(grid):
     row_display = chr(65 + i) + ' | '
     for cell in row:
        if cell == 'B' and not reveal_bombs:
            row_display += '* | '  
        else:
           row_display += f'{cell} | '
     print(row_display.rstrip())
     print(divider)

def move_bombs(grid, bomb_count):
    new_bombs = {}
    revealed_cells = [(x, y) for x in range(len(grid)) for y in range(len(grid)) if grid[x][y] != '*']

    while len(new_bombs) < bomb_count:
        x, y = random.randint(0, len(grid) - 1), random.randint(0, len(grid) - 1)
        if (x, y) not in new_bombs and (x, y) not in revealed_cells:
            new_bombs[(x, y)] = 'B'

    return new_bombs

def recalculate_adjacent_bombs(grid, bombs):
    for x in range(len(grid)):
        for y in range(len(grid)):
            if grid[x][y] != '*':  
                adjacent_bombs = sum((nx, ny) in bombs for nx in range(x-1, x+2) for ny in range(y-1, y+2) 
                                     if 0 <= nx < len(grid) and 0 <= ny < len(grid) and (nx, ny) != (x, y))
                grid[x][y] = str(adjacent_bombs) if adjacent_bombs > 0 else ' '

def count_non_bomb_cells(grid, bombs):
    return sum(1 for x in range(len(grid)) for y in range(len(grid)) if grid[x][y] == '*' and (x, y) not in bombs)

def reveal_adjacent_cells(grid, bombs, row, col):
    for nx in range(max(0, row - 1), min(len(grid), row + 2)):
        for ny in range(max(0, col - 1), min(len(grid), col + 2)):
            if (nx, ny) != (row, col) and grid[nx][ny] == '*' and (nx, ny) not in bombs:
                adjacent_bombs = sum((mx, my) in bombs for mx in range(nx-1, nx+2) 
                                     for my in range(ny-1, ny+2) 
                                     if 0 <= mx < len(grid) and 0 <= my < len(grid) and (mx, my) != (nx, ny))
                grid[nx][ny] = str(adjacent_bombs) if adjacent_bombs > 0 else ' '

def reveal_cell(grid, bombs, row, col):
    # Check if the cell is a bomb
    if (row, col) in bombs:
        return True, False

    # Calculate the number of adjacent bombs
    adjacent_bombs = sum((nx, ny) in bombs for nx in range(row-1, row+2) 
                         for ny in range(col-1, col+2) 
                         if 0 <= nx < len(grid) and 0 <= ny < len(grid) and (nx, ny) != (row, col))

    grid[row][col] = str(adjacent_bombs) if adjacent_bombs > 0 else ' '
   
    if adjacent_bombs == 0:
     reveal_adjacent_cells(grid, bombs, row, col)
    return False, adjacent_bombs == 0

def check_win(grid, bombs):
    return all(grid[x][y] != '*' for x in range(len(grid)) for y in range(len(grid)) if (x, y) not in bombs)
   

def display_grid_with_bombs(grid, bombs):
    size = len(grid)
 # Tens header 
    tens_header = '          ' + ''.join(['   ' if i < 9 else '   ' + str((i + 1) // 10) for i in range(size)])

    # Units header 
    units_header = ' ' + ''.join(['   ' + str((i + 1) % 10) if i < 9 else '   ' + str((i + 1) % 10) for i in range(size)])

    divider = '----' + '----' * size

    # Print the headers
    print(tens_header.rstrip())
    print(units_header.rstrip())
    print(divider)

    for i, row in enumerate(grid):
        row_display = chr(65 + i) + ' | '
        for j, cell in enumerate(row):
            if (i, j) in bombs:
                cell_display = 'B'
            elif cell == '*':
                cell_display = '*'
            else:
                cell_display = cell
            row_display += f'{cell_display} | '
        print(row_display)
        print(divider)


def reveal_adjacent_cells2(grid, bombs, row, col):
    for nx in range(max(0, row - 1), min(len(grid), row + 2)):
        for ny in range(max(0, col - 1), min(len(grid), col + 2)):
            if (nx, ny) != (row, col) and grid[nx][ny] == '*' and (nx, ny) not in bombs:
                adjacent_bombs = sum((mx, my) in bombs for mx in range(nx-1, nx+2) 
                                     for my in range(ny-1, ny+2) 
                                     if 0 <= mx < len(grid) and 0 <= my < len(grid) and (mx, my) != (nx, ny))
                grid[nx][ny] = str(adjacent_bombs) if adjacent_bombs > 0 else ' '

def reveal_cell_level_2(grid, bombs, previous_bombs, row, col):
    # Check if the cell was a bomb in the previous configuration
    if (row, col) in previous_bombs:
        return True, False  # Hit a bomb from the previous configuration

    # Calculate the number of adjacent bombs based on current bomb configuration
    adjacent_bombs = sum((nx, ny) in bombs for nx in range(row-1, row+2) 
                         for ny in range(col-1, col+2) 
                         if 0 <= nx < len(grid) and 0 <= ny < len(grid) and (nx, ny) != (row, col))

    grid[row][col] = str(adjacent_bombs) if adjacent_bombs > 0 else ' '

    return False, adjacent_bombs == 0

def recalculate_adjacent_bombs_level_2(grid, bombs):
    for x in range(len(grid)):
        for y in range(len(grid)):
            # Only recalculate for non-bomb and non-flagged cells
            if grid[x][y] not in ['B', '*']:
                adjacent_bombs = sum((nx, ny) in bombs for nx in range(x-1, x+2) 
                                     for ny in range(y-1, y+2) 
                                     if 0 <= nx < len(grid) and 0 <= ny < len(grid) and (nx, ny) != (x, y))
                grid[x][y] = str(adjacent_bombs) if adjacent_bombs > 0 else ' '


def main():
    print("###\nWelcome in the minesweeper game.\nTry to find all cases without bombs.\nGood Luck!\n###")

    while True:
        try:
            difficulty = int(input("Choose your difficulty.\nFor project Grid press, easy press 0, medium press 1, hard press 2: "))
            if difficulty not in [0, 1, 2]:
                raise ValueError
            break
        except ValueError:
            print("Invalid difficulty. Please enter 0, 1, or 2.")

    while True:
        try:
            size = 9 if difficulty == 0 else int(input("Enter grid size: "))
            if size <= 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer for the grid size.")

    if difficulty == 0:
        bombs = load_bombs_from_file('bombs.txt')
    else:
        # Calculate bomb count for medium and difficult levels
       bomb_count = int((size * size) / 5)
       bomb_count = max(1, bomb_count)  # Ensure at least one bomb
       bombs = place_bombs_randomly(size, bomb_count)

    grid = initialize_grid(size, bombs)
    previous_bombs = bombs.copy() if difficulty == 2 else {}  # Initialize previous_bombs for level 2

    print(f"We planted {len(bombs)} bombs. Good luck!")
    rounds = 1

    while True:
        cases_to_find = count_non_bomb_cells(grid, bombs)
        print(f"### Round {rounds}")
        display_grid(grid)
        print(f"--> {cases_to_find} cases to find.")

        valid_input = False
        while not valid_input:
            row_input = input(f"Choose your line (A-{chr(65 + size - 1)}): ").upper()
            if len(row_input) == 1 and 'A' <= row_input <= chr(65 + size - 1):
                valid_input = True
                row = ord(row_input) - 65
            else:
                print(f"Invalid input. Please enter a single letter from A to {chr(65 + size - 1)}.")

        valid_input = False
        while not valid_input:
            col_input = input(f"Choose your column (1-{size}): ")
            if col_input.isdigit() and 1 <= int(col_input) <= size:
                valid_input = True
                col = int(col_input) - 1
            else:
                print(f"Invalid input. Please enter a number from 1 to {size}.")

           
        if difficulty == 2:
        # Upecialized reveal function for level 2
           hit_bomb, _ = reveal_cell_level_2(grid, bombs, previous_bombs, row, col) 
           reveal_adjacent_cells2(grid, bombs, row, col)
        else:
          # standard reveal function for other levels
          hit_bomb, _ = reveal_cell(grid, bombs, row, col)

         # Check if the player won
        if check_win(grid, bombs):
          print("Congratulations! You've won!")
          break

        if difficulty == 2 and not hit_bomb:
          # Update previous_bombs and move bombs for level 2
          previous_bombs = bombs.copy()
          bombs = move_bombs(grid, len(bombs))

          # Recalculate the grid AFTER moving bombs
          recalculate_adjacent_bombs_level_2(grid, bombs)

          print("--> You successfully passed this step, a new grid is now generated!")
          print(previous_bombs)  # Print the previous bomb positions

        if hit_bomb:
          print("BOUM, You lost!")
          if difficulty == 2:
           recalculate_adjacent_bombs_level_2(grid, bombs)
           display_grid_with_bombs(grid, previous_bombs)  # Use previous bomb locations
          else:
           display_grid_with_bombs(grid, bombs)  # For other levels, use current bombs
          break  # Display the grid with bombs
          
    rounds += 1

if __name__ == "__main__":
    main()
    



