from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        result = []
        remuve = []
        for i in range(0, len(nums)):
            if nums[i] not in result:
                result.append(nums[i])
            else:
                remuve.append(nums[i])
        for i in remuve:
            nums.remove(i)
        return len(result)


if __name__ == '__main__':
    s = Solution()
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    len = s.removeDuplicates(nums)
    print(nums)
    print(len)