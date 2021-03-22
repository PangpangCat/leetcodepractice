# 496. Next Greater Element I
# Easy
# Example 1:
#
# Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
# Output: [-1,3,-1]
# Explanation:
# For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
# For number 1 in the first array, the next greater number for it in the second array is 3.
# For number 2 in the first array, there is no next greater number for it in the second array, so output -1.
# Example 2:
#
# Input: nums1 = [2,4], nums2 = [1,2,3,4]
# Output: [3,-1]
# Explanation:
# For number 2 in the first array, the next greater number for it in the second array is 3.
# For number 4 in the first array, there is no next greater number for it in the second array, so output -1.

# Example 1:
#
# Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
# Output: [-1,3,-1]
# Explanation:
# For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
# For number 1 in the first array, the next greater number for it in the second array is 3.
# For number 2 in the first array, there is no next greater number for it in the second array, so output -1.

# Example 2:
#
# Input: nums1 = [2,4], nums2 = [1,2,3,4]
# Output: [3,-1]
# Explanation:
# For number 2 in the first array, the next greater number for it in the second array is 3.
# For number 4 in the first array, there is no next greater number for it in the second array, so output -1.

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d ={}
        st = []
        res =[]

        for x in nums2:
            if len(st) == 0:
                st.append(x)
            elif x <= st[-1]:
                st.append(x)
            else:
                while st and st[-1]< x:
                    d[st.pop()] = x
                st.append(x)
        for x in nums1:
            if x in d:
                res.append(d[x])
            else:
                res.append(-1)
        return res

# 建立一个stack 作为一个递减的sequence
# dictionary是{nums2的值：它的greater element}
#For example [9, 8, 7, 3, 2, 1, 6]. The stack will first contain [9, 8, 7, 3, 2, 1]
# and then we see 6 which is greater than 1 so we pop 1 2 3 whose next greater element should be 6.
