"""
Generate a minesweeper grid (2x3) with 3 randomly-placed mines
"""
import random

def generate():
    # original idea:
    # mine1, mine2, mine3 = None, None, None
    # while len(set([mine1, mine2, mine3])) != 3: # get 3 distinct mines
    #     mine1 = random.randint(0, 5)
    #     mine2 = random.randint(0, 5)
    #     mine3 = random.randint(0, 5)
    # mines = [mine1, mine2, mine3]

    # optimal approach:
    mines = random.sample(range(0, 6), 3)
    grid = []
    coord = 0
    for _ in range(2):
        row = []
        for _ in range(3):
            if coord in mines:
                row.append("X")
            else:
                row.append("O")
            print(coord)
            coord += 1
        grid.append(row)
    return grid


def display(grid):
    for row in grid:
        print(row)


grid = generate()
display(grid)