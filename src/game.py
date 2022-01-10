from grid import Grid

class Game:
    def __init__(self, rows, columns, mode="auto", birth_chance=25, generations_limit=250):
        self.rows = rows
        self.columns = columns
        self.mode = mode
        self.birthchace = birth_chance
        self.generations_limit = generations_limit
        
    def run(self):
        
        grid = Grid(self.rows, self.columns)
        grid.build_grid()
        game_over = False
        if self.mode == "auto":
            while not game_over:
                grid.print_grid()
                for i in range(self.generations_limit):
                    print()
                    grid.evolve()
                    grid.print_grid()
                game_over = False
        else:
            while not game_over:
                grid.print_grid()
                if input() == "g":
                    grid.evolve()
                    grid.print_grid()
                game_over = False

