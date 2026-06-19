# Summary Report - Bowling Game QA and Maintenance

## Project Summary
This project tested and improved the bowling game backend using a structured QA workflow: test planning, unit test design, defect fixing, refactoring, documentation, and version control.

## Testing Approach
A formal test plan was created first to define scope, risk, and methodology. Testing focused on ten-pin scoring rules from the business requirements, especially high-risk logic around strike/spare bonuses and 10th-frame behavior.

Automated unit tests were implemented using `unittest`. The suite includes normal scenarios, edge cases, and invalid input/state validation. Final result: 15 tests passing.

## Debugging Findings and Fixes
Issue 1: Incomplete game scoring could fail with index errors.
- Cause: `score()` assumed enough rolls always existed.
- Fix: Added completion check and clear `ValueError` for incomplete games.

Issue 2: Invalid frame totals were accepted (e.g., 8 + 3 in one frame).
- Cause: No frame-level roll validation.
- Fix: Added roll-sequence validation in `roll()`.

Issue 3: Invalid extra rolls and invalid 10th bonus combinations were not prevented.
- Cause: No game-state validation for completion and 10th-frame constraints.
- Fix: Added explicit checks for game completion and valid 10th-frame bonus logic.

## Refactoring Performed
Refactor 1: Introduced `is_complete()` and `_validate_roll_sequence()`.
- Improvement: Centralized rule validation, reduced hidden failure modes, improved readability.

Refactor 2: Improved naming and formatting.
- Improvement: Better maintainability and easier code review.

Refactor 3: Added comprehensive Python docstrings.
- Improvement: Better developer onboarding and API understanding.

## Documentation Produced
- Python docstrings in source code (`bowling_game.py`).
- Generated PythonDoc HTML output (`bowling_game.html`).
- Test plan (`TEST_PLAN.md`).
- Unit test design (`UNIT_TEST_DESIGN.md`).
- This summary report (`SUMMARY_REPORT.md`).

## Version Control Usage
Changes were committed in logical steps:
1. Refactor and bug-fix commit for validation/scoring robustness.
2. Unit test expansion commit for rule and edge-case coverage.
3. Documentation commit for assessment deliverables.

Repository link: Add your remote repository URL here before submission.

## Recommendations
- Add CI to run tests on each commit.
- Add branch protection and pull-request checks if collaborating.
- Extend tests for mutation testing/property-based checks in future iterations.
