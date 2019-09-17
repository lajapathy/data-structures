class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) < 3:
            return False
        start = 0
        end = len(A) - 1
        while start < len(A) - 1:
            #import pdb;pdb.set_trace()
            if start > end:
                return False
            if A[start] == A[start + 1] or A[end] == A[end - 1]:
                return False
            if start == end and end < len(A) - 1:
                return True
            if A[start] < A[start + 1]:
                start += 1
            if A[end] < A[end - 1]:
                end -= 1
        return False
s = Solution()
print s.validMountainArray([[0,3,2,1]])