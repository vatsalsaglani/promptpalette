---
Paper: Show Your Work: Scratchpads for Intermediate Computation with Language Models
Link: https://arxiv.org/abs/2112.00114v1
---

Based on the paper, here are the key aspects of the "scratchpad" prompting technique:

Essence of the technique:
The scratchpad technique involves allowing language models to produce intermediate steps or computations before giving a final answer. This is done by training the model to output a sequence of intermediate tokens (the "scratchpad") in addition to the final result.

Key ideas:
1. Provides adaptive computation time, allowing the model to process information as long as needed based on task complexity.
2. Allows storing intermediate state in the scratchpad buffer rather than just in model activations.
3. Forces model to output concrete intermediate states, potentially reducing error propagation.
4. Enables interpretation of intermediate steps to identify and correct errors.

Use cases:
1. Algorithm induction (e.g. learning to perform long addition)
2. Mathematical reasoning (e.g. polynomial evaluation)
3. Program execution prediction
4. Multi-step reasoning tasks

Examples from the paper:

1. Long Addition:
Input: 2 9 + 5 7
Target:
<scratch>
2 9 + 5 7 , C: 0
2 + 5 , 6 C: 1 # added 9 + 7 = 6 carry 1
, 8 6 C: 0 # added 2 + 5 + 1 = 8 carry 0
0 8 6
</scratch>
8 6

2. Polynomial Evaluation:
Input:
Evaluate -7*x**2 + 7*x + 5 at x = 1
Target:
<scratch>
-7*x**2: -7
7*x: 7
5: 5
</scratch>
total: 5

3. Python Code Execution:
Input:
def remove_Occ(s,ch):
    for i in range(len(s)):
        if (s[i] == ch):
            s = s[0 : i] + s[i + 1:]
            break
    for i in range(len(s) - 1,-1,-1):
        if (s[i] == ch):
            s = s[0 : i] + s[i + 1:]
            break
    return s
output = remove_Occ("PHP","P")

Target:
state: {}
line: def remove_Occ(s,ch):
state: {"remove_Occ": "<callable_object remove_Occ>"}
line: output = remove_Occ("PHP","P")
state: {"ch": "P", "s": "PHP"}
line: for i in range(len(s)):
state: {"ch": "P", "s": "PHP", "i": 0}
...
state: {"remove_Occ": "<callable_object remove_Occ>", "output": "H"}

These examples show how the scratchpad technique can be applied to different types of computational and reasoning tasks, allowing the model to show its work step-by-step before producing a final answer.