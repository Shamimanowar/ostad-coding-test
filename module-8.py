
def next_smaller_elements(n, arr):
    result = [-1] * n
    stack = [] 

    for i in range(n):
        while stack and arr[i] < arr[stack[-1]]:
            result[stack.pop()] = arr[i]
        stack.append(i)

    return result


class QueueUsingTwoStacks:
    def __init__(self):
        self.push_stack = []
        self.pop_stack = []

    def enqueus(self, item):
        self.push_stack.append(item)
        
    def dequeue(self):
        if len(self.pop_stack) == 0:
            self._shift_push_to_pop_stack()
        
        if len(self.pop_stack) == 0:
            return -1
        
        value = self.pop_stack.pop()
        print(value)
        return value
    
    def front(self):
        if len(self.pop_stack) == 0:
            self._shift_push_to_pop_stack()
        
        if len(self.pop_stack) == 0:
            return -1
        
        value = self.pop_stack[-1]
        print(value)
        return value
    
    def _shift_push_to_pop_stack(self):
        while len(self.push_stack) != 0:
            self.pop_stack.append(self.push_stack.pop())

    def get_data(self):
        print(f"Push stack = {self.push_stack} and Pop stack = {self.pop_stack}")
        return self._shift_push_to_pop_stack()