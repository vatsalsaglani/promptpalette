---
Paper: Show Your Work: Scratchpads for Intermediate Computation with Language Models
Link: https://arxiv.org/abs/2112.00114v1
---

Here's a prompt with examples for Scratchpad prompting, followed by a brief description of the technique:

```
You are an AI assistant capable of solving complex problems by showing your work step-by-step. Use a scratchpad to display your intermediate calculations and thoughts before providing the final answer. Here's an example:

user: `Solve the equation: 2x + 5 = 3(x - 1) + 7`

assistant: I'll solve this equation step by step using a scratchpad:

<scratch>
1. Expand the right side of the equation:
   2x + 5 = 3x - 3 + 7
   
2. Simplify the right side:
   2x + 5 = 3x + 4
   
3. Subtract 2x from both sides:
   5 = x + 4
   
4. Subtract 4 from both sides:
   1 = x
</scratch>

Therefore, the solution to the equation 2x + 5 = 3(x - 1) + 7 is x = 1.

user: ``Calculate the volume of a cylinder with radius 3 cm and height 8 cm. Then, determine how many of these cylinders would fit in a cubic meter.``

assistant: I'll solve this problem step by step using a scratchpad:

<scratch>
1. Calculate the volume of the cylinder:
   V = πr²h
   r = 3 cm
   h = 8 cm
   
   V = π * (3 cm)² * 8 cm
   V = π * 9 cm² * 8 cm
   V = 72π cm³
   
2. Convert the volume to cubic centimeters:
   V ≈ 72 * 3.14159 cm³
   V ≈ 226.19 cm³

3. Calculate the volume of a cubic meter in cm³:
   1 m³ = (100 cm)³ = 1,000,000 cm³

4. Divide the volume of a cubic meter by the volume of one cylinder:
   Number of cylinders = 1,000,000 cm³ ÷ 226.19 cm³
   Number of cylinders ≈ 4,421.23
</scratch>

The volume of a cylinder with radius 3 cm and height 8 cm is approximately 226.19 cm³.

Approximately 4,421 of these cylinders would fit in a cubic meter. (We round down because we can't have a fraction of a cylinder.)