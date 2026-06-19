# Bowling Game Test Plan

## 1. Test Plan Overview
This test plan verifies correctness, reliability, and maintainability of the ten-pin bowling scoring backend in `bowling_game.py`.

## 2. Objectives
- Validate scoring logic against business rules for all 10 frames.
- Confirm strike and spare bonus behavior, including chained strikes.
- Validate 10th-frame bonus roll rules.
- Ensure invalid inputs and invalid game states are rejected with clear errors.
- Provide repeatable automated unit testing for regression detection.

## 3. Scope
In scope:
- `BowlingGame.roll()` input and rule validation.
- `BowlingGame.score()` for completed games.
- Internal frame behavior for strike/spare/open-frame scoring.

Out of scope:
- GUI behavior.
- File/database input.
- Multiplayer turn ordering.

## 4. Test Approach
- Technique: automated unit tests using Python `unittest`.
- Level: unit-level backend logic.
- Method: black-box tests from business rules + white-box tests for edge validation paths.
- Regression strategy: run full suite on every code change.

## 5. Test Environment
- OS: Windows
- Language: Python 3.x
- Test runner: `python test_bowling_game.py`

## 6. Entry and Exit Criteria
Entry criteria:
- Source code available and runnable.
- Business rules understood and documented.

Exit criteria:
- All designed tests executed.
- 100% pass rate for current suite.
- Identified defects fixed and retested.
- Updated docs and git history recorded.

## 7. Risk Assessment
High risk:
- Strike and spare bonus calculations can be off by one roll.
- 10th-frame logic can allow invalid extra rolls.

Medium risk:
- Incomplete game scoring may crash (index errors) instead of returning controlled feedback.

Low risk:
- Simple open-frame arithmetic.

Mitigation:
- Add targeted unit tests for each high-risk rule path.
- Enforce defensive validation in `roll()` and completion checks in `score()`.

## 8. Defect Management
- Log defects during test execution.
- Fix defect in smallest safe change.
- Add or update test to prevent recurrence.
- Re-run complete suite after each fix.

## 9. Coverage Summary
The final suite covers:
- Gutter game
- All ones
- Spare scoring
- Single strike scoring
- Consecutive strikes
- Perfect game (300)
- All spares (150)
- 10th-frame spare bonus
- 10th-frame strike bonus
- Invalid pins (<0, >10)
- Invalid frame totals
- Invalid 10th bonus combinations
- Rolling after game complete
- Scoring incomplete game

## 10. Traceability (Business Rule -> Tests)
- Basic frame scoring -> `test_gutter_game`, `test_all_ones`
- Spare bonus rule -> `test_spare`, `test_all_spares`, `test_tenth_frame_spare_bonus`
- Strike bonus rule -> `test_single_strike`, `test_consecutive_strikes`, `test_perfect_game`, `test_tenth_frame_strike_bonus`
- Validation and robustness -> remaining negative tests
