# Evidence Log (Commands and Results)

## Environment
- Workspace: `C:/Users/Admin/assessment2`
- Date: 2026-06-19

## Test Execution
Command:
`python test_bowling_game.py`

Result:
- Ran 15 tests
- Status: OK

## PythonDoc Generation
Command:
`python -m pydoc -w bowling_game`

Result:
- Generated `bowling_game.html`

## Git Commit Evidence
Command:
`git log --oneline --decorate --date=iso --pretty="%h %ad %s" -n 5`

Captured output:
- `52afd20 2026-06-19 17:05:20 +1200 Add assessment documentation and generated PythonDoc output`
- `8098103 2026-06-19 17:04:38 +1200 Expand bowling unit tests to cover strikes spares tenth-frame and invalid input`
- `fa2df43 2026-06-19 17:04:38 +1200 Refactor bowling game with robust frame validation and clear scoring errors`

## Submission Package
Command:
`Compress-Archive -Path bowling_game.py,test_bowling_game.py,TEST_PLAN.md,UNIT_TEST_DESIGN.md,SUMMARY_REPORT.md,bowling_game.html -DestinationPath assessment2_submission.zip -Force`

Result:
- Created `assessment2_submission.zip`

## Screenshot Checklist (for tutor requirement)
Take screenshots showing date/time for:
1. `git log --oneline --decorate --date=iso --pretty="%h %ad %s" -n 10`
2. `python test_bowling_game.py`
3. `python -m pydoc -w bowling_game`
4. Folder view showing all deliverables and `assessment2_submission.zip`
