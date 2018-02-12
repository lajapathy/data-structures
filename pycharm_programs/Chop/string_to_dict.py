
def string_dict(str):
    word_list = set(str.split(' '))
    temp = {}
    for word in word_list:
        temp[word] = 1

def string_dict2(str):
    return dict([(x,10) for x in set(str.split(" "))])

def string_dict3(str):
    return dict((zip(str.split(" "), ["0"]*len(str))))
    #return dict([(x,10) for x in set(str.split(" "))])

print (string_dict3("india is my my country"))