def sqrt(number):
    if number < 0:
      # Return none for negative numberss
      return None
    if number == 1:
        return number

    # Find the two square roots that are smaller
    # and bigger than our target
    root = number / 2
    prev_root_value = root
    while root * root > number:
        prev_root_value = root
        root = root / 2

    if root * root == number:
        # if we find the square root in the first step
        # return the value
        return root
    else:
        # Lookup the square root between 
        # the values we got in the first step
        start = root
        end = prev_root_value
        mid = (start + end) // 2

        while mid != start and mid != end:
            if mid * mid == number:
                return mid
            if mid * mid > number:
                # If mid square is greater than target
                # discard the upper bound
                end = mid
                mid = (start + end) // 2
                continue
            # If mid square is smaller than target
            # discard the lower bound
            start = mid
            mid = (start + end) // 2

        if mid * mid > number:
            mid -= 1

        return mid


print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")

# Additional test cases

# Large input
print(sqrt(999999999999999999999))
# It should return 31622776601

# Null imput
print(sqrt(None))
# It should return None

# Negative number
print(sqrt(-1))
# It should return None