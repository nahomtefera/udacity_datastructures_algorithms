# # P3 GET MIN MAX PROBLEM
# # import random
# # def get_min_max(ints):
# #   """
# #   Return a tuple(min, max) out of list of unsorted integers.

# #   Args:
# #       ints(list): list of integers containing one or more integers
# #   """
# #   hashT = {"min": None, "max": None}

# #   for num in ints:

# #     if hashT["min"] is None:
# #       hashT["min"] = num
# #     if hashT["max"] is None:
# #       hashT["max"] = num

# #     if num < hashT["min"]:
# #       hashT["min"] = num

# #     if num > hashT["max"]:
# #       hashT["max"] = num

# #   print(hashT["min"], hashT["max"])
# #   return (hashT["min"], hashT["max"])

# # ## Example Test Case of Ten Integers

# # l = [i for i in range(0, 190)]  # a list containing 0 - 9
# # random.shuffle(l)

# # print ("Pass" if ((0, 189) == get_min_max(l)) else "Fail")

# items = [0, 1, 2, 7, 3, 10, 8, 4, 5]

# #QUICKSORT PLAYGROUND
# # def quicksort(arr, left_index, pivot_index):
# #   if left_index >= pivot_index:
# #     return

# #   while left_index < pivot_index:
# #     current_el = arr[left_index]
# #     pivot = arr[pivot_index]

# #     if current_el <= pivot:
# #       left_index += 1
# #       continue

# #     arr[left_index] = arr[pivot_index - 1]
# #     arr[pivot_index - 1] = pivot
# #     arr[pivot_index] = current_el

# #     pivot_index -= 1

# #   return pivot_index

# # def sort_all(arr, start, end):
# #   if start >= end:
# #     return

# #   pivot_index = quicksort(arr, start, end)

# #   sort_all(arr, start, pivot_index-1)
# #   sort_all(arr, pivot_index+1, end)

# # # print(quicksort(items, 0, len(items)-1))
# # sort_all(items, 0, len(items) -1)

# # HEAP SORT PLAYGROUND

# def heapify(arr, n, index):

#   largest_i = index
#   left_node_index = 2 * index + 1
#   right_node_index = 2 * index + 2

#   # if largest_i < n:
#   #   print("largest_i", largest_i, arr[largest_i])
#   # if left_node_index < n:
#   #   print("left_node_index", left_node_index, arr[left_node_index])
#   # if right_node_index < n:
#   #   print("right_node_index", right_node_index, arr[right_node_index])

#   if left_node_index < n and arr[left_node_index] > arr[largest_i]:
#     largest_i = left_node_index

#   if right_node_index < n and arr[right_node_index] > arr[largest_i]:
#     largest_i = right_node_index

#   if largest_i != index:
#     # print('found firsts')
#     arr[largest_i], arr[index] = arr[index], arr[largest_i]
#     heapify(arr, n, largest_i)

# print(items, len(items))

# solution = []

# for i in range(len(items), -1, -1):
#   heapify(items, len(items), i)
#   print(i, items)

# for i in range(len(items)-1, 0, -1):
#   items[i], items[0] = items[0], items[i]
#   heapify(items, i, 0)

# print(items)

#sort 012


def sort_012(arr):
    li = 0
    lzi = 0
    lti = len(arr) - 1

    while li < len(arr) - 1:
        if arr[li] == 0 and li > lzi:
            arr[li], arr[lzi] = arr[lzi], arr[li]
            lzi += 1
            continue
        elif arr[li] == 2 and li < lti:
            if arr[lti] == 2:
                lti -= 1
                continue
            if arr[lti] == 0:
                arr[lti], arr[li] = arr[li], arr[lti]
                lti -= 1
                continue
            arr[lti], arr[li] = arr[li], arr[lti]
            lti -= 1
            continue

        li += 1

    print(arr)
    return arr


test_case = [0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]
test_case = [2, 2, 0, 0, 2, 1, 0, 2, 2, 1, 1, 1, 0, 1, 2, 0, 2, 0, 1]

sort_012(test_case)

