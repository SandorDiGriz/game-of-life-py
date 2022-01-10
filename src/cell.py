import typing

class Cell:
    def __init__(self):
        self.life_status = False
    
    def set_alive(self):
        self.life_status = True
    
    def set_dead(self):
        self.life_status = False
        
    def is_alive(self) -> bool:
        if self.life_status:
            return True
        return False
    
    def get_character(self) -> str: 
        if self.is_alive():
            return "X"
        return "-"
        
