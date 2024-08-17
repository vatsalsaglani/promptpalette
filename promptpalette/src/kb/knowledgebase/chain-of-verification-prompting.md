---
Paper: Chain-of-Verification Reduces Hallucination in Large Language Models
Link: https://arxiv.org/abs/2309.11495v2
---

Examples of Chain-of-Verification (CoVe) prompting mentioned in the paper:

1. List-based question:
Query: "Who are some politicians who were born in NY, New York?"
Baseline Response: Lists politicians including Hillary Clinton and Michael Bloomberg (which are incorrect).
CoVe: Generates verification questions like "Where was Hillary Clinton born?", "Where was Michael Bloomberg born?", etc. Then answers these questions independently and produces a corrected final response.

2. Longform generation (biography):
Query: "Tell me a bio of <person>"
Baseline Response: Generates a biography that may contain factual errors.
CoVe: Breaks down the biography into facts, generates verification questions for each fact, answers them independently, and then produces a revised biography with corrected information.

3. Closed-book QA:
Query: "What was the primary cause of the Mexican-American war?"
Baseline Response: Generates an answer that may contain incorrect dates or facts.
CoVe: Generates verification questions like "When did the Mexican American war start and end?", "When did the US annex Texas?", etc. Answers these questions and produces a revised response based on the verified information.

Essence of Chain-of-Verification (CoVe) prompting:

CoVe is a method designed to reduce hallucinations in large language models by implementing a self-verification process. The key idea is to have the model deliberate on its own responses and self-correct them through a series of steps.

Key aspects:
1. Generation of initial response
2. Planning verification questions
3. Independent execution of verifications
4. Generation of final verified response

The core principle is that models tend to answer specific, focused questions more accurately than they generate longform content. By breaking down the initial response into smaller, verifiable facts, CoVe improves the overall accuracy of the final output.

Use cases:
1. Fact-based question answering
2. Longform text generation (e.g., biographies, historical accounts)
3. List-based queries (e.g., entities with specific attributes)
4. Closed-book knowledge tasks
5. Any task prone to factual hallucinations

Additional examples of CoVe prompting:

1. Scientific explanation:
Query: "Explain the process of photosynthesis."
CoVe: Generate an initial explanation, then create verification questions like "What are the reactants in photosynthesis?", "What is the role of chlorophyll?", etc. Answer these independently and produce a verified explanation.

2. Historical event description:
Query: "Describe the events of the French Revolution."
CoVe: Produce an initial description, generate verification questions such as "When did the French Revolution begin?", "Who was the king of France at the time?", etc. Verify these facts and create a revised, more accurate description.