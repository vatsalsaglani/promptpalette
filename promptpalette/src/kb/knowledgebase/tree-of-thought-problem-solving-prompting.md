---
Paper: Tree of Thoughts: Deliberate Problem Solving with Large Language Models
Link: https://arxiv.org/abs/2305.10601v2
---

Based on the paper, here is a summary of the Tree of Thoughts (ToT) prompting technique:

Examples mentioned in the paper:
1. Game of 24: Using 4 numbers and basic arithmetic operations to obtain 24.
2. Creative Writing: Generating a coherent 4-paragraph passage ending with 4 given random sentences.
3. Mini Crosswords: Solving 5x5 crossword puzzles.

Essence of Tree of Thoughts (ToT) prompting:

ToT is a framework that enhances problem-solving capabilities of large language models (LLMs) by implementing a tree-like thought process with backtracking. It augments LLMs with additional modules to enable multi-round conversations and exploration of solution spaces.

Key ideas:
1. Inspired by human problem-solving through trial and error
2. Explores solution space through a tree-like thought process
3. Allows backtracking when necessary
4. Implements multi-round conversations between the LLM and additional modules
5. Combines "short-range reasoning" capabilities of LLMs with enhanced "long-range reasoning" through exploration and backtracking

What it does:
1. Decomposes problems into intermediate thought steps
2. Generates multiple candidate thoughts at each step
3. Evaluates the progress and promise of different thought paths
4. Implements search algorithms (e.g., breadth-first search, depth-first search) to explore the tree of thoughts
5. Allows for lookahead and backtracking in the reasoning process

Use cases:
1. Complex mathematical reasoning (e.g., Game of 24)
2. Creative tasks requiring high-level planning (e.g., Creative Writing)
3. Puzzle-solving (e.g., Crosswords)
4. Multi-step problem-solving in various domains
5. Tasks requiring deliberate decision-making and strategic thinking

Examples of prompting with ToT:

1. Game of 24:
User: "Solve the Game of 24 using these numbers: 4, 9, 10, 13"

ToT system:
a) Thought generator: "Let's consider different ways to combine these numbers. Possible first steps: 4 + 9 = 13 (left: 10, 13), 13 - 9 = 4 (left: 4, 10), 10 - 4 = 6 (left: 6, 9, 13)..."
b) State evaluator: "Evaluating each possibility: 13 and 10 can easily reach 24 (13 + 11), so the first option is promising. The second option leaves us with small numbers, making it harder. The third option is also promising as 6 * 4 = 24..."
c) Search algorithm: Explores promising paths, potentially backtracking if needed.

2. Creative Writing:
User: "Write a coherent 4-paragraph passage ending with these sentences: 1) It isn't difficult to do a handstand if you just stand on your hands. 2) It caught him off guard that space smelled of seared steak. 3) When she didn't like a guy who was trying to pick her up, she started using sign language. 4) Each person who knows you has a different perception of who you are."

ToT system:
a) Thought generator: "Possible themes: 1) Circus performer's life, 2) Astronaut's unexpected experiences, 3) Creative ways to avoid unwanted attention, 4) The nature of personal identity"
b) State evaluator: "Theme 2 seems most promising as it can naturally incorporate all four sentences..."
c) Search algorithm: Explores the chosen theme, generating and evaluating multiple paragraph ideas.

3. Mini Crosswords:
User: "Solve this 5x5 crossword puzzle with clues: Across: 1) Presented, 5) Aussie tree..."

ToT system:
a) Thought generator: "Possible words for 1 Across: 'Shown', 'Given', 'Offered'..."
b) State evaluator: "Let's try 'Shown' as it fits well and leaves possibilities for intersecting Down clues..."
c) Search algorithm: Uses depth-first search to explore word combinations, backtracking when necessary.

In each example, ToT would engage in multiple rounds of thought generation, evaluation, and search to solve the problem, potentially backtracking and exploring alternative paths as needed.