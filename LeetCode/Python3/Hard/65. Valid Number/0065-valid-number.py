class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        if not s:
            return False
        dot_seen = False
        e_seen = False
        num_seen = False
        num_after_e = False
        for i, char in enumerate(s):
            if char == '+' or char == '-':
                if i > 0 and s[i - 1] != 'e' and s[i - 1] != 'E':
                    return False
                if i == len(s) - 1:
                    return False
            elif char.isdigit():
                num_seen = True
                num_after_e = True
            elif char == '.':
                if dot_seen or e_seen:
                    return False
                dot_seen = True
                if i == len(s) - 1:
                    return num_seen
            elif char == 'e' or char == 'E':
                if e_seen or not num_seen:
                    return False
                e_seen = True
                num_after_e = False
                if i == len(s) - 1:
                    return False
            else:
                return False
        return num_seen and num_after_e