import pdb
def longest_palindromic_substring(str_in):
    i=1
    j=1
    palin_result = str_in[0]
    current_result = str_in[0]
    def get_max_length_string(str1, str2):
        if len(str1) > len(str2):
            return str1
        return str2
    while not ((j>len(str_in) or (i>len(str_in)))):
        #pdb.set_trace()
        if str_in[j:i-1:-1] == str_in[i:j+1]:
            current_result += str_in[i:j+1]
            palin_result = get_max_length_string(palin_result, current_result)
            j+=1
        else:
            current_result = ''
            i+=1

    return palin_result

def longest_palindromic_substring2(str_in):
    result=[][]

print(longest_palindromic_substring("mbbababal"))


