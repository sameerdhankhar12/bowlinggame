# Bowling Game Test Plan

## Overview
This test plan explains how I tested the bowling backend and checked that it follows the business rules for ten-pin bowling. The code under test is in bowling_game.py.

## What I wanted to confirm
- Scoring is correct across all 10 frames.
- Spare and strike bonuses are applied correctly.
- 10th frame bonus roll rules are handled correctly.
- Invalid input is rejected with clear errors.
- The tests can be rerun any time to catch regressions.

## Scope
In scope:
- BowlingGame.roll() validation and rule checking.
- BowlingGame.score() calculation for full games.
- Strike, spare, and open frame scoring behavior.

Out of scope:
- GUI features.
- File/database input.
- Multiplayer player order.

## Test approach
- I used automated unit tests with Python unittest.
- I focused on rule-based scenarios from the assignment brief.
- I included positive tests and negative/validation tests.
- I reran the full test suite after each meaningful code change.

## Test environment
- OS: Windows
- Language: Python 3.x
- Command used: python test_bowling_game.py

## Entry and exit criteria
Entry criteria:
- Source code is available and runs.
- Business rules are understood.

Exit criteria:
- All planned tests are executed.
- All tests pass.
- Any discovered bugs are fixed and retested.
- Documentation and commit history are updated.

## Risk assessment
High risk:
- Strike and spare bonus logic can easily be off by one roll.
- 10th frame bonus logic can allow invalid extra rolls.

Medium risk:
- Incomplete games might crash during scoring if not validated first.

Low risk:
- Basic open-frame addition.

Mitigation:
- Add targeted tests for high-risk scoring paths.
- Validate roll sequence in roll().
- Check game completion before allowing score().

## Defect handling process
- Run tests and note any failures.
- Identify the root cause.
- Apply smallest safe fix.
- Add/update tests so the issue does not return.
- Run all tests again.

## Coverage summary
My final suite covers:
- Gutter game
- All ones
- Spare scoring
- Single strike scoring
- Consecutive strikes
- Perfect game (300)
- All spares (150)
- 10th frame spare bonus
- 10th frame strike bonus
- Invalid pins (<0 and >10)
- Invalid frame totals
- Invalid 10th frame bonus combinations
- Rolling after game completion
- Scoring an incomplete game

## Traceability from business rules to tests
- Basic frame scoring: test_gutter_game, test_all_ones
- Spare rule: test_spare, test_all_spares, test_tenth_frame_spare_bonus
- Strike rule: test_single_strike, test_consecutive_strikes, test_perfect_game, test_tenth_frame_strike_bonus
- Validation and robustness: remaining negative tests
