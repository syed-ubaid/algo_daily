def binary_search(arr, target):
    """
    Performs binary search on a sorted array.
    
    Args:
        arr (list): A sorted list of elements.
        target (any): The element to search for.
        
    Returns:
        int: The index of the target if found, else -1.
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1

if __name__ == "__main__":
    # Test cases
    test_arr = [1, 3, 5, 7, 9, 11, 13, 15]
    print(f"Searching for 7 in {test_arr}: Index {binary_search(test_arr, 7)}")
    print(f"Searching for 10 in {test_arr}: Index {binary_search(test_arr, 10)}")
