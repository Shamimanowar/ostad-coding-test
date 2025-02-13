from typing import List

# Task-1 : Pascal's Triangle
def pascal_triangle(numRows: List[int]) -> List[List[int]]:
    initial_triangle = [[1], [1, 1]]
    
    if numRows <= 2:
        return initial_triangle[:numRows]
    
    for i in range(2, numRows): # control the rows
        new_entry = []
        for j in range(i+1): # control the items
            if j in [0, i]:
                new_entry.append(1)
                continue
            new_entry.append(initial_triangle[i-1][j-1] + initial_triangle[i-1][j])
        initial_triangle.append(new_entry)
    return initial_triangle


# Task-2 : Maximum Gap
def maximum_gap(nums: List[int]) -> int :
    length = len(nums)
    
    if length < 2:
        return 0
    
    nums.sort()
    max_diff = float('-inf')
    
    for i in range(1, len(nums)):
        if (diff:= nums[i] - nums[i-1]) > max_diff:
            max_diff = diff
    return max_diff




# -------------------------------- Test Functions ------------------------------

def test_pascal_triangle() -> None:
    test_cases = [
        {
            'order': 1,
            'input': 2,
            'expected_output': [[1], [1, 1]],
            'description': 'Base case with order 1'
        },
        {
            'order': 2,
            'input': 3,
            'expected_output': [[1], [1, 1], [1, 2, 1]],
            'description': 'Base case with order 2'
        },
        {
            'order': 3,
            'input': 4,
            'expected_output': [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]],
            'description': 'Base case with order 3'
        },
        {
            'order': 4,
            'input': 5,
            'expected_output': [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]],
            'description': 'Base case with order 4'
        },
        {
            'order': 5,
            'input': 7,
            'expected_output': [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1]],
            'description': 'Base case with order 5'
        },
        {
            'order': 6,
            'input': 3,
            'expected_output': [[1], [1, 1], [1, 3, 3, 1]],  # Incorrect output
            'description': 'Incorrect output for order 6'
        },
        {
            'order': 7,
            'input': 5,
            'expected_output': [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]],  # Incorrect output
            'description': 'Incorrect output for order 7'
        }
    ]
    
    for case in test_cases[:-2]:
        result = pascal_triangle(case['input'])
        assert result == case['expected_output'], f"Test case {case['order']} failed: {case['description']}"


def test_maximum_gap() -> None:
    test_cases = [
        {
            'order': 1,
            'input': [1, 0, 3],
            'output': 2,
        },        
        {
            'order': 2,
            'input': [1, 0, 3, 7, -5, -6, 13],
            'output': 6,
        },        
        {
            'order': 3,
            'input': [1, 0, 3, 5, 3, 9, 10, 2, 20, -5, 8],
            'output': 10,
        },        
        {
            'order': 4,
            'input': [1, 0, 3, 7, 0, 1, -2, -1],
            'output': 4,
        },        
        {
            'order': 5,
            'input': [1, 0, 3, 5, 0, 1, -2, -1],
            'output': 4, # Incorrect output
        },        
    ]
    
    for case in test_cases[:-1]:
        result = maximum_gap(case['input'])
        assert result == case['output'], f"Test case {case['order']} failed: Expected {case['order']} but Got {result}"


if __name__ == '__main__':
    test_pascal_triangle()
    test_maximum_gap()