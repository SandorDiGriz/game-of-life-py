from cell import Cell 
import random

class Grid:
    def __init__(self, rows: int, elems: int, grid=None, birth_chance=25):
        self.rows = rows
        self.elems = elems
        self.birth_chance = birth_chance
        if grid is None:
            grid = [[Cell() for elem in range(self.elems)] for row in range(self.rows)]
        self.grid = grid

    def build_grid(self) -> list[str]:
        
        for row in self.grid:
            for elem in row:
                if self.birth_chance >= random.randint(1, 100):
                    elem.set_alive()
        self

    def print_grid(self):
        for row in self.grid:
            for elem in row:
                print(elem.get_character(), end='')
            print()


a = Grid(3, 4)
a.build_grid()
a.print_grid()
# print(random.randint(1, 100))