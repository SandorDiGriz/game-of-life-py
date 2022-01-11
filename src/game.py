"""File contols the course of the game"""

from grid import Grid


class Game:
    """
    Class launches the gameplay

    Attributes
    ----------
    rows (int): Number of grid's rows
    columns (int): Number of grid's columns
    mode (str, optional): Mode of cell generation change ('auto' | 'one-step'). Defaults to "auto".
    birth_chance (int, optional): [Percentage probability of a cell being born. Defaults to 25.
    generations_limit (int, optional): Maximum number of generations. Defaults to 250.
    """

    def __init__(
        self,
        rows: int,
        columns: int,
        mode="auto",
        birth_chance=25,
        generations_limit=250,
    ):
        """Initialisation of all game parameters"""
        self.rows = rows
        self.columns = columns
        self.mode = mode
        self.birthchance = birth_chance
        self.generations_limit = generations_limit

    def run(self):
        """Controls the two modes of the game"""
        grid = Grid(self.rows, self.columns, self.birthchance)
        grid.build_grid()
        game_over = False
        # Executing first mode
        if self.mode == "auto":
            while not game_over:
                grid.print_grid()
                for _ in range(self.generations_limit):
                    print()
                    grid.evolve()
                    grid.print_grid()
                game_over = True
        # Executing second mode
        elif self.mode == "one-step":
            while not game_over:
                grid.print_grid()
                print("Type 'g' to breed a new generation or anything else to quit")
                if input() == "g":
                    grid.evolve()
                    grid.print_grid()
                    continue
                game_over = True
