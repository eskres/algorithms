        
# binary search

def binary_search(elements, value):
    low = 0
    high = len(elements)-1

    while low <= high:
        mid = (low + high)
        if elements[mid] == value:
            return mid
        if elements[mid] > value:
            high = mid - 1
        else:
            low = mid + 1
    return None
        
a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(binary_search(a_list, 3))