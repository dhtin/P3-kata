import unittest
from bowling_game import Game


class MyTestCase(unittest.TestCase):
    def test_starting_score(self):
        bowling_game = Game()
        output = bowling_game.score()
        self.assertEqual(0, output) 

if __name__ == '__main__':
    unittest.main()
