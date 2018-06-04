import time
from random import randint
import os


class Male:
    def __init__(self):
        self.life = randint(50, 100)
        self.power = randint(50, 100)
        self.agression = randint(50, 100)
        self.buti = randint(50, 100)
 
def read_grid(array):
    """
    Reads a given grid from a text file and sanitizes it to be used with the
    script.

    Keyword arguments:
    array -- the array into which the grid is loaded.

    Using python's with keyword the values of the grid are loaded into the array
    line by line. Once the values are loaded, it checks for the boundaries and sets
    them to -1
    """
    with open("grid.txt", 'r') as f:
        for line in f:
            temp = []
            for i in range(len(line) - 1):
                if line[i] == "*":
                    temp.append(1)
                elif line[i] == ".":
                    temp.append(0)
            array += [temp]
    print(array)

    for i in range(len(array)):
        for j in range(len(array[0])):
            if (i == 0 or j == 0 or (i == len(array) - 1) or (j == len(array[0]) - 1)):
                array[i][j] = -1

def init_grid(rows, cols, array):
    """
    Creates a array of the given size filling it with alive cells at random.

    Keyword arguments:
    rows -- number of rows of the array
    cols -- number of cols of the array
    array -- the array to fill with initial values.

    It iterates over all the values possible within the given range and sets the
   boundary values to -1. Then it fills the array with random alive(1) and dead (0)
    cells.
    """
    for i in range(rows):
        single_row = []
        for j in range(cols):
            if(i == 0 or j == 0 or (i == rows - 1) or ( j == cols - 1 )):
                single_row.append(-1)
            else:
                ran = random.randint(0,3)
                if ran == 0:
                    single_row.append(1)
                else:
                    single_row.append(0)
        array.append(single_row)

def process_neighbors(x, y, cur_gen):
    """
    Returns the value for a given cell in the next generation

    Keyword arguments:
    x -- row coordinate of the current cell
    y -- column coordinate of the current cell
    cur_gen -- array representing the current generation

    The function first iterates over all the neighbors of the given cell and
    sets the neighbor_count variable to the number of alive cells.
    """
    neighbor_count = 0

    # range() method in pyhton is exclusive, therefore to select the range between
    # x-1, x+1 we need to set the right interval of the range() method to x+2
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if not(i == x and j == y):
                if cur_gen[i][j] != -1:
                    # The count is incremented by whatever value is contained by the
                    # neighboring cell. This can either be 0 or 1, but the total will
                    # always reflect the number of cells alive.
                    neighbor_count += cur_gen[i][j]

    # Checking the 4 rules of game of life.
    if cur_gen[x][y] == 1 and neighbor_count < 2:
        return 0
    if cur_gen[x][y] == 1 and neighbor_count > 3:
        return 0
    if cur_gen[x][y] == 0 and neighbor_count == 3:
        return 1
    else:
        return cur_gen[x][y]

def process_next_gen(rows, cols, cur_gen, next_gen):
    """
    Keyword arguments:
    rows -- number of rows in the current generation array
    cols -- number of cols in the current generation array
    cur_gen -- array representing the current generation
    next_gen -- array representing the next generation

    Iterates over current generation array and sets the values for the
    cells in the array for the next generation by processing the neighbors
    of each cell in the current generation
    """
    for i in range(0, rows-1):
        for j in range(0, cols-1):
            next_gen[i][j] = process_neighbors(i, j, cur_gen)

def print_gen(rows, cols, cur_gen, gen):
    """
    Function to handle printing each generation

    Keyword arguments:
    rows -- number of rows in the array
    cols -- number of columns in the array
    cur_gen -- the array representing the current generation
    gen -- the number of the current generation

    Simple double for loop for iterating over contents of the array and
    printing the representation of alive cells (*) and dead cells (.) to
    STDOUT
    """
    os.system("clear")
    print("Conway's game of life simulation. Generation : " + str(gen + 1))

    for i in range(rows):
        for j in range(cols):
            if cur_gen[i][j] == -1:
                print("#", end = " ")
            elif cur_gen[i][j] == 1:
                print("*", end = " ")
            elif cur_gen[i][j] == 0:
                print(".", end = " ")
        print("\n")

def start_simulation(rows, cols, cur_gen, num_gen, delay):
    """
    This function runs the simulation.
    Keyword arguments:
    rows -- number of rows in the array
    cols -- the number of columns in the array
    cur_gen -- the array representing the current generation
    num_gen -- the number of generations the simulation has to run for
    delay -- time delay between the rendering of each generation

    This function creates a temp array of same size as the cur_gen array with
    random values. It prints the current generation,processses the next
    generation and swaps the current genration with the next one and repeats
    the process until it has finished running the simulation for num_gen
    generations
    """
    next_gen = []
    init_grid(rows, cols, next_gen)

    for gen in range(num_gen):
        print_gen(rows, cols, cur_gen, gen)
        process_next_gen(rows, cols, cur_gen, next_gen)
        time.sleep(delay)

        # Swapping this generation with the next
        cur_gen, next_gen = next_gen, cur_gen
    input("Simulation finished. Press any key to exit")

# Entry point for the script
if __name__ == '__main__':

    # Setting and declaring constatns
    _delay = 0.2
    _num_gen = 100
    _rows = 0
    _cols = 0

    print("Select choice : ")
    print("1: Read initial grid from file 'grid.txt'")
    print("2: Generate random grind of size 11X40")

    choice = int(input("Option: "))

    # Reading the grid from file
    if choice == 1:
        # temp list for stroring the grid from file
        this_gen = []
        read_grid(this_gen)
        _rows = len(this_gen)

        # All rows in the grid have the same number of columns
        _cols = len(this_gen[0])

        start_simulation(_rows, _cols, this_gen, _num_gen, _delay)
    elif choice == 2:
        # initalizing the starting grid of size 22X62.
        _rows = 50
        _cols = 62

        this_gen = []
        init_grid(_rows, _cols, this_gen)

        start_simulation(_rows, _cols, this_gen, _num_gen, _delay)