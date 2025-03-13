
def next_smaller_elements(n, arr):
    result = [-1] * n
    stack = [] 

    for i in range(n):
        while stack and arr[i] < arr[stack[-1]]:
            result[stack.pop()] = arr[i]
        stack.append(i)

    return result