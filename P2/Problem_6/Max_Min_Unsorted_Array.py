import random
def get_min_max(ints):
  max = None
  min = None
  for num in ints:
    if max is None:
      max = num
    if min is None:
      min = num

    if num > max:
      max = num
    if num < min:
      min = num
  return (min, max) 


l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")


# Additional test cases

# None values
test1 = [None, None, None, None, 0]
print(get_min_max(test1))
# returns (0,0)

# Empty Array
test2 = []
print(get_min_max(test2))
# returns (None, None)

# Test 3
test3 = [i for i in range(232, 7986)]
random.shuffle(test3)
print(get_min_max(test3))
# returns (232, 7985)