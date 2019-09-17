class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        word_list = str.split(' ')
        if len(pattern) != len(word_list):
            return False
        if not pattern and str:
            return False
        if pattern and not str:
            return False
        pattern_dict = {}
        for i in xrange(len(word_list)):
            if pattern[i] in pattern_dict:
                if (word_list[i] != pattern_dict[pattern[i]]):
                    return False
            else:
                if word_list[i] in pattern_dict.values():
                    return False
                pattern_dict[pattern[i]] = word_list[i]
        return True


sol = Solution()
print sol.wordPattern('aaa', 'aa aa aa aa')