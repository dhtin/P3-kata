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

    def test_invalid_roll(self):
        with self.assertRaises(ValueError):
            self.bowling_game.roll(11)

    def test_non_integer_roll(self):
        with self.assertRaises(TypeError):
            self.bowling_game.roll(9.6)

    def test_non_number_roll(self):
        with self.assertRaises(TypeError):
            self.bowling_game.roll("nine")

    def test_two_rolls(self):
        self.bowling_game.roll(1)
        self.bowling_game.roll(5)
        output = self.bowling_game.score()
        self.assertEqual(6, output)

    def test_spare_bonus(self):
        self.bowling_game.roll(5)
        self.bowling_game.roll(5)
        self.bowling_game.roll(4)
        output = self.bowling_game.score()
        self.assertEqual(18, output)

    def test_roll_over_remaining_pins(self):
        self.bowling_game.roll(5)
        with self.assertRaises(ValueError):
            self.bowling_game.roll(7)

    def test_successive_spares(self):
        self.bowling_game.roll(5)
        self.bowling_game.roll(5)
        self.bowling_game.roll(5)
        self.bowling_game.roll(5)
        self.bowling_game.roll(4)
        output = self.bowling_game.score()
        self.assertEqual(29, output)

if __name__ == '__main__':
    unittest.main()
