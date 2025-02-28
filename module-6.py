"""
********************************************************************************
*                                                                              *
*                                Module 6: Recursion                           *
*                                                                              *
********************************************************************************
This module covers various aspects of recursion, including its definition, 
applications, and implementation in Python. Recursion is a powerful technique 
where a function calls itself to solve smaller instances of the same problem.

Tasks:
1. Task-1: Given an integer n, return true if it is a power of 5. Otherwise, return false.
An integer n is a power of 5, if there exists an integer x such that n == 5^x

2. Task-2:Sadman and Salman are playing a game. Initially, Sadman has a string word = "a".
You are given a positive integer k.
Now Salman will ask Sadman to perform the following operation forever:
Generate a new string by changing each character in word to its next character in the English alphabet, and append it to the original word.
For example, performing the operation on "c" generates "cd" and performing the operation on "zb" generates "zbac".
Return the value of the kth character in word, after enough operations have been done for word to have at least k characters.
Note that the character 'z' can be changed to 'a' in the operation.

"""


# Task-1 Solution
def is_power_of_5(n: int) -> bool:
    if n == 5 or n == 1:
        return True
    if n % 5 != 0 or n <= 0:
        return False
    
    return is_power_of_5(n / 5)



# Task-2 Solution
def find_kth_character(k, word="a"):
    if len(word) >= k:
        return word[k - 1]
    
    next_word = ""
    for char in word:
        if char == 'z':
            next_char = 'a'
        else:
            next_char = chr(ord(char) + 1)
        next_word += next_char
    
    return find_kth_character(k, word + next_word)



# ********************************* Test Functions ***********************************

def test_is_power_of_5():
    test_cases = [
        {"serial_number": 1, "input": -1, "expected_output": False},
        {"serial_number": 2, "input": 1, "expected_output": True},
        {"serial_number": 3, "input": 0, "expected_output": False},
        {"serial_number": 4, "input": 100, "expected_output": False},
        {"serial_number": 5, "input": 500, "expected_output": False},
        {"serial_number": 6, "input": 625, "expected_output": True},
        {"serial_number": 7, "input": -625, "expected_output": False},
        {"serial_number": 8, "input": 3125, "expected_output": True},
        {"serial_number": 9, "input": 3126, "expected_output": False},
        {"serial_number": 10, "input": 15625, "expected_output": True},
        {"serial_number": 11, "input": 78125, "expected_output": True},
        {"serial_number": 12, "input": -78126, "expected_output": False}
    ]
    for test_case in test_cases:
        assert is_power_of_5(test_case["input"]) == test_case["expected_output"], \
            f"Test case {test_case['serial_number']} failed!"
    
    print("All test cases for is_power_of_5() passed successfully.")


def test_find_kth_character():
    test_cases = [
        {"serial_number": 1, "input": 5, "expected_output": "b"},
        {"serial_number": 2, "input": 10, "expected_output": "c"},
        {"serial_number": 3, "input": 1, "expected_output": "a"},
        {"serial_number": 4, "input": 2, "expected_output": "b"},
        {"serial_number": 5, "input": 3, "expected_output": "b"},
        {"serial_number": 6, "input": 7, "expected_output": "b"}, # False test case
        {"serial_number": 7, "input": 12, "expected_output": "c"} # False test case
    ]
    
    for case in test_cases:
        result = find_kth_character(case["input"])
        assert result == case["expected_output"], f"Test case {case['serial_number']} failed: expected {case['expected_output']}, got {result}"
    
    print("All test cases passed!")


    
if __name__ == '__main__':
    test_is_power_of_5()
    test_find_kth_character()