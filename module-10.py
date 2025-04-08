
# Task-1 - Start
def sort_array(array):
    # Implementing a sorting algorithm (Merge Sort) to sort the array
    # This is necessary for the binary search to work correctly
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left_half = sort_array(array[:mid])
    right_half = sort_array(array[mid:])
    return merge(left_half, right_half)

def merge(left, right):
    sorted_array = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])
    return sorted_array

def binary_search_left(array, target):
    # Find the first occurrence of target or greater value
    low, high = 0, len(array)
    while low < high:
        mid = (low + high) // 2
        if array[mid] < target:
            low = mid + 1
        else:
            high = mid
    return low

def binary_search_right(array, target):
    # Find the first occurrence of a value greater than target
    low, high = 0, len(array)
    while low < high:
        mid = (low + high) // 2
        if array[mid] <= target:
            low = mid + 1
        else:
            high = mid
    return low

def fast_search(array, queries):
    # Sort the array using merge sort
    sorted_array = sort_array(array)
    results = []
    for l, r in queries:
        left_index = binary_search_left(sorted_array, l)
        right_index = binary_search_right(sorted_array, r)
        results.append(right_index - left_index)
    return results

# Task-1 - End


# Task-2 - Start

def closest_to_the_left(n, k, array, queries):
    def binary_search_left(array, target):
        # Binary search for the maximum index of element ≤ target
        low, high = 0, n - 1
        result = -1  # Initialize result as -1 (no valid index found yet)
        while low <= high:
            mid = (low + high) // 2
            if array[mid] <= target:
                result = mid  # Update result (1-based index will be adjusted later)
                low = mid + 1  # Move right to find a larger value ≤ target
            else:
                high = mid - 1  # Move left to discard larger values
        return result + 1  # Convert 0-based index to 1-based index

    # Process each query
    results = []
    for value in queries:
        results.append(binary_search_left(array, value))
    return results

# Task-2 - End

########################################## Test Cases ##########################################
# Task-1 - Test Cases
def test_fast_search():
    # Test Case 1: Simple case
    array = [10, 1, 10, 3, 4]
    queries = [(1, 10), (2, 9), (3, 4), (2, 2)]
    assert fast_search(array, queries) == [5, 2, 2, 0]

    # Test Case 2: Array with negative numbers
    array = [-5, -10, 0, 5, 10]
    queries = [(-10, -5), (-5, 0), (0, 10), (5, 15)]
    assert fast_search(array, queries) == [2, 2, 3, 2]

    # Test Case 3: Array with duplicates
    array = [5, 5, 5, 10, 10]
    queries = [(5, 5), (10, 10), (1, 5)]
    assert fast_search(array, queries) == [3, 2, 3]

    # Test Case 4: Query range not in array
    array = [1, 2, 3, 4, 5]
    queries = [(6, 10), (-10, -1)]
    assert fast_search(array, queries) == [0, 0]

    print("All test cases passed!")

# Task-2 - Test Cases
def test_closest_to_the_left():
    # Test Case 1: Example from problem statement
    array = [3, 3, 5, 8, 9]
    queries = [2, 4, 8, 1, 10]
    assert closest_to_the_left(5, 5, array, queries) == [0, 2, 4, 0, 5]

    # Test Case 2: Single element array
    array = [5]
    queries = [3, 5, 6]
    assert closest_to_the_left(1, 3, array, queries) == [0, 1, 1]

    # Test Case 3: All elements equal
    array = [7, 7, 7, 7, 7]
    queries = [6, 7, 8]
    assert closest_to_the_left(5, 3, array, queries) == [0, 5, 5]

    # Test Case 4: Queries with no valid indices
    array = [10, 20, 30, 40, 50]
    queries = [5, 1]
    assert closest_to_the_left(5, 2, array, queries) == [0, 0]

    print("All test cases passed!")




if __name__ == "__main__":
    # Run tests
    test_fast_search()

    test_closest_to_the_left()