# Problem 1 - P1_LRU_cache

  ## For this problem I chose to use a dictionary to lookup key value pairs in our cache in constant time. I also used a list to easily rearange the usage order of the elements added to the cache and pop/append elements.
  
    - Worst Case Complexity: O(1) since all operations run in constant time. 


# Problem 2 - P2_File_Recursion
  ## For this problem I'm using a list to store the pathnames that match our query and I'm using recursion function to traverse through each folder.

    - Worst Case Complexity: O(n) - since we have to traverse through every directory and subdirectory the time complexity will be linear depending on the number of folders there are.



# Problem 3
    - Worst Case Complexity: O(n)
    - Algorithm:
        - Initialize variable O(1)
        - Loop operation O(n)
            - Initialize variables O(1)
            - Comparison O(1)
                - 4x Search dict O(1)
                    - Assign variable O(1)
        - Loop Operation O(n)
            - Assign variable O(1)
            - Comparison O(1)
                - 2x Assign variable O(1)

# Problem 4
    - Worst Case Complexity: O(n log n)
    - Algorithm:
        - 3x Assign variables O(1)
        - Loop through calls O(n)
            - Comparison O(1)
                - 3x Comparison O(1)
                    - Assign variables / Append to list O(1)
        - List operations and Sort O(n log n)
        - Assign variable O(1)
        - Loop through list O (n)
            - Comparison O(1)
                - Addition O(1)
        - 2x Prints O(1)
        - Loop O(n)

# Problem 5 COMPLEXY ANALYSIS
    - Worst Case Complexity: O(n log n)
    - Algorithm:
        - Assign Variables O(1)
        - 3x Loop list
            - Assign / add O(1)
    - Sort list O(n log n)
    - Print O(1)
    - Loop O(n)
        - Print O(1)