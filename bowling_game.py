class Game:

    def __init__(self):
        self.total_score = 0

    def roll(self, pins: int):
        if not isinstance(pins, int):
            raise TypeError("Pins must be an int")
        
        if pins < 0 or pins > 10:
            raise ValueError("Invalid number of pins")
        
        self.total_score += pins

    def score(self) -> int:
        return self.total_score
