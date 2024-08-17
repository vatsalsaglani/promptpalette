---
Paper: Active Prompting with Chain-of-Thought for Large Language Models
Link: https://arxiv.org/abs/2302.12246v5
---

Here's a prompt with examples for Active Prompting with Chain-of-Thought (Active-Prompt CoT), followed by a brief description of the technique:

```
You are an AI assistant capable of solving complex reasoning tasks using the Active-Prompt Chain-of-Thought method. When presented with a problem, break it down into steps and provide detailed reasoning. Here's an example:

user: `Josh and Anna were both born on August 17th, but in different years. To consolidate celebrations they also got married on August 17 when Josh turned 22. If today they're celebrating 30 years of marriage and their combined age is exactly 5 times what Josh's age was when they married, how old was Anna when they got married?`

assistant: Let's break this problem down step by step:

1. Josh's age when they got married:
   Josh was 22 when they got married.

2. Josh's current age:
   They've been married for 30 years, so Josh is now 22 + 30 = 52 years old.

3. Their combined current age:
   Their combined age is 5 times Josh's age when they married: 5 * 22 = 110 years

4. Anna's current age:
   Combined age - Josh's current age = 110 - 52 = 58 years

5. Anna's age when they got married:
   Anna's current age - Years of marriage = 58 - 30 = 28 years

Therefore, Anna was 28 years old when they got married.

user: `Where would you find a sloth that is not afraid of being hunted?`

assistant: Let's think through this step-by-step:

1. Natural habitat of sloths:
   Sloths are typically found in tropical rainforests in Central and South America.

2. Sloth behavior in the wild:
   In their natural habitat, sloths may be hunted by predators or humans, so they would typically be cautious.

3. Conditions for a sloth not afraid of being hunted:
   We need a place where:
   a) Sloths are present
   b) Hunting is not allowed or doesn't occur

4. Potential locations:
   a) Zoos: Have sloths and protect them from hunting
   b) Wildlife sanctuaries: Provide safe environments for animals
   c) Rehabilitation centers: Care for injured or rescued sloths

5. Most likely answer:
   Among these options, a zoo is the most common and accessible place where you'd find a sloth not afraid of being hunted.

Therefore, you would most likely find a sloth that is not afraid of being hunted in a zoo.

user: Ok now I want you to give me the details of this technique within 100 words