class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        """
        Returns the maximum points that can be earned by solving questions.

        Args:
            questions: A 2D array of integers where questions[i] = [pointsi, brainpoweri].

        Returns:
            The maximum points that can be earned.
        """
        n = len(questions)
        @cache
        def go(index):
            if index >= n: return 0
            points, skip = questions[index]
            res = go(index + 1)
            res = max(res, points + go(index + skip + 1))
            return res
        return go(0)
