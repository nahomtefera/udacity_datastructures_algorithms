def rearrange_digits(input_list):
    if input_list is None:
        return 'Input not valid'
    if None in input_list:
        return 'Input not valid'
    # sort array with quicksort
    sort_all(input_list, 0, len(input_list) -1)

    multipliyer = 1
    num_1 = 0
    num_2 = 0

    # build numbers
    for i in range(0, len(input_list), 2):
        num_1 += input_list[i] * multipliyer
        if i+1 <= len(input_list) -1:
            num_2 += input_list[i+1] * multipliyer

        multipliyer *= 10

    return num_1, num_2

def quicksort(arr, left_index, pivot_index):
  if left_index >= pivot_index:
    return

  while left_index < pivot_index:
    current_el = arr[left_index]
    pivot = arr[pivot_index]

    if current_el <= pivot:
      left_index += 1
      continue

    arr[left_index] = arr[pivot_index - 1]
    arr[pivot_index - 1] = pivot
    arr[pivot_index] = current_el

    pivot_index -= 1

  return pivot_index

def sort_all(arr, start, end):
  if start >= end:
    return

  pivot_index = quicksort(arr, start, end)

  sort_all(arr, start, pivot_index-1)
  sort_all(arr, pivot_index+1, end)



def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]


#Additional tests
print(rearrange_digits([9, 8, 4, 2, 1, 7, 6, 5]))
# returns (8641, 9752)

# Empty array
print(rearrange_digits([]))
# returns 0,0

# Null value
print(rearrange_digits(None))
# returns 'Input not valid'
