from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        base = strs[0]
        for s in strs[1:]:
            i = 0
            while i < len(base) and i < len(s) and base[i] == s[i]:
                i += 1
            base = base[:i]

        return base
