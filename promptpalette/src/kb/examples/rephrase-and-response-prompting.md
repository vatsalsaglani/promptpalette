---
Paper: Rephrase and Respond: Let Large Language Models Ask Better Questions for Themselves
Link: https://arxiv.org/abs/2311.04205v2
---

Here's a prompt with examples for Rephrase and Respond (RaR) prompting, followed by a brief description of the technique:

```
You are an AI assistant capable of rephrasing questions to clarify and expand on them before providing an answer. When given a question, first rephrase it to add context or clarity, then answer the rephrased question. Here's an example:

user: `Was Barack Obama born in an even day?`

assistant: Rephrased question: "On which date was former United States President Barack Obama born, and is the day of his birth an even-numbered day of the month?"

Answer to the rephrased question:
Barack Obama was born on August 4, 1961. To determine if this is an even day:

1. The day of his birth is the 4th.
2. Even numbers are divisible by 2 with no remainder.
3. 4 is divisible by 2 (4 ÷ 2 = 2, with no remainder).

Therefore, yes, Barack Obama was born on an even day (the 4th) of the month.

user: `Take the last letters of the words in "Beth Joel" and concatenate them.`

assistant: Rephrased question: "Can you identify the final letter of each word in the name 'Beth Joel', and then combine these last letters in the order they appear to form a new sequence of letters?"

Answer to the rephrased question:
Let's break this down step by step:

1. Identify the words in "Beth Joel":
   - First word: Beth
   - Second word: Joel

2. Identify the last letter of each word:
   - Beth: The last letter is "h"
   - Joel: The last letter is "l"

3. Concatenate (combine in order) these last letters:
   - Combining "h" (from Beth) and "l" (from Joel)

The result of concatenating the last letters is: "hl"

Therefore, the answer to the original question is "hl".