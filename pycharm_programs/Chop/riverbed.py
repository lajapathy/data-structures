import pdb

def combination(a1, a2):
    if a1==[]:
        return([[x] for x in a2])
    if a2==[]:
        return([[x] for x in a1])
    result_list=[]
    for element in [[[i,j] for i in a1] for j in a2]:
        result_list.extend([x for x in y] for y in element)
    return result_list

def combination_3(a1, a2, a3):
    return combination(combination(a1, a2), a3)
for element in combination_3([1,2,3], [4,5], [7,8,9]):
    print(element)

# def list_combination(a1, a2):
#
#     if a1==[]:
#         return [[x] for x in a2]
#
#     if a2==[]:
#         return [[x] for x in a1]
#
#     return combination()
#
#     result_list = []
#     for i in range(len(a1)):
#         result_list.extend(
#             combination(a1[i], a2))
#
#     for i in range(len(a3)):
#         result_list.extend(
#             combination(a3[i], result_list)
#         )
#     return result_list
#
# for element in list_combination([1,2,3], [4,5]):
#     print (element)
