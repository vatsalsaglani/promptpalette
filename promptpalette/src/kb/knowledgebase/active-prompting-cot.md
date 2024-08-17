---
Paper: Active Prompting with Chain-of-Thought for Large Language Models
Link: https://arxiv.org/abs/2302.12246v5
---

Thank you for providing that paper on Active Prompting with Chain-of-Thought for Large Language Models. I'll summarize the key aspects and provide some examples as requested.

Essence of Active Prompting with Chain-of-Thought:

Active Prompting with Chain-of-Thought (Active-Prompt) is an enhancement to the traditional Chain-of-Thought (CoT) prompting method for large language models. The core idea is to actively select the most informative and helpful examples to annotate with reasoning steps, rather than using a fixed set of human-annotated examples.

Key ideas:
1. Uses uncertainty-based metrics to select the most informative questions for annotation
2. Incorporates both question selection and human annotation of reasoning steps
3. Aims to improve model performance on complex reasoning tasks
4. Can be applied with or without initial few-shot examples
5. Compatible with other techniques like self-consistency

The method works by:
1. Estimating uncertainty for a pool of questions (using metrics like disagreement or entropy)
2. Selecting the most uncertain questions for human annotation
3. Using the annotated examples as prompts for inference on new questions

Use cases:
- Arithmetic reasoning tasks
- Commonsense reasoning 
- Symbolic reasoning
- Any complex task requiring multi-step reasoning

Examples of Active Prompting with Chain-of-Thought:

1. Arithmetic reasoning:

Question: Josh and Anna were both born on August 17th, but in different years. To consolidate celebrations they also got married on August 17 when Josh turned 22. If today they're celebrating 30 years of marriage and their combined age is exactly 5 times what Josh's age was when they married, how old was Anna when they got married?

Active-Prompt annotated answer: Let's think step by step:
1. Josh was 22 when they got married
2. They've been married for 30 years, so Josh is now 22 + 30 = 52 years old
3. Their combined age is 5 times Josh's age when they married: 5 * 22 = 110 years
4. Anna's current age = Combined age - Josh's current age = 110 - 52 = 58 years
5. Anna's age when they got married = Current age - Years of marriage = 58 - 30 = 28 years

Therefore, Anna was 28 years old when they got married.

2. Commonsense reasoning:

Question: Where would you find a sloth that is not afraid of being hunted?

Active-Prompt annotated answer: Let's think through this step-by-step:
1. Sloths are typically found in tropical rainforests in Central and South America.
2. In their natural habitat, sloths may be hunted by predators or humans.
3. To find a sloth not afraid of being hunted, we need a place where:
   a) Sloths are present
   b) Hunting is not allowed or doesn't occur
4. Among the given options, a "zoo" meets both criteria:
   a) Zoos often have sloths as part of their exhibits
   b) Animals in zoos are protected from hunting

Therefore, you would find a sloth that is not afraid of being hunted in a zoo.

3. Symbolic reasoning:

Question: Take the last letters of the words in "Willie Valeria Zane" and concatenate them.

Active-Prompt annotated answer: Let's approach this step-by-step:
1. Break down the name into individual words:
   - Willie
   - Valeria
   - Zane
2. Identify the last letter of each word:
   - Willie -> e
   - Valeria -> a
   - Zane -> e
3. Concatenate these letters in order:
   e + a + e = eae

Therefore, the answer is "eae".

These examples demonstrate how Active-Prompt selects informative questions and provides detailed, step-by-step reasoning, which can then be used to guide the language model in solving similar problems.