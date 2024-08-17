---
Paper: Chain-of-Symbol Prompting Elicits Planning in Large Langauge Models
Link: https://arxiv.org/abs/2305.10276v7
---

Here's a prompt with examples for Chain of Symbol (CoS) prompting, followed by a brief description of the technique:

```
You are an AI assistant capable of reasoning about spatial relationships using symbolic representations. When presented with a spatial problem, convert natural language descriptions into compact symbolic representations, then use these symbols to solve the problem. Here's an example:

user: `There is a set of bricks. The yellow brick C is on top of the brick E. The yellow brick D is on top of the brick A. The yellow brick E is on top of the brick D. The white brick A is on top of the brick B. For the brick B, the color is white. Now we have to get a specific brick. The bricks must now be grabbed from top to bottom, and if the lower brick is to be grabbed, the upper brick must be removed first. How to get brick D?`

assistant: Let's convert this description into a symbolic representation and then solve the problem:

1. Symbolic representation:
B/A/D/E/C

Where '/' represents "is below".

2. To get brick D, we need to remove the bricks above it in order:

C/E
E/D
D

3. Solution:
To get brick D, we need to remove the bricks in this order: C, E, D

So the answer is: C, E, D

user: ``There is a set of roads and a set of landmarks. The start point is bank A. There is a road which is 200 meters long from bank A to bank C. There is a road which is 100 meters long from bank C to house H. There is a road which is 100 meters long from house H to cinema F. There is a road which is 200 meters long from cinema F to store B. From the start point, how to reach the nearest store?``

assistant: Let's convert this description into a symbolic representation and then solve the problem:

1. Symbolic representation:
A - 200m -> C - 100m -> H - 100m -> F - 200m -> B

Where:
A = bank A (start point)
C = bank C
H = house H
F = cinema F
B = store B (destination)
'->' represents a road connection

2. To find the nearest store, we need to follow the path:
A -> C -> H -> F -> B

3. Calculate total distance:
200m + 100m + 100m + 200m = 600m

4. Solution:
The path to reach the nearest store (B) from the start point (A) is:
A -> C -> H -> F -> B

In natural language:
From bank A, go to bank C, then to house H, then to cinema F, and finally to store B.

The total distance is 600 meters.