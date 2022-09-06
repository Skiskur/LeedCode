import re

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        p = '^' + p + '$'
        print(p)
        result = re.sub(p,'', s)

        print(result)

        if result == '':
            return True
        else:
            return False


if __name__ == '__main__':
    sol = Solution()

    s = "aa"
    p = "a*"
    

    print(sol.isMatch(s,p))