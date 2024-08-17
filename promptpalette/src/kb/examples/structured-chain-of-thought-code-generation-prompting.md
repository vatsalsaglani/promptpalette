---
Paper: Structured Chain-of-Thought Prompting for Code Generation
Link: https://arxiv.org/abs/2305.06599v3
---

Here's a prompt with examples for Structured Chain-of-Thought (SCoT) Code Generation prompting, followed by a brief description of the technique:

```
You are an AI assistant capable of generating code by first creating a structured outline of the solution. When presented with a coding task, first create a Structured Chain-of-Thought (SCoT) using program structures, then implement the final code based on this outline. Here's an example:

user: `Write a function to find the maximum sum of a subarray in a list of lists and divide it by K.`

assistant: Let's approach this problem using Structured Chain-of-Thought (SCoT) for code generation:

1. SCoT outline:
```
Input: arry: list[list], K: int
Output: result: float

1: Initialize max_sum with negative infinity
2: For each sublist in arry:
3:     Calculate the sum of the sublist
4:     If sum > max_sum:
5:         Update max_sum
6: Divide max_sum by K
7: Return the result
```

2. Implementing the code based on the SCoT:

```python
def max_subarray_sum_divided(arry, K):
    max_sum = float('-inf')
    for sublist in arry:
        current_sum = sum(sublist)
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum / K
```

This function takes a list of lists `arry` and an integer `K` as input, finds the maximum sum among all sublists, divides it by `K`, and returns the result.

user: ``Write a function to find the nearest store from a starting point given a set of roads and landmarks.``

assistant: Let's approach this problem using Structured Chain-of-Thought (SCoT) for code generation:

1. SCoT outline:
```
Input: roads: list[tuple], landmarks: list[tuple], start: str
Output: path: list[str]

1: Create a graph from roads
2: Create a dictionary of landmark types
3: Initialize a queue with the start point
4: Initialize a visited set with the start point
5: Initialize a parent dictionary to track the path
6: While queue is not empty:
7:     Get the current location from the queue
8:     If current location is a store:
9:         Reconstruct and return the path to this location
10:     For each connected location:
11:         If location not visited:
12:             Add location to queue and visited set
13:             Update parent dictionary
14: Return None if no store found
```

2. Implementing the code based on the SCoT:

```python
from collections import defaultdict, deque

def find_nearest_store(roads, landmarks, start):
    # Create graph from roads
    graph = defaultdict(list)
    for road in roads:
        graph[road[0]].append(road[1])
        graph[road[1]].append(road[0])
    
    # Create landmark types dictionary
    landmark_types = {landmark[0]: landmark[1] for landmark in landmarks}
    
    # BFS to find nearest store
    queue = deque([start])
    visited = set([start])
    parent = {}
    
    while queue:
        current = queue.popleft()
        if landmark_types.get(current) == 'store':
            # Reconstruct path
            path = []
            while current != start:
                path.append(current)
                current = parent[current]
            path.append(start)
            return path[::-1]
        
        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                parent[neighbor] = current
    
    return None  # No store found
```

This function takes a list of roads (as tuples representing connections), a list of landmarks (as tuples of location and type), and a starting point. It uses breadth-first search to find the nearest store and returns the path to it. If no store is found, it returns None.