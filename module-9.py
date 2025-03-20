from typing import List, Optional

def manage_patients(n:int, patients: List):
    for i in range(n):
        for j in range(0, n - i - 1):
            # Compare severity scores (- for descending order)
            if patients[j][3] < patients[j + 1][3] or (
                patients[j][3] == patients[j + 1][3] and patients[j][2] > patients[j + 1][2]
            ):
                # Swap if the current patient should come after the next patient
                patients[j], patients[j + 1] = patients[j + 1], patients[j]


def test_manage_patients():
    # Test Case 1: Basic example with different severity scores
    patients_1 = [
        (101, "Alice", 30, 5),
        (102, "Bob", 25, 8),
        (103, "Charlie", 40, 6)
    ]
    expected_1 = [
        (102, "Bob", 25, 8),
        (103, "Charlie", 40, 6),
        (101, "Alice", 30, 5)
    ]
    manage_patients(len(patients_1), patients_1)
    assert patients_1 == expected_1, f"Test Case 1 Failed: {patients_1}"

    # Test Case 2: Tie in severity score, sort by age
    patients_2 = [
        (101, "Alice", 30, 5),
        (102, "Bob", 25, 5),
        (103, "Charlie", 40, 5)
    ]
    expected_2 = [
        (102, "Bob", 25, 5),
        (101, "Alice", 30, 5),
        (103, "Charlie", 40, 5)
    ]
    manage_patients(len(patients_2), patients_2)
    assert patients_2 == expected_2, f"Test Case 2 Failed: {patients_2}"

    # Test Case 3: Patients already sorted
    patients_3 = [
        (102, "Bob", 25, 8),
        (103, "Charlie", 40, 6),
        (101, "Alice", 30, 5)
    ]
    expected_3 = [
        (102, "Bob", 25, 8),
        (103, "Charlie", 40, 6),
        (101, "Alice", 30, 5)
    ]
    manage_patients(len(patients_3), patients_3)
    assert patients_3 == expected_3, f"Test Case 3 Failed: {patients_3}"

    # Test Case 4: All patients have the same severity and age
    patients_4 = [
        (101, "Alice", 30, 5),
        (102, "Bob", 30, 5),
        (103, "Charlie", 30, 5)
    ]
    expected_4 = [
        (101, "Alice", 30, 5),
        (102, "Bob", 30, 5),
        (103, "Charlie", 30, 5)
    ]
    manage_patients(len(patients_4), patients_4)
    assert patients_4 == expected_4, f"Test Case 4 Failed: {patients_4}"

    # Test Case 5: Single patient
    patients_5 = [
        (101, "Alice", 30, 5)
    ]
    expected_5 = [
        (101, "Alice", 30, 5)
    ]
    manage_patients(len(patients_5), patients_5)
    assert patients_5 == expected_5, f"Test Case 5 Failed: {patients_5}"

    print("All test cases passed!")


if __name__ == '__main__':
    test_manage_patients()
