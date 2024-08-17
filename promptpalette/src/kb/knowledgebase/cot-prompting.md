---
Paper: Chain-of-Thought Prompting Elicits Reasoning in Large Language Models
Link: https://arxiv.org/abs/2201.11903v6
---

The essence of the Chain-of-Thought (CoT) prompting technique is:

Key ideas:
1. Prompts the language model to generate intermediate reasoning steps before providing a final answer
2. Allows models to break down complex problems into smaller, more manageable steps
3. Enables more computation and reasoning for challenging tasks
4. Emerges as an ability in sufficiently large language models (typically 100B+ parameters)

What it does:
- Guides the model to produce a series of coherent reasoning steps leading to the final answer
- Improves performance on tasks requiring multi-step reasoning, like math word problems and commonsense reasoning
- Provides interpretable rationales for the model's answers
- Facilitates generalization to more complex problems than seen in training

Use cases:
- Arithmetic reasoning and math word problems
- Commonsense reasoning tasks
- Symbolic manipulation
- Multi-step problem-solving in various domains
- Tasks that benefit from step-by-step reasoning processes

Examples from the paper:

1. Math word problem:

Q: Roger has 5 tennis balls. He buys 2 more cans of tennis balls. Each can has 3 tennis balls. How many tennis balls does he have now?

A: Roger started with 5 balls. 2 cans of 3 tennis balls each is 6 tennis balls. 5 + 6 = 11. The answer is 11.

2. Commonsense reasoning (CSQA):

Q: When a person is beginning work, what are they building?
Answer Choices: (a) time (b) accomplishing (c) working (d) momentum (e) tiredness

A: The answer must be something that is built. Of the above choices, only momentum is built. So the answer is (d).

3. Symbolic reasoning (Last letter concatenation):

Q: Take the last letters of the words in "Elon Musk" and concatenate them.

A: The last letter of "Elon" is "n". The last letter of "Musk" is "k". Concatenating them is "nk". The answer is nk.

These examples demonstrate how CoT prompting guides the model through a step-by-step reasoning process, breaking down complex problems into more manageable steps and providing a clear rationale for the final answer.