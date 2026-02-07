def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

if __name__ == "__main__":
    test_arr = [10, 7, 8, 9, 1, 5]
    print(f"Original array: {test_arr}")
    print(f"Sorted array: {quick_sort(test_arr)}")
