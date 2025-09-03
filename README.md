  #  🎳 Bowling Game
  
  [bowling game on kata-log.rocks](https://kata-log.rocks/bowling-game-kata)

# Bowling Rules
The game consists of 10 frames. In each frame the player has two rolls to knock down 10 pins. The score for the frame is the total number of pins knocked down, plus bonuses for strikes and spares.

A spare is when the player knocks down all 10 pins in two rolls. The bonus for that frame is the number of pins knocked down by the next roll.

A strike is when the player knocks down all 10 pins on his first roll. The frame is then completed with a single roll. The bonus for that frame is the value of the next two rolls.

In the tenth frame a player who rolls a spare or strike is allowed to roll the extra balls to complete the frame. However no more than three balls can be rolled in tenth frame.


# Requirements
Write a class Game that has two methods

void roll(int) is called each time the player rolls a ball. The argument is the number of pins knocked down.
int score() returns the total score for that game.

# Instructions for running the app
Run test_bowling_game.py to see test case output / run multiple instances of bowling games.
Or create your own bowling game object, use the roll() function to record rolls and use the score() function to return the score.

I decided to be pretty rigid with what inputs would be allowed and to raise errors for inputs that would go against a standard bowling game.
One area where I would ask for clarification on is what the behavior should be if a roll is made after the game is over, i.e. should it start a new game, raise an error, or not raise an error but also not update the score.

I completed the specifications for the kata, but with additional time it might be good to add some additional comments to bowling_game.py and create an interface of some sort for a user to directly interact with the bowling game.

-Mark
