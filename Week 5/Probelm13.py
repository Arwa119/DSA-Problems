grid = []

def add_row(row):
    grid.append(row)
    print(f"Row {row} added successfully.")

def add_column(column):
    if len(grid) == 0:
        print("Grid is empty. Add rows first.")
        return
    
    if len(column) != len(grid):
        print("Column length must match the number of rows.")
        return
    
    for i in range(len(grid)):
        grid[i].append(column[i])
    print(f"Column {column} added successfully.")

def display_grid():
    if not grid:
        print("The grid is empty.")
        return
    print("Current grid:")
    for row in grid:
        print(row)

def sum_grid():
    total_sum = 0
    for row in grid:
        total_sum += sum(row)
    return total_sum

if __name__ == "__main__":
    add_row([0, 2, 8])
    add_row([3, 1, 4])
    display_grid()

    add_column([20, 19])
    display_grid()

    total = sum_grid()
    print(f"Sum of all elements in the grid: {total}")
