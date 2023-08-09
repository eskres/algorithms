# binary search - O(log n)

def binary_search(elements, value):
    low = 0
    high = len(elements)-1

    # loop through list
    while low <= high:
        # find middle point
        mid = (low + high)
        # Return middle value if it matches input value
        if elements[mid] == value:
            return mid
        # Check whether middle value is higher or lower than input value
        if elements[mid] > value:
            high = mid - 1
        else:
            low = mid + 1
    return None
        
a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(binary_search(a_list, 3))