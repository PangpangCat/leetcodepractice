# 66. Plus One
# Easy
# Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.
#
# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.
#
# You may assume the integer does not contain any leading zero, except the number 0 itself.

class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        #数组转换成数字
        intNum=0
        for i in range(len(digits)):
            intNum=intNum*10+digits[i]
        intNum+=1
        #数字转换成字符
        strNum=str(intNum)
        #字符转换成数组
        res=[]
        for i in range(len(strNum)):
            res.append(int(strNum[i]))
        return res