"""Bowling game scorer and validator for ten-pin rules."""


class BowlingGame:
    """Model a single ten-pin bowling game.

    Rolls are recorded with :meth:`roll`, and total score is computed with
    :meth:`score` once a full game has been completed.
    """

    def __init__(self):
        """Initialise an empty game."""
        self.rolls = []

    def roll(self, pins):
        """Record one roll after validating ten-pin frame constraints.

        Args:
            pins (int): Number of pins knocked down in this roll.

        Raises:
            ValueError: If pins are outside 0..10, if a frame exceeds 10 pins,
                or if trying to roll after the game is complete.
        """
        candidate_rolls = self.rolls + [pins]
        self._validate_roll_sequence(candidate_rolls)
        self.rolls.append(pins)

    def score(self):
        """Calculate the total score for a completed game.

        Returns:
            int: Total game score across all ten frames.

        Raises:
            ValueError: If called before a full valid game has been entered.
        """
        if not self.is_complete():
            raise ValueError("Cannot score an incomplete game")

        total = 0
        frame_index = 0

        for _ in range(10):
            if self._is_strike(frame_index):
                total += 10 + self._strike_bonus(frame_index)
                frame_index += 1
            elif self._is_spare(frame_index):
                total += 10 + self._spare_bonus(frame_index)
                frame_index += 2
            else:
                total += self.rolls[frame_index] + self.rolls[frame_index + 1]
                frame_index += 2

        return total

    def is_complete(self):
        """Return True when the game has exactly ten complete frames."""
        return self._validate_roll_sequence(self.rolls, require_complete=True)

    def _validate_roll_sequence(self, sequence, require_complete=False):
        """Validate a full or partial roll sequence.

        Args:
            sequence (list[int]): Rolls to validate.
            require_complete (bool): If True, sequence must represent a full
                completed game. If False, partial but valid progress is allowed.

        Returns:
            bool: True when valid and complete in ``require_complete`` mode,
                otherwise True for any valid partial/complete sequence.

        Raises:
            ValueError: If any roll violates bowling rules.
        """
        for pins in sequence:
            if pins < 0 or pins > 10:
                raise ValueError("Pins must be between 0 and 10")

        index = 0

        for _ in range(9):
            if index >= len(sequence):
                return not require_complete

            first = sequence[index]
            if first == 10:
                index += 1
                continue

            if index + 1 >= len(sequence):
                return not require_complete

            second = sequence[index + 1]
            if first + second > 10:
                raise ValueError("Frame pin count cannot exceed 10")

            index += 2

        remaining = sequence[index:]

        if not remaining:
            return not require_complete

        if len(remaining) > 3:
            raise ValueError("Cannot roll after game is complete")

        first = remaining[0]

        if len(remaining) == 1:
            return not require_complete

        second = remaining[1]
        if first != 10 and first + second > 10:
            raise ValueError("Frame pin count cannot exceed 10")

        bonus_awarded = first == 10 or (first + second == 10)

        if not bonus_awarded:
            if len(remaining) > 2:
                raise ValueError("Cannot roll after game is complete")
            return len(remaining) == 2 if require_complete else True

        if len(remaining) == 2:
            return not require_complete

        third = remaining[2]
        if first == 10 and second != 10 and second + third > 10:
            raise ValueError("Bonus rolls after strike must be valid")

        return True

    def _is_strike(self, frame_index):
        """Return True when the frame at ``frame_index`` is a strike."""
        return self.rolls[frame_index] == 10

    def _is_spare(self, frame_index):
        """Return True when two rolls in frame sum to ten."""
        return self.rolls[frame_index] + self.rolls[frame_index + 1] == 10

    def _strike_bonus(self, frame_index):
        """Return the next two rolls counted as strike bonus."""
        return self.rolls[frame_index + 1] + self.rolls[frame_index + 2]

    def _spare_bonus(self, frame_index):
        """Return the next roll counted as spare bonus."""
        return self.rolls[frame_index + 2]
