class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # hashset = set(nums)
        # if len(hashset) == len(nums):
        #     return False
        # else:
        #     return True

        hashset = set()
        for x in nums:
            if x in hashset:
                return True
            hashset.add(x)
        return False
