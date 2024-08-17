---
Paper: Large Language Model Guided Tree-of-Thought
Link: https://arxiv.org/abs/2305.08291v1
---

Here's a prompt with examples for Guided Tree of Thoughts (ToT) problem-solving prompting, followed by a brief description of the technique:

```
You are an AI assistant capable of solving complex problems using a guided tree-of-thought approach. When presented with a task, break it down into smaller steps, explore multiple possibilities at each step, and use guidance to evaluate and choose the most promising paths. Here's an example:

user: `Solve this 4x4 Sudoku puzzle: [[3,*,*,2],[1,*,3,*],[*,1,*,3],[4,*,*,1]] where * represents a cell to be filled`

assistant: Let's approach this Sudoku puzzle using a guided tree-of-thought method:

Step 1: Analyze the given numbers
- We have 3, 2, 1, 3, 1, 3, 4, 1 already placed
- Missing numbers in each row/column/box must be from 1, 2, 3, 4

Step 2: Start filling obvious cells
[Branch 1] Fill (1,2) - only 4 is possible
[[3,4,*,2],[1,*,3,*],[*,1,*,3],[4,*,*,1]]

[Branch 2] Fill (4,2) - only 2 is possible
[[3,4,*,2],[1,*,3,*],[*,1,*,3],[4,2,*,1]]

Evaluation: Both branches are valid. Let's continue with Branch 2 as it's more constrained.

Step 3: Continue filling
[Branch 2.1] Fill (2,2) - only 2 is possible
[[3,4,*,2],[1,2,3,*],[*,1,*,3],[4,2,*,1]]

[Branch 2.2] Fill (3,1) - only 2 is possible
[[3,4,*,2],[1,2,3,*],[2,1,*,3],[4,2,*,1]]

Evaluation: Both sub-branches are valid. Continue with Branch 2.2.

Step 4: Complete the puzzle
Final solution:
[[3,4,1,2],
 [1,2,3,4],
 [2,1,4,3],
 [4,3,2,1]]

The 4x4 Sudoku puzzle has been solved using the guided tree-of-thought approach.

user: ``Design a simple recipe for a vegetarian pasta dish using ingredients commonly found in a home kitchen.``

assistant: Let's design a vegetarian pasta recipe using a guided tree-of-thought approach:

Step 1: Choose base ingredients
[Branch 1] Pasta type
- 1.1 Spaghetti
- 1.2 Penne
- 1.3 Fusilli

Evaluation: Let's go with 1.2 Penne for its ability to hold sauce well.

[Branch 2] Main vegetable
- 2.1 Tomatoes
- 2.2 Spinach
- 2.3 Zucchini

Evaluation: 2.1 Tomatoes are common and versatile. Let's choose this.

Step 2: Decide on a sauce base
[Branch 3] Sauce type
- 3.1 Tomato-based
- 3.2 Olive oil-based
- 3.3 Cream-based

Evaluation: Since we chose tomatoes as the main vegetable, let's go with 3.2 Olive oil-based for variety.

Step 3: Select additional flavors
[Branch 4] Herbs and spices
- 4.1 Basil and garlic
- 4.2 Oregano and red pepper flakes
- 4.3 Parsley and lemon zest

Evaluation: 4.1 Basil and garlic complement the tomatoes well.

Step 4: Choose a protein source
[Branch 5] Protein
- 5.1 Chickpeas
- 5.2 Nuts (e.g., pine nuts or walnuts)
- 5.3 No additional protein

Evaluation: 5.1 Chickpeas add protein and are common in pantries.

Final Recipe:
Penne with Tomatoes, Chickpeas, and Basil

Ingredients:
- 8 oz penne pasta
- 2 tbsp olive oil
- 2 cloves garlic, minced
- 1 pint cherry tomatoes, halved
- 1 can chickpeas, drained and rinsed
- 1/4 cup fresh basil, chopped
- Salt and pepper to taste
- Grated Parmesan cheese (optional)

Instructions:
1. Cook penne according to package instructions.
2. In a large skillet, heat olive oil over medium heat.
3. Add minced garlic and cook until fragrant, about 1 minute.
4. Add cherry tomatoes and cook until they start to soften, about 5 minutes.
5. Add chickpeas and cook for another 2-3 minutes.
6. Drain pasta and add to the skillet. Toss to combine.
7. Remove from heat and stir in chopped basil.
8. Season with salt and pepper to taste.
9. Serve with grated Parmesan cheese if desired.

This recipe was designed using a guided tree-of-thought approach, considering common ingredients and making decisions at each step.