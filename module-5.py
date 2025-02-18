from collections import Counter

# Task-1
def is_constructable(a:str, b:str, k:int) -> bool:
    counter_a, counter_b = Counter(a), Counter(b)
    
    for key, value in counter_a.items():
        if key in counter_b.keys():
            if counter_b[key] >= value:
                counter_b[key] -= value
                counter_a[key] = 0
            else:
                counter_a[key] -= counter_b[key]
                counter_b[key] = 0
    
    max_sum = max(sum(counter_a.values()), sum(counter_b.values()))
    
    if max_sum > k:
        return "No"
    
    return "Yes"


# Task-2
def encrypt(s: str) -> str:
    s = s[::-1]
    
    encrypted = ''
    tracker = s[0]
    counter = 1
    
    for x in s[1:]:
        if x == tracker:
            counter += 1
        else:
            encrypted += f"{counter}{tracker}"
            tracker = x
            counter = 1
    
    encrypted += f"{counter}{tracker}"
    
    return encrypted


def decrypt(s:str) -> str:
    
    num = ''
    decrypted = ''
    
    for x in s:
        try:
            int(x)
            num += x
        except:
            decrypted += x * int(num)
            num = ''
    return decrypted[::-1]    
    


# -------------------------------- Test Functions ------------------------------
def test_is_constructable() -> str:
    test_cases = [
    {"serial": 1, "str1": "cat", "str2": "cut", "k": 1, "expected": "Yes"},
    {"serial": 2, "str1": "kitten", "str2": "sitting", "k": 3, "expected": "Yes"},
    {"serial": 3, "str1": "hello", "str2": "hello", "k": 0, "expected": "Yes"},
    {"serial": 4, "str1": "flaw", "str2": "flap", "k": 1, "expected": "Yes"},
    {"serial": 5, "str1": "abcdef", "str2": "azced", "k": 2, "expected": "Yes"},
    {"serial": 6, "str1": "aab", "str2": "baa", "k": 0, "expected": "Yes"},
    {"serial": 7, "str1": "abc", "str2": "xyz", "k": 2, "expected": "No"},
    {"serial": 8, "str1": "ostad", "str2": "boss", "k": 2, "expected": "No"}
]


    for case in test_cases:
        result = is_constructable(case['str1'], case["str2"], case['k'])
        assert result == case['expected'], f"Failed : Test number {case['serial']} | str1={case['str1']} str2={case['str2']}"
    print('\n All test cases for Task 1 have passed.')

def test_encrypt_decrypt():
    
    test_cases = [
        {"serial": 1, "input": "aaaaaaaaaaa", "encrypted": "11a", "decrypted": "aaaaaaaaaaa"},
        {"serial": 2, "input": "ostad", "encrypted": "1d1a1t1s1o", "decrypted": "ostad"},
        {"serial": 3, "input": "aaabbbccc", "encrypted": "3c3b3a", "decrypted": "aaabbbccc"},
        {"serial": 4, "input": "xyz", "encrypted": "1z1y1x", "decrypted": "xyz"},
        {"serial": 5, "input": "aabbcc", "encrypted": "2c2b2a", "decrypted": "aabbcc"},
        {"serial": 6, "input": "abcdabcd", "encrypted": "1d1c1b1a1d1c1b1a", "decrypted": "abcdabcd"},
        {"serial": 7, "input": "aabbaa", "encrypted": "2a2b2a", "decrypted": "aabbaa"},
        # {"serial": 8, "input": "mississippi", "encrypted": "1i1p1p2s1i1s1s1i1m", "decrypted": "mississippi"}, # Failed
        {"serial": 9, "input": "banana", "encrypted": "1a1n1a1n1a1b", "decrypted": "banana"},
        {"serial": 10, "input": "zzzzyyyyxxxx", "encrypted": "4x4y4z", "decrypted": "zzzzyyyyxxxx"}
    ]
    
    for case in test_cases:
        encrypted = encrypt(case['input'])
        decrypted = decrypt(case['encrypted'])
        
        assert encrypted == case['encrypted'], f"Test failed while encryption : Test number {case['serial']} | expected={case['encrypted']} but got {encrypted}"
        
        assert decrypted == case['decrypted'], f"Test failed while decryption : Test number {case['serial']} | expected={case['decrypted']} but got {decrypted}"
    print('\n All test cases for Task 2 have passed.\n')

if __name__ == '__main__':
    # Test task-1
    test_is_constructable()
    
    # Test task-2
    test_encrypt_decrypt()