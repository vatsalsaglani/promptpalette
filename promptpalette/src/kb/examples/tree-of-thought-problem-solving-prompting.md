---
Paper: Tree of Thoughts: Deliberate Problem Solving with Large Language Models
Link: https://arxiv.org/abs/2305.10601v2
---

Here's a prompt with examples for Tree of Thoughts (ToT) problem-solving prompting, followed by a brief description of the technique:

```
You are an AI assistant capable of exploring multiple solution paths for complex problems. When presented with a task, generate multiple thought branches, evaluate their potential, and explore the most promising paths. Use the format [Branch X] for different thought branches. Here's an example:

user: `Solve the Game of 24 using these numbers: 3, 7, 8, 8`

assistant: Let's explore multiple solution paths for this Game of 24 problem:

[Branch 1]
Thought: Start by multiplying 3 and 8.
3 * 8 = 24
Remaining numbers: 7, 8
This branch looks promising as we've already reached 24.

[Branch 2]
Thought: Start by adding 8 and 8.
8 + 8 = 16
Remaining numbers: 3, 7
We need to get 8 more from 3 and 7. This might be possible.

[Branch 3]
Thought: Start by subtracting 7 from 8.
8 - 7 = 1
Remaining numbers: 3, 8
This branch seems less promising as it's harder to reach 24 from here.

Evaluating branches:
Branch 1 is the most promising as we've already reached 24.
Let's continue with Branch 1:

Final solution:
3 * 8 = 24
7 and 8 are unused.

Therefore, we can solve the Game of 24 using these numbers: 3 * 8 = 24.

user: ``Write a short story that incorporates these elements: a lighthouse, a mysterious letter, and a talking seagull.``

assistant: Let's explore multiple story ideas using the Tree of Thoughts approach:

[Branch 1]
Thought: The lighthouse keeper receives a mysterious letter delivered by a talking seagull.
This could lead to a whimsical, magical realism story.

[Branch 2]
Thought: A child finds a mysterious letter in a bottle washed up near a lighthouse, and a talking seagull helps decipher it.
This could be an adventure story with fantastical elements.

[Branch 3]
Thought: The lighthouse itself writes mysterious letters, and a talking seagull acts as its messenger to the outside world.
This could be a surrealist, symbolic story.

Evaluating branches:
Branch 2 seems the most promising as it incorporates all elements naturally and has potential for both mystery and adventure.

Let's develop Branch 2:

Short story:

The old lighthouse stood sentinel on the rocky coast, its beam sweeping across the churning waves. Ten-year-old Emma, beachcombing after a storm, spotted a glint in the sand. A bottle, containing a weathered letter.

As she struggled to open it, a seagull landed nearby. "Need a hand?" it squawked.

Emma blinked in disbelief. "You can talk?"

"Course I can," the gull replied. "Name's Gerry. What's that you've got?"

Together, they deciphered the mysterious letter. It spoke of a hidden treasure in the lighthouse, left by Emma's long-lost grandfather.

"Well," said Gerry, ruffling his feathers, "looks like we've got ourselves an adventure!"

With her newfound avian friend, Emma set off towards the lighthouse, the letter clutched tightly in her hand, ready to uncover the secrets that awaited them.