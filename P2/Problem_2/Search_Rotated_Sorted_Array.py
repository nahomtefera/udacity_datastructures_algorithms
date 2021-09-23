def rotated_array_search(input_list, number):
    if len(input_list) == 0:
        return -1 
    if input_list[0] == number:
        return 0
    elif input_list[len(input_list) -1] == number:
        return len(input_list) -1
    
    # Find pivot
    pivot = findPivot(input_list)

    if pivot == None:
        return 'Array is not valid'
        
    # Once we find the pivot
    # we can perform a binary search
    # with the pivot as the lower or upper bound
    if number == input_list[pivot]:
        return pivot
    elif number > input_list[len(input_list)-1]:
        # If last item is smaller than target
        # pivot will be our upper bound 
        end = pivot
        start = 0
    else:
        # else pivot will be lower bound
        start = pivot
        end = len(input_list) -1 

    while start < end:
        # print(start, end)
        # perform binary search
        # within the bounds specified on previous step
        mid = (start + end) // 2
        # print(mid)
        # print(input_list[mid])
        if input_list[mid] == number:
            return mid
        elif input_list[mid] > number:
            end = mid
            continue
        # break condition
        if start == mid or end == mid:
            break
        start = mid
        
    return -1


def findPivot(arr):
    start = 0
    end = len(arr) - 1

    pivot = None

    while start < end:
        mid = (start + end) // 2
        if arr[mid] < arr[start]:
            # we are to the right of the pivot
            if arr[mid - 1] > arr[mid]:
                pivot = mid
                break
            end = mid
            continue
        # we are on the left side of the pivot
        if arr[mid + 1] < arr[mid]:
            pivot = mid + 1
            break
        # break condition
        if start == mid or end == mid:
            break
        start = mid

    return pivot

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

# Additional test cases

# Passing a sorted array
test_function([[1, 2, 3, 4, 5, 6, 7], 2])
# It will return Array is not valid

# Array with negative numbers and negative target
test_function([[1, 2, 3, 4, 5, -5, -4, -2, -1, 0], -1])
# Returns index 8

# Empty array
test_function([[], 11])
# returns -1
