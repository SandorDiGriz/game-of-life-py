from cell import Cell 
import random

class Grid:
    def __init__(self, rows: int, elems: int, birth_chance=25, grid=None):
        self.rows = rows + 2
        self.elems = elems + 2
        self.birth_chance = birth_chance
        if grid is None:
            grid = [[Cell() for elem in range(self.elems)] for row in range(self.rows)]
        self.grid = grid

    def build_grid(self) -> list[str]:
        row_index = 0 
        for row in self.grid:
            elem_index = 0
            
            if row_index == 0 or row_index == len(self.grid) - 1:
                row_index += 1
                continue
            
            row_index += 1
            for elem in row:
                
                if elem_index == 0 or elem_index == len(self.grid[0]) - 1:
                    elem_index += 1
                    continue
                
                if self.birth_chance >= random.randint(1, 100):
                    elem.set_alive()
                
                # print(row_index - 1, elem_index, elem.get_character())
                # print(self.grid[row_index - 1][elem_index].get_character())
                elem_index += 1

    def print_grid(self):
        row_index = 0 
        for row in self.grid:
            elem_index = 0
            
            if row_index == 0 or row_index == len(self.grid) - 1:
                row_index += 1
                continue
            
            row_index += 1
            for elem in row:
                
                if elem_index == 0 or elem_index == len(self.grid[0]) - 1:
                    elem_index += 1
                    continue
                
                print(elem.get_character(), end='')
                elem_index += 1
            print()


    def get_neighbors(self, row_index, elem_index):
        neighbors = []
        
        operands = [1, 0, -1]
        for x in operands:
            for y in operands:
                if x == 0 and y == 0:
                    continue
                neighbors.append(self.grid[row_index + x][elem_index + y].get_character())
        return neighbors

    @staticmethod
    def new_cell(current_cell, neighbors):
        count = 0
        for neighbor in neighbors:
            if neighbor == "X":
                count += 1
        if current_cell == "X" and count in (2, 3):
            return True
        if current_cell == "-" and count == 3:
            return True
        else:
            return False
    
    def evolve(self):
        row_index = 0
        living_cells = []
        dying_cells = []
        for row in self.grid:
            elem_index = 0
            
            if row_index == 0 or row_index == len(self.grid) - 1:
                row_index += 1
                continue
            
            row_index += 1
            for elem in row:
                
                if elem_index == 0 or elem_index == len(self.grid[0]) - 1:
                    elem_index += 1
                    continue
                
                #print(self.new_cell(elem, self.get_neighbors(row_index - 1, elem_index)))
                if self.new_cell(elem.get_character(), self.get_neighbors(row_index - 1, elem_index)):
                    living_cells.append(elem)
                else:
                    dying_cells.append(elem)
                    
                elem_index += 1
        self.change_generation(living_cells, dying_cells)
    
    def change_generation(self, living_cells, dying_cells):
        for cell in living_cells:
            cell.set_alive()
        for cell in dying_cells:
            cell.set_dead()


# a = Grid(3, 3, 50)
# # a.build_grid()
# # a.print_grid()
# # a.evolve()
# # print()
# # a.print_grid()
