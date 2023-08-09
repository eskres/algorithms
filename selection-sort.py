# selection sort = O(n^2)

def selection_sort(list):
    for i in range(len(list) - 1):
        # assume value at i is smallest
        smallest = i
        # loop through values in the list that come after i
        for j in range(i + 1, len(list)):
            # check whether value is smaller than that found at i
            if(list[j] < list[smallest]):
                smallest = j
        # Swap values
        list[i], list[smallest] = list[smallest], list[i]
    return list


print(selection_sort([5, 3, 6, 2, 10]))