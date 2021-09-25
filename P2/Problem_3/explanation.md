# Problem 3 - Rearrange_Array_Elements

  ## To solve this problem I decided to sort the array tto find a simple solution to build the two biggest numbers.
  
  ### Time complexity
    - I'm using the quicksort algortithm to sort the array which executes with O(nlog(n)) time complexity.

    - Once sorted we have a for loop that traverses the sorted array two stepss at a time, adding O(n/2) time to our function's time complexity.

  ### Space complexity
    - The worst space complexity of our quicksort call will be O(n) depending on the space used in the call stack.

    - The while loop building the final numbers has a space complexity of O(1)
