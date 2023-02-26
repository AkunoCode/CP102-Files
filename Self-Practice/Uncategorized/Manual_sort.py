# Quick-Sort Recursion
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    print(middle)

    return quick_sort(left) + middle + quick_sort(right)


# Example usage
my_list = [3, 6, 1, 8, 2, 10, 4]
list = quick_sort(my_list)
print(list)
