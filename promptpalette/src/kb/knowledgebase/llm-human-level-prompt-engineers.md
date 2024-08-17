---
Paper: Large Language Models Are Human-Level Prompt Engineers
Link: https://arxiv.org/abs/2211.01910v2
---

Examples of Automatic Prompt Engineer (APE) from the paper:

1. For the MMLU Physics task:
Original question: "What happens to the pressure, P, of an ideal gas if the temperature is increased by a factor of 2 and the volume is increased by a factor of 8?"
Step-back question: "What are the physics principles behind this question?"

2. For the TimeQA task:
Original question: "Who was the spouse of Anna Karina from 1968 to 1974?"
Step-back question: "What was Anna Karina's education history?"

3. For Zero-Shot Chain of Thought:
APE-generated prompt: "Let's work this out in a step by step way to be sure we have the right answer."

Essence of Automatic Prompt Engineer (APE):

APE is an automated method for generating and selecting effective instructions for language models. It treats instruction generation as a natural language program synthesis problem and uses large language models (LLMs) to generate, evaluate, and refine instructions.

Key ideas:
1. Use LLMs to generate candidate instructions based on task demonstrations
2. Evaluate instructions using a scoring function (e.g., execution accuracy)
3. Iteratively refine instructions through a Monte Carlo search process

What it does:
1. Generates a pool of candidate instructions for a given task
2. Evaluates the effectiveness of these instructions using a chosen metric
3. Selects the best-performing instruction for the task

Use cases:
1. Improving zero-shot and few-shot learning performance on various NLP tasks
2. Finding better prompts for chain-of-thought reasoning
3. Steering language models towards desired behaviors (e.g., truthfulness, informativeness)
4. Automating prompt engineering for specialized tasks

Examples of prompting with APE:

1. Math problem-solving:
Original question: "A rectangle has a length that is 3 units longer than its width. If the perimeter of the rectangle is 26 units, what is its area?"
APE-generated instruction: "Let's break this problem down into steps. First, identify the given information and the unknown variables. Then, use geometric formulas to set up equations and solve for the missing values."

2. Sentiment analysis:
Original task: Determine the sentiment of movie reviews.
APE-generated instruction: "Analyze the overall tone of the given text. Look for key positive or negative words and phrases. Consider the context and any sarcasm. Classify the sentiment as either 'positive' or 'negative' based on your analysis."

3. Language translation:
Original task: Translate English sentences to French.
APE-generated instruction: "For each input sentence, provide an accurate French translation that preserves the original meaning, tone, and context. Pay attention to idiomatic expressions and cultural nuances when translating."