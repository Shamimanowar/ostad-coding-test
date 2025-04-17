class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

def in_order(node, result, nodes):
    if node == -1:
        return
    in_order(nodes[node].left, result, nodes)
    result.append(nodes[node].val)
    in_order(nodes[node].right, result, nodes)

def pre_order(node, result, nodes):
    if node == -1:
        return
    result.append(nodes[node].val)
    pre_order(nodes[node].left, result, nodes)
    pre_order(nodes[node].right, result, nodes)

def post_order(node, result, nodes):
    if node == -1:
        return
    post_order(nodes[node].left, result, nodes)
    post_order(nodes[node].right, result, nodes)
    result.append(nodes[node].val)

def main1():
    n = int(input())  # Number of nodes
    nodes = []
    for _ in range(n):
        val, left, right = input().split()
        nodes.append(Node(int(val), int(left), int(right)))

    in_order_result = []
    pre_order_result = []
    post_order_result = []

    in_order(0, in_order_result, nodes)
    pre_order(0, pre_order_result, nodes)
    post_order(0, post_order_result, nodes)

    print(" ".join(map(str, in_order_result)))
    print(" ".join(map(str, pre_order_result)))
    print(" ".join(map(str, post_order_result)))



def compute_height(n, parent):
    # Create a list to store the height of each node
    heights = [0] * n

    # Helper function to calculate the height of a node recursively
    def calculate_height(node):
        if heights[node] != 0:  # If already computed, return it
            return heights[node]
        if parent[node] == -1:  # Root node
            heights[node] = 1
        else:
            heights[node] = 1 + calculate_height(parent[node])
        return heights[node]

    # Compute the height for each node
    max_height = 0
    for i in range(n):
        max_height = max(max_height, calculate_height(i))

    return max_height

def main2():
    n = int(input())  # Number of nodes
    parent = list(map(int, input().split()))  # Parent array
    print(compute_height(n, parent))


if __name__ == "__main__":
    main1()
    main2()
