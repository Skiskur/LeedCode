class Solution:

    def climb(self, stair, count):
        if stair >= 2:
            count = self.climb(stair - 2, count)
        if stair >= 1:
            count = self.climb(stair - 1, count)
        if stair == 0:
            print(count)
            count += 1
        return count

    def climbStairs(self, n: int) -> int:

        if n == 1:
            return 1
        dp = []
        dp.append(1)
        dp.append(2)
        for i in range(2, n):
            dp.append(dp[i - 1] + dp[i - 2])

        return dp[n-1]


if __name__ == '__main__':
    s = Solution()
    len = s.climbStairs(38)
    print(len)