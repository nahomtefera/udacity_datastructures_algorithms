def sort_012(input_list):

    if input_list is None:
        return 'Input not valid'
    if None in input_list:
        return 'Input not valid'

    li = 0 # Main pointer
    lzi = 0 # Pointer to the where the next '0' should go
    lti = len(input_list) - 1 # Pointer to the where the next '2' should go

    while li < len(input_list) - 1:
        if input_list[li] == 0 and li > lzi:
            # If we find a 0 and our index is greater 
            # than our 0s pointer, swap 
            input_list[li], input_list[lzi] = input_list[lzi], input_list[li]
            lzi += 1
            continue
        elif input_list[li] == 2 and li < lti:
            # If we find a 2 and our index is smaller 
            # than our 2s pointer 
            if input_list[lti] == 2:
                # If there is already a '2' at our pointer
                # Decrease pointer and re-enter iteration
                lti -= 1
                continue
            # Perform swap
            input_list[lti], input_list[li] = input_list[li], input_list[lti]
            lti -= 1
            continue

        li += 1

    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0,1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

# Additional test cases

# Descending array from 2 to 0
test_function([2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0])
# Returns sorted array

# Null input
test_function([None])
# return 'Input not valid'

# empty array
test_function([])
# returns empty array

