class Solution:
    def plusOne(self, digits):
        digits.reverse()
        for i in range(0, len(digits)):
            if digits[i] < 9:
                digits[i] = digits[i] + 1
                digits.reverse()
                print(digits)
                return digits
            else:
                digits[i] = 0
        digits.append(1)
        digits.reverse()
        return digits


if __name__ == '__main__':
    s = Solution()
    nums = [9,9,9]

    len = s.plusOne(nums)
    print(nums)
    print(len)