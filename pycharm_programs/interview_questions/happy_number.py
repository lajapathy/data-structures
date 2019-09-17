class Solution(object):
    def isHappy(self, n, count=0):
        """
        :type n: int
        :rtype: bool
        """
        if count>10:
            return False
        if n==1:
            return True
        sumsquare = 0
        for c in str(n):
            #import pdb;pdb.set_trace()
            sumsquare += int(c)**2
        count+=1
        return self.isHappy(sumsquare, count)

s=Solution()

print s.isHappy(55)