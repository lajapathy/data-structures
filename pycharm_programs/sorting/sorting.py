class Sorting(object):

    def _combine_list(self, list1, list2):
        combined_list = []

        while(len(list1)>0 and len(list2)>0):
            if list1[0] <= list2[0]:
                combined_list.append(list1[0])
                del list1[0]
            elif list2[0] < list1[0]:
                combined_list.append(list2[0])
                del list2[0]
        if len(list1) == 0:
            combined_list.extend(list2)
        if len(list2) == 0:
            combined_list.extend(list1)

        return combined_list

    def merge_sort(self, list):
        #base case
        if len(list) == 1:
            return list
        list1 = list[:int(len(list)/2)]
        list2 = list[int(len(list) / 2):]
        return (self._combine_list(self.merge_sort(list1), self.merge_sort(list2)))

    def binary_search(self, sorted_list, element):
        ''' Checks if an element is present in a list or not

            Returns:
                True: If element is present
                False: Otherwise
        '''
        if sorted_list == []:
            return False
        if len(sorted_list) == 1:
            return sorted_list[0] == element
        if element == sorted_list[int(len(sorted_list)/2)]:
            return True
        if element < sorted_list[int(len(sorted_list)/2)]:
            return self.binary_search(sorted_list[:int(len(sorted_list)/2)], element)
        else:
            return self.binary_search(sorted_list[(int(len(sorted_list) / 2)):], element)


s = Sorting()
print(s.merge_sort([3,5,1,2,4]))
print(s.merge_sort([3,5,1,2,4,34,12,17,13]))
print(s.binary_search([1,4,6,7],14))
print(s.binary_search([],14))
print(s.binary_search([0,1,2,3,4,5,6,7,8,9],9))



