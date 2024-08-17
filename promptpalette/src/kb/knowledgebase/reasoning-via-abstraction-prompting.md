---
Paper: Take a Step Back: Evoking Reasoning via Abstraction in Large Language Models
Link: https://arxiv.org/abs/2310.06117v2
---

The "Take a step back" or "Step-Back Prompting" technique described in this paper is an approach to improve reasoning in large language models by encouraging abstraction before tackling specific problems. Here's a summary of the key aspects:

Essence of the technique:
1. Abstraction: Instead of directly addressing a question, the model is prompted to ask a more generic "step-back" question about a higher-level concept or principle related to the original question.
2. Reasoning: Using the retrieved high-level concepts or principles, the model then reasons about the solution to the original question.

Idea behind it:
The technique is inspired by how humans often approach complex problems by first considering general principles before diving into specifics. This helps in grounding the reasoning process and reducing errors in intermediate steps.

What it does:
1. Improves model performance on complex reasoning tasks
2. Reduces errors by providing a broader context for problem-solving
3. Enables more reliable retrieval of relevant information
4. Helps models to focus on key concepts rather than getting lost in details

Use cases:
1. STEM problems (e.g., physics, chemistry)
2. Knowledge-intensive question answering
3. Multi-hop reasoning tasks
4. Time-sensitive queries
5. Complex problem-solving in various domains

Examples from the paper:

1. MMLU Physics:
Original question: "What happens to the pressure, P, of an ideal gas if the temperature is increased by a factor of 2 and the volume is increased by a factor of 8?"
Step-back question: "What are the physics principles behind this question?"

2. TimeQA:
Original question: "Who was the spouse of Anna Karina from 1968 to 1974?"
Step-back question: "What was Anna Karina's education history?"

3. StrategyQA:
Original question: "Would a Monoamine Oxidase candy bar cheer up a depressed friend?"
Step-back question: "What are the effects of Monoamine Oxidase?"

Additional examples of Step-Back Prompting:

1. Math Problem Solving:
Original question: "A rectangle has a length that is 3 units longer than its width. If the perimeter of the rectangle is 26 units, what is its area?"
Step-back question: "What are the key formulas and concepts for solving rectangle problems?"

2. Historical Analysis:
Original question: "How did the Treaty of Versailles contribute to the outbreak of World War II?"
Step-back question: "What were the major political and economic consequences of World War I?"

3. Literary Interpretation:
Original question: "What does the green light symbolize in F. Scott Fitzgerald's 'The Great Gatsby'?"
Step-back question: "What are common themes and symbols in American literature of the 1920s?"