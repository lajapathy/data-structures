
class Solution:
    def longestCommonPrefix(self, strs):

        #base
        if not strs:
            return ''
        if len(strs)==1:
            return strs[0]

        mid = len(strs)//2
        leftresult = self.longestCommonPrefix(strs[:mid])
        rightresult = self.longestCommonPrefix(strs[mid:])
        print leftresult, rightresult

        return self.lcp(leftresult, rightresult)

    def lcp(self, str1, str2):
        #import pdb;pdb.set_trace()
        if not str1 or not str2:
            return ''
        result = ''
        minlength = min(len(str1), len(str2))
        for i in xrange(minlength):
            if str1[i]==str2[i]:
                result += str1[i]
        return result

s=Solution()
print s.longestCommonPrefix(['abcd','abcef','abcg',''])
print s.longestCommonPrefix(['abcd','abcef','abcg','abc'])