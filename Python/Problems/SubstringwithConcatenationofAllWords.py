from typing import List
import re

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        result = []

        for w in words:
            print(re.findall(w, s))

        return result


if __name__ == '__main__':
    sol = Solution()

    s = "barfoothefoobarman"
    words = ["foo","bar"]

    print(sol.findSubstring(s,words))
