class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        return letters[bisect_right(letters, target)] if bisect_right(letters, target) < len(letters) else letters[0]