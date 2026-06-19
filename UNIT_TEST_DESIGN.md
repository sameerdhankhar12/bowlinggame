# Unit Test Design

## Strategy
I designed the test suite to cover the core bowling rules first, then added edge and invalid-input tests to catch likely bugs.

## Test Cases

1. test_gutter_game
- Purpose: confirm score is 0 when no pins are knocked down.
- Data: 20 rolls of 0.
- Expected: 0.

2. test_all_ones
- Purpose: check simple open-frame accumulation.
- Data: 20 rolls of 1.
- Expected: 20.

3. test_spare
- Purpose: verify spare gets bonus from the next one roll.
- Data: 5, 5, 3, then zeros.
- Expected: 16.

4. test_single_strike
- Purpose: verify strike gets bonus from next two rolls.
- Data: 10, 3, 4, then zeros.
- Expected: 24.

5. test_consecutive_strikes
- Purpose: check correct scoring for back-to-back strikes.
- Data: 10, 10, 4, 2, then zeros.
- Expected: 46.

6. test_perfect_game
- Purpose: confirm maximum possible score boundary.
- Data: 12 strikes.
- Expected: 300.

7. test_all_spares
- Purpose: verify repeated spare behavior across a full game.
- Data: 21 rolls of 5.
- Expected: 150.

8. test_tenth_frame_spare_bonus
- Purpose: check 10th frame spare gives one bonus roll.
- Data: 18 zeros, 7, 3, 9.
- Expected: 19.

9. test_tenth_frame_strike_bonus
- Purpose: check 10th frame strike gives two bonus rolls.
- Data: 18 zeros, 10, 10, 10.
- Expected: 30.

10. test_roll_rejects_negative_pins
- Purpose: lower bound validation.
- Expected: ValueError.

11. test_roll_rejects_more_than_ten_pins
- Purpose: upper bound validation.
- Expected: ValueError.

12. test_regular_frame_cannot_exceed_ten
- Purpose: enforce frame pin-total rule in frames 1-9.
- Data: 8 then 3 in same frame.
- Expected: ValueError.

13. test_tenth_frame_bonus_must_be_valid_after_strike
- Purpose: enforce valid 10th frame bonus after a strike when second bonus is not strike.
- Data: 18 zeros, 10, 7, 5.
- Expected: ValueError.

14. test_cannot_roll_after_game_complete
- Purpose: prevent extra rolls after game completion.
- Data: 20 zeros then one extra roll.
- Expected: ValueError.

15. test_score_rejects_incomplete_game
- Purpose: ensure partial games are not scored.
- Data: 10 zeros only.
- Expected: ValueError from score().

## Coverage Result
- Total tests: 15
- Status: All passing
- Areas covered: normal scoring, edge boundaries, invalid input/state, and 10th frame rules
