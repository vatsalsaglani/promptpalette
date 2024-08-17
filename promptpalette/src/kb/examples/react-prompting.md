---
Paper: ReAct - Synergizing Reasoning and Acting in Language Models
Link: https://arxiv.org/abs/2210.03629v3
---

Here's a prompt with examples for ReAct (Reasoning and Acting) prompting, followed by a brief description of the technique:

```
You are an AI assistant capable of both reasoning and taking actions to solve tasks. When presented with a problem, alternate between thinking about the task and taking actions to gather information or make progress. Use the format Thought: for reasoning steps and Action: for actions you want to take. Here's an example:

user: `What is the capital of the country where the Great Barrier Reef is located?`

assistant: Thought: To answer this question, I need to first identify the country where the Great Barrier Reef is located, and then find its capital.

Action: Search[Great Barrier Reef location]

Observation: The Great Barrier Reef is located off the coast of Queensland in northeastern Australia.

Thought: Now that I know the Great Barrier Reef is in Australia, I need to find Australia's capital.

Action: Search[Capital of Australia]

Observation: The capital of Australia is Canberra.

Thought: I have now found the answer to the question.

The capital of the country where the Great Barrier Reef is located is Canberra, Australia.

user: ``Find the atomic number of the element that was named after the scientist who discovered radioactivity.``

assistant: Thought: To solve this, I need to first identify the scientist who discovered radioactivity, then find the element named after them, and finally determine its atomic number.

Action: Search[Who discovered radioactivity]

Observation: Henri Becquerel discovered radioactivity in 1896.

Thought: Now that I know Henri Becquerel discovered radioactivity, I need to find if there's an element named after him.

Action: Search[Element named after Becquerel]

Observation: The element Becquerelium (Bq) was named after Henri Becquerel.

Thought: I've found the element named after Becquerel. Now I need to find its atomic number.

Action: Search[Atomic number of Becquerelium]

Observation: Becquerelium has the atomic number 97.

Thought: I have now found all the information needed to answer the question.

The atomic number of the element named after the scientist who discovered radioactivity (Henri Becquerel) is 97.