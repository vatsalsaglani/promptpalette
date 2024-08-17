---
Paper: Chain-of-Symbol Prompting Elicits Planning in Large Langauge Models
Link: https://arxiv.org/abs/2305.10276v7
---

Thank you for providing that paper on Chain-of-Symbol (COS) prompting for spatial reasoning in large language models. I'll summarize the key aspects and provide some examples as requested.

Essence of Chain-of-Symbol (COS) Prompting:

Chain-of-Symbol prompting is a novel method that enhances the spatial reasoning capabilities of large language models by representing complex spatial relationships using condensed symbolic representations instead of natural language descriptions.

Key ideas:
1. Converts natural language descriptions of spatial environments into compact symbolic representations
2. Uses symbols to represent spatial relationships between objects
3. Removes redundant text descriptions, focusing on essential spatial information
4. Compatible with few-shot learning approaches
5. Improves model performance while reducing input token count

The method works by:
1. Converting spatial relationships described in natural language to symbolic representations
2. Using these symbolic representations in the intermediate reasoning steps
3. Providing few-shot demonstrations to guide the model in generating similar symbolic chains

Use cases:
- Complex spatial planning tasks
- Virtual environment navigation
- Object manipulation scenarios
- Spatial question answering
- Any task requiring understanding and reasoning about spatial relationships

Examples of Chain-of-Symbol Prompting:

1. Brick World task:

Question: There is a set of bricks. The yellow brick C is on top of the brick E. The yellow brick D is on top of the brick A. The yellow brick E is on top of the brick D. The white brick A is on top of the brick B. For the brick B, the color is white. Now we have to get a specific brick. The bricks must now be grabbed from top to bottom, and if the lower brick is to be grabbed, the upper brick must be removed first. How to get brick D?

COS Answer:
B/A/D/E/C
C/E
E/D
D

So we get the result as C, E, D.

2. Natural Language Navigation:

Question: There is a set of roads and a set of landmarks. The start point is bank A. There is a road which is 200 meters long from bank A to bank C. There is a road which is 100 meters long from bank C to house H. There is a road which is 100 meters long from house H to cinema F. There is a road which is 200 meters long from cinema F to store B. From the start point, how to reach the nearest store?

COS Answer:
- bank A / bank C / house H / cinema F / store B (200 + 100 + 100 + 200 = 600)

So we get the result as bank A / bank C / house H / cinema F / store B.
So the answer is ACHFB

3. Spatial QA:

Background: There are three blue shapes in a block that we call A. Two medium blue squares are below a big blue square. The first medium blue square is to the left of the other medium one which is touching the bottom edge of block A. There is another block below block A we call it B. A big blue triangle is touching the top edge of this block which is above a small black triangle, a big blue circle and a medium blue triangle. The medium triangle is touching the bottom edge of the block. The circle is below and to the left of the small triangle. It is above the medium triangle.

Question: Is the small triangle below the medium triangle?

COS Answer:
B:
1. (big, blue, triangle) = top B
2. (big, blue, triangle) ↑ (small, black, triangle), (big, blue, circle) & (medium, blue, triangle)
3. (big, blue, circle) ↓< (small, black, triangle)
4. (big, blue, circle) ↓ (medium, blue, triangle)
5. (medium, blue, triangle) = bottom B

Based on the provided information, the small black triangle is above the medium blue triangle. So, the correct answer is: "No."

These examples demonstrate how COS uses compact symbolic representations to encode spatial relationships, allowing for more efficient and effective reasoning about complex spatial scenarios.