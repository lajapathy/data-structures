import pdb
def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    start_index = 0
    end_index = 2
    result_str = s[start_index:end_index + 1]

    def max_len(s1, s2):
        if len(s1) > len(s2):
            return s1
        else:
            return s2

    while (end_index < len(s)):
        pdb.set_trace()
        sub_str = s[start_index:end_index + 1]
        end_index += 1
            result_str = max_len(sub_str, result_str)
        else:

            sub_str += s[end_index]
    return result_str

print(longestPalindrome("lajvju"))