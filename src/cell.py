class Cell:
    def __init__(self, life_status=None):
        if life_status is None:
            life_status is False
        self.life_status = life_status
    
    def set_alive(self):
        self.life_status = True
    
    def set_dead(self):
        self.life_status = False
        
    def is_alive(self):
        if self.life_status:
            return True
        return False
    
    def get_character(self):
        if self.is_alive():
            return "X"
        return "-"
        
