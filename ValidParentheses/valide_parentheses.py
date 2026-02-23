class Solution:
    def isValid(self, s: str) -> bool:
        opening = "({["
        closing = ")}]"
        mapping = {")": "(", "}": "{", "]": "["}

        if len(s) == 1:
            return False

        o = []
        for char in s:
            if char in opening:
                o.append(char)
                continue
            elif char in closing and len(o) > 0:
                if o.pop(-1) == mapping[char]:
                    continue
                else:
                    return False
            else:
                return False

        if len(o) != 0:
            return False
        return True
