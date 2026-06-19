import unittest
from bowling_game import BowlingGame


class TestBowlingGame(unittest.TestCase):
    def test_gutter_game(self):
        game = BowlingGame()
        for _ in range(20):
            game.roll(0)
        self.assertEqual(game.score(), 0)

    def test_all_ones(self):
        game = BowlingGame()
        for _ in range(20):
            game.roll(1)
        self.assertEqual(game.score(), 20)

    def test_spare(self):
        game = BowlingGame()
        game.roll(5)
        game.roll(5)
        game.roll(3)
        for _ in range(17):
            game.roll(0)
        self.assertEqual(game.score(), 16)

    def test_single_strike(self):
        game = BowlingGame()
        game.roll(10)
        game.roll(3)
        game.roll(4)
        for _ in range(16):
            game.roll(0)
        self.assertEqual(game.score(), 24)

    def test_consecutive_strikes(self):
        game = BowlingGame()
        game.roll(10)
        game.roll(10)
        game.roll(4)
        game.roll(2)
        for _ in range(14):
            game.roll(0)
        self.assertEqual(game.score(), 46)

    def test_perfect_game(self):
        game = BowlingGame()
        for _ in range(12):
            game.roll(10)
        self.assertEqual(game.score(), 300)

    def test_all_spares(self):
        game = BowlingGame()
        for _ in range(21):
            game.roll(5)
        self.assertEqual(game.score(), 150)

    def test_tenth_frame_spare_bonus(self):
        game = BowlingGame()
        for _ in range(18):
            game.roll(0)
        game.roll(7)
        game.roll(3)
        game.roll(9)
        self.assertEqual(game.score(), 19)

    def test_tenth_frame_strike_bonus(self):
        game = BowlingGame()
        for _ in range(18):
            game.roll(0)
        game.roll(10)
        game.roll(10)
        game.roll(10)
        self.assertEqual(game.score(), 30)

    def test_roll_rejects_negative_pins(self):
        game = BowlingGame()
        with self.assertRaises(ValueError):
            game.roll(-1)

    def test_roll_rejects_more_than_ten_pins(self):
        game = BowlingGame()
        with self.assertRaises(ValueError):
            game.roll(11)

    def test_regular_frame_cannot_exceed_ten(self):
        game = BowlingGame()
        game.roll(8)
        with self.assertRaises(ValueError):
            game.roll(3)

    def test_tenth_frame_bonus_must_be_valid_after_strike(self):
        game = BowlingGame()
        for _ in range(18):
            game.roll(0)
        game.roll(10)
        game.roll(7)
        with self.assertRaises(ValueError):
            game.roll(5)

    def test_cannot_roll_after_game_complete(self):
        game = BowlingGame()
        for _ in range(20):
            game.roll(0)
        with self.assertRaises(ValueError):
            game.roll(0)

    def test_score_rejects_incomplete_game(self):
        game = BowlingGame()
        for _ in range(10):
            game.roll(0)
        with self.assertRaises(ValueError):
            game.score()


if __name__ == "__main__":
    unittest.main()
