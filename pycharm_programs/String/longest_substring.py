#given a string, find the longest substring with no repeating characters

def longest_substring(str_in):
    if len(str_in) == 1:
        return str_in
    start_index = 0
    end_index = 1
    result = ''
    curr_result = ''

    def max_len(str1, str2):
        if len(str1) > len(str2):
            return str1
        return str2

    while end_index < len(str_in):
        if str_in[end_index] not in str_in[start_index:end_index]:
            curr_result = str_in[start_index:end_index+1]
            end_index += 1
        else:
            start_index = end_index
            result = max_len(str_in[start_index:end_index+1], curr_result)

    return result

print(longest_substring('abcabcbb'))
