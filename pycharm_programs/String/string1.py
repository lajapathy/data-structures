#You have a string aaabbdcccccf, transform it the following way => a3b2d1c5f1
#ie: aabbaa -> a2b2a2 not a4b2

def convert_string(str1):
    curr_char_count = 1
    output_str = ''
    temp = ''
    for c in str1:

        if c == temp :
            curr_char_count += 1
            continue
        else:
            output_str = output_str + temp + str(curr_char_count)
            temp = c
            curr_char_count = 1

    output_str = output_str + temp + str(curr_char_count)

    return output_str[1:]


print convert_string('aabbaa')



