
def find_start_index(arr, element):
    start=0
    end=len(arr)-1
    if (arr[start] == arr[end]):
        return start
    while(start<end):
        mid = (start+end)//2
        if arr[mid] < element:
            start=mid+1
            continue
        end=mid
    return start

def find_end_index(arr, element):
    start=0
    end=len(arr)-1
    element_found=False
    if(arr[start]==arr[end]):
        return end
    while(start<end):
        mid = (start+end)//2
        if arr[mid] > element:
            end=mid-1
            continue
        start = mid
    return end


def repeat_count(arr, element):
    start_position = find_start_index(arr, element)
    end_position = find_end_index(arr, element)
    print(start_position)
    print(end_position)

print(repeat_count([2,3,4,7,7,7,7,7,7,7,7,8,9], 7))
print(repeat_count([7,7,7,7,7,7,8,9], 7))
print(repeat_count([7,7,7,7,7,7], 7))
print(repeat_count([7], 7))