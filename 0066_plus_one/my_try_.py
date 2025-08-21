class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        strDigits = str()
        for i in digits:
            strDigits = strDigits + str(i)
            plusOne = str(int(strDigits) +1)
        return list(int(i) for i in plusOne)