# Summary Report - Bowling Game QA and Maintenance

## Project Summary
In this project, I tested and improved the bowling game backend using a full QA process. I created a test plan, designed and ran unit tests, fixed issues found during testing, refactored parts of the code, documented the code, and tracked changes with Git.

## Testing Approach
I started with a test plan so I could define scope, risk, and test method before making code changes. I focused on the ten-pin bowling rules from the brief, especially strike/spare bonus logic and 10th frame behavior because those areas have the highest chance of errors.

I implemented automated unit tests using unittest. The suite covers normal cases, edge cases, and invalid input/state behavior. Final result: 15 tests passing.

## Debugging Findings and Fixes
Issue 1: Incomplete game scoring could fail with index errors.
- Cause: score() assumed enough rolls were already present.
- Fix: I added a game completion check and raised ValueError for incomplete games.

Issue 2: Invalid frame totals were accepted (e.g., 8 + 3 in one frame).
- Cause: No frame-level roll validation.
- Fix: I added roll-sequence validation in roll().

Issue 3: Invalid extra rolls and invalid 10th bonus combinations were not prevented.
- Cause: No game-state validation for completion and 10th-frame constraints.
- Fix: I added checks for game completion and valid 10th frame bonus rules.

## Refactoring Performed
Refactor 1: Added is_complete() and _validate_roll_sequence().
- Improvement: validation is centralized, easier to read, and easier to maintain.

Refactor 2: Improved naming and formatting.
- Improvement: Better maintainability and easier code review.

Refactor 3: Added comprehensive Python docstrings.
- Improvement: Better developer onboarding and API understanding.

## What I learned
- Writing tests first (or early) helped me find logic gaps quickly.
- Most bugs were around rule boundaries, not basic arithmetic.
- Small, focused commits made it easier to track and explain each change.

## Documentation Produced
- Python docstrings in the source code (bowling_game.py).
- Generated PythonDoc HTML output (bowling_game.html).
- Test plan (TEST_PLAN.md).
- Unit test design (UNIT_TEST_DESIGN.md).
- Summary report (SUMMARY_REPORT.md).

## Version Control Usage
I committed changes in logical steps:
1. Refactor and bug-fix commit for validation/scoring robustness.
2. Unit test expansion commit for rule and edge-case coverage.
3. Documentation commit for assessment deliverables.

Repository link: https://github.com/sameerdhankhar12/bowlinggame

## Recommendations
- Add CI to run tests on each commit.
- Add branch protection and pull-request checks if collaborating.
- Extend tests for mutation testing/property-based checks in future iterations.
