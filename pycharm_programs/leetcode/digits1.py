class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits_new = []
        if digits[-1] < 9:
            digits_new = digits[:len(digits)-1]
            digits_new.append(digits[len(digits)-1] + 1)
            return digits_new
        def incr_digit(dig, carry=0):
            if dig+carry+1 < 9:
                return dig+carry+1,0
            return 10-(dig+carry+1),1
        carry=0
        for i in reversed(xrange(len(digits))):
            digits_new[i], carry = incr_digit(digits[i],carry)
        if carry==1:
            digits_new.insert(0,1)
        return digits_new

import pdb;pdb.set_trace()
ss=Solution()

print ss.plusOne([9])