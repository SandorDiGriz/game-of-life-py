"""File defines a game grid and its transformations"""


from cell import Cell
import random


class Grid:
    """Class implements functions for creating the board,
    drawing it and changing its dwellers
    """

    def __init__(self, rows: int, columns: int, birth_chance=25, grid=None):
        """Initialisation of grid's size and probability of cell birth"""
        # Adding borders to make the whole board playable
        self.rows = rows + 2
        self.columns = columns + 2
        self.birth_chance = birth_chance
        # Generating the grid with the defined cell objects
        if grid is None:
            grid = [
                [Cell() for elem in range(self.columns)] for row in range(self.rows)
            ]
        self.grid = grid

    def build_grid(self) -> list[list[object]]:
        """Creation of grid and and random cell colonization"""
        row_index = 0
        for row in self.grid:
            elem_index = 0
            # Skipping borders
            if row_index == 0 or row_index == len(self.grid) - 1:
                row_index += 1
                continue
            row_index += 1
            for elem in row:
                # Processing the side borders
                if elem_index == 0 or elem_index == len(self.grid[0]) - 1:
                    elem_index += 1
                    continue
                # Generating the percentage probability of cell birth
                if self.birth_chance >= random.randint(1, 100):
                    elem.set_alive()
                elem_index += 1

    def print_grid(self):
        """Prints the grid line by line and cuts borders"""
        row_index = 0
        for row in self.grid:
            elem_index = 0
            # Skipping borders
            if row_index == 0 or row_index == len(self.grid) - 1:
                row_index += 1
                continue
            row_index += 1
            for elem in row:
                # Processing the side borders
                if elem_index == 0 or elem_index == len(self.grid[0]) - 1:
                    elem_index += 1
                    continue
                # Printing the grid by lines
                print(elem.get_character(), end="")
                elem_index += 1
            print()

    def get_neighbors(self, row_index, elem_index):
        neighbors = []

        operands = [1, 0, -1]
        for x in operands:
            for y in operands:
                if x == 0 and y == 0:
                    continue
                neighbors.append(
                    self.grid[row_index + x][elem_index + y].get_character()
                )
        return neighbors

    @staticmethod
    def new_cell(current_cell: object, neighbors: list) -> bool:
        """Creation of a new generation of cells

        Args:
            current_cell (object): each element from the grid
            neighbors (list): list of cell neighbors

        Returns:
            [bool]: Is cell alive
        """
        count = 0
        # If living neighbors more then 3 cell dies
        # If cell is dead and has 3 living neighbors it lives
        # If cell is alive and has 2 or 3 living neighbors it survives
        for neighbor in neighbors:
            if neighbor == "X":
                count += 1
        if current_cell == "X" and count in (2, 3):
            return True
        if current_cell == "-" and count == 3:
            return True
        else:
            return False

    def evolve(self) -> list[list[object]]:
        """Gets the new cells generation"""
        row_index = 0
        living_cells = []
        dying_cells = []
        for row in self.grid:
            elem_index = 0
            # Skipping borders
            if row_index == 0 or row_index == len(self.grid) - 1:
                row_index += 1
                continue
            row_index += 1
            for elem in row:
                # Processing the side borders
                if elem_index == 0 or elem_index == len(self.grid[0]) - 1:
                    elem_index += 1
                    continue
                # Collecting cells life status for the next generation
                if self.new_cell(
                    elem.get_character(), self.get_neighbors(row_index - 1, elem_index)
                ):
                    living_cells.append(elem)
                else:
                    dying_cells.append(elem)
                elem_index += 1
        # Evolving cells
        self.change_generation(living_cells, dying_cells)

    def change_generation(self, living_cells: list, dying_cells: list):
        """Evolves cells according to the life status"""
        for cell in living_cells:
            cell.set_alive()
        for cell in dying_cells:
            cell.set_dead()
