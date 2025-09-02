import unittest
from bowling_game import Game


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.bowling_game = Game()

    def test_starting_score(self):
        output = self.bowling_game.score()
        self.assertEqual(0, output) 

    def test_roll_1_pin_knocked(self):
        self.bowling_game.roll(1)
        output = self.bowling_game.score()
        self.assertEqual(1, output)

if __name__ == '__main__':
    unittest.main()
