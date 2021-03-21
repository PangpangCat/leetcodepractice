# 697. Degree of an Array
# Easy
# Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.
#
# Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.
#
# Example 1:
#
# Input: nums = [1,2,2,3,1]
# Output: 2
# Explanation:
# The input array has a degree of 2 because both elements 1 and 2 appear twice.
# Of the subarrays that have the same degree:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# The shortest length is 2. So return 2.
#
# Example 2:
#
# Input: nums = [1,2,2,3,1,4,2]
# Output: 6
# Explanation:
# The degree is 3 because the element 2 is repeated 3 times.
# So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.
#
# Constraints:
#
# nums.length will be between 1 and 50,000.
# nums[i] will be an integer between 0 and 49,999.

class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = {}
        for i in nums:
            if i not in a:
                a[i] =1
            else:
                a[i]+=1
        degree = max(a.values())
        res =[]
        for k, v in a.items():
            if v == degree:
                res.append(k)
        mmin = 100000
        for i in res:
            x = len(nums) - nums.index(i) - nums[::-1].index(i)
            if x<mmin:
                mmin = x
        return mmin

# nums =[1,2,2,3,1]
# left,right,count ={},{},{}
# print(list(enumerate(nums)))
# for i, x in enumerate(nums):
#     if x not in left:
#         left[x] = i
#         right[x] = i
#         count[x] = count.get(x, 0) + 1
# print(left)
# print(right)
# print(count)
# ans = len(nums)
# degree = max(count.values())
# print(degree)
# for x in count:
#     if count[x] == degree:
#         ans = min(ans, right[x] - left[x] +1)




