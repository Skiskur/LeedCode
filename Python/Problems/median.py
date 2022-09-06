from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    	arr = nums1 + nums2
    	arr.sort()

    	lenght = len(arr)

    	for num in arr:
    		num = float(num)

    	result = lenght/2 - 1



    	if result % 1 == 0:
    		result = int(result)
    		result = (arr[result] + arr[result+1]) /2
    	else:
    		result += 0.5
    		result = int(result)
    		result = arr[result]
    	


    	return result



if __name__ == '__main__':

	num1 = [0,0]
	num2 = [0,0]
	# 0,0,1,2,2,3 == 2

	s = Solution()

	print(s.findMedianSortedArrays(num1, num2))