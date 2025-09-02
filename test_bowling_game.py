import unittest
from bowling_game import Game


class MyTestCase(unittest.TestCase):
    def test_something(self):
        bowling_game = Game()
        output = bowling_game.something()
        self.assertTrue(output)  # add assertion here

if __name__ == '__main__':
    unittest.main()
