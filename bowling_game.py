class Game:

    def __init__(self):
        self.rolls = []
        self.current_frame_rolls = []

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
        
    def score(self) -> int:
        total_score = 0
        roll_index = 0
        frame = 0

        while frame < 10 and roll_index < len(self.rolls):

            if self.rolls[roll_index] == 10: # Strike
                if roll_index + 2 < len(self.rolls):
                    total_score += 10 + self.rolls[roll_index + 1] + self.rolls[roll_index + 2]
                roll_index += 1
            elif roll_index + 1 < len(self.rolls) and self.rolls[roll_index] + self.rolls[roll_index + 1] == 10: # Spare
                if roll_index + 2 < len(self.rolls):
                    total_score += 10 + self.rolls[roll_index + 2]
                roll_index += 2
            elif roll_index + 1 < len(self.rolls):
                total_score += self.rolls[roll_index] + self.rolls[roll_index + 1]
                roll_index += 2
            else:
                total_score += self.rolls[roll_index]
                roll_index += 1
            
            frame += 1

        return total_score
