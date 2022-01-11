"""File defines a cell in the game grid and its possible conditions"""


class Cell:
    """The class defines the properties of the cell,
    its life status and character
    """

    def __init__(self):
        """Initialisation the 'dead' cell"""
        self.life_status = False

    def set_alive(self):
        """Ressurection of the cell"""
        self.life_status = True

    def set_dead(self):
        """Death of the cell"""
        self.life_status = False

    def is_alive(self) -> bool:
        """Checks if cell lives"""
        if self.life_status:
            return True
        return False

    def get_character(self) -> str:
        """Gets character due cell's life status"""
        if self.is_alive():
            return "X"
        return "-"
