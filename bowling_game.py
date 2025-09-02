class Game:

    def __init__(self):
        self.rolls = []
        self.current_frame_rolls = []
        self.total_score = 0

    def roll(self, pins: int):
        if not isinstance(pins, int):
            raise TypeError("Pins must be an int")
        
        if pins < 0 or pins > 10:
            raise ValueError("Invalid number of pins")
        
        if len(self.current_frame_rolls) == 1:
            if self.current_frame_rolls[0] + pins > 10:
                raise ValueError("Total pins in a frame can not exceed 10")


        self.current_frame_rolls.append(pins)
        self.rolls.append(pins)

        if len(self.current_frame_rolls) == 2 or pins == 10:
            self.current_frame_rolls = []

        self.total_score += pins
        self._handle_spare_bonus()

    def _handle_spare_bonus(self):
        if len(self.rolls) > 2:
            if self.rolls[-3] + self.rolls[-2] == 10:
                    self.total_score += self.rolls[-1]
        

    def score(self) -> int:
        return self.total_score
