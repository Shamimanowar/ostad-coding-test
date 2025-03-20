from typing import List, Optional

# Function to read and sort patient records
def manage_patients(n: int, patients: List):
    
    # Sort the patients list by Severity Score (descending), then Age (ascending)
    sorted_patients = sorted(patients, key=lambda x: (-x[3], x[2]))

    print("\nSorted Patient List:")
    for patient in sorted_patients:
        print(f"{patient[0]} {patient[1]} {patient[2]} {patient[3]}")
    
    return sorted_patients



def test_manage_patients():
    # Input data: 5 patient records
    input_data = [
        (101, "Alice", 30, 5),
        (102, "Bob", 25, 8),
        (103, "Charlie", 40, 8),
        (104, "David", 35, 6),
        (105, "Eve", 28, 5)
    ]

    # Expected output after sorting
    expected_output = [
        (102, "Bob", 25, 8),
        (103, "Charlie", 40, 8),
        (104, "David", 35, 6),
        (105, "Eve", 28, 5),
        (101, "Alice", 30, 5)
    ]

    # Simulate the sorting logic
    sorted_patients = manage_patients(5, input_data)

    # Check if the actual output matches the expected output
    assert sorted_patients == expected_output, "Test failed!"
    print("Test passed!")

# Run the test
test_manage_patients()