#longest common substring

class Solution:
    def lcs(self, strs):
        if not strs:
            return ''
        mid = len(strs)/2
        leftresult = self.lcs(strs[:mid])
        rightresult = self.lcs(strs[mid:])

        return self.lcs2strings(leftresult, rightresult)

    def maxlength(self, str1, str2):
        if len(str1)>len(str2):
            return str1
        return str2

    def lcs2strings(self, str1, str2):
        #basecase
        if not str1 or not str2:
            return ''

        if str1[-1]==str2[-1]:
            return self.lcs2strings(str1[:-1], str2[:-1]) + str1[-1]

        result1 = self.lcs2strings(str1, str2[:-1])
        result2 = self.lcs2strings(str1[:-1], str2)
        return self.maxlength(result1, result2)

s = Solution()
