class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
    
        i = s.strip(" ")[::-1].find(" ")
        if (i==-1):
            return len(s.strip())
        else:
            return i