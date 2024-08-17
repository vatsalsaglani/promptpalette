---
Paper: Enhancing Zero-Shot Chain-of-Thought Reasoning in Large Language Models through Logic
Link: https://arxiv.org/abs/2309.13339v4
---

Based on the paper, here is a summary of the Logical Thoughts (LoT) prompting technique:

Examples mentioned in the paper:
1. Math reasoning tasks: GSM8K and AQuA datasets
2. Commonsense reasoning tasks: DateUnderstanding and OddOneOut
3. Causal inference tasks: CauseEffect and ShuffledObjects
4. Symbolic reasoning task: LastLetter 
5. Social interaction reasoning task: SocialQA

Essence of Logical Thoughts (LoT) prompting:

LoT is a self-improvement prompting framework that leverages principles from symbolic logic, particularly Reductio ad Absurdum, to systematically verify and rectify reasoning processes step by step in large language models.

Key ideas:
1. Integrates logical principles into the reasoning process
2. Verifies each reasoning step using a think-verify-revise loop
3. Generates post hoc explanations for both the original thought and its negation
4. Uses the language model to decide between conflicting explanations
5. Revises and adapts the reasoning chain based on verification results

What it does:
1. Decomposes complex problems into smaller, verifiable steps
2. Generates multiple potential thoughts for each reasoning step
3. Verifies the validity of each thought using logical principles
4. Revises incorrect or implausible thoughts
5. Adapts the reasoning chain based on verified thoughts
6. Produces more logically sound and robust reasoning chains

Use cases:
1. Enhancing zero-shot reasoning abilities of large language models
2. Improving performance on complex reasoning tasks across various domains
3. Detecting and correcting logical errors in reasoning processes
4. Handling tasks requiring multi-step reasoning and logical deduction
5. Improving model performance on math, commonsense, causal, symbolic, and social reasoning tasks

Examples of prompting with LoT:

1. Math reasoning (GSM8K dataset):
Human: Terry eats 2 yogurts a day. They are currently on sale at 4 yogurts for $5.00. How much does he spend on yogurt over 30 days?

LoT system:
Step 1: Calculate total yogurts needed for 30 days
Thought: Terry eats 2 yogurts per day, so for 30 days he needs 2 * 30 = 60 yogurts.
Verification: [Generate explanations for and against this thought, then verify]

Step 2: Calculate cost per yogurt
Thought: 4 yogurts cost $5.00, so each yogurt costs $5.00 / 4 = $1.25.
Verification: [Generate explanations for and against this thought, then verify]

Step 3: Calculate total cost
Thought: Terry needs 60 yogurts, each costing $1.25. Total cost is 60 * $1.25 = $75.00.
Verification: [Generate explanations for and against this thought, then verify]

Final Answer: Terry spends $75.00 on yogurt over 30 days.

2. Date Understanding:
Human: Jane and John married on Jan 2, 1958. Today is their golden wedding anniversary. What is the date one week ago from today in MM/DD/YYYY?

LoT system:
Step 1: Determine the current date
Thought: A golden wedding anniversary is 50 years after marriage. So today's date is Jan 2, 2008.
Verification: [Generate explanations for and against this thought, then verify]

Step 2: Calculate the date one week ago
Thought: One week ago from Jan 2, 2008 would be Dec 26, 2007.
Verification: [Generate explanations for and against this thought, then verify]

Final Answer: The date one week ago from today in MM/DD/YYYY format is 12/26/2007.

3. Symbolic reasoning (LastLetter task):
Human: What is the last letter of each word in "apple banana cherry" concatenated?

LoT system:
Step 1: Identify last letter of "apple"
Thought: The last letter of "apple" is "e".
Verification: [Generate explanations for and against this thought, then verify]

Step 2: Identify last letter of "banana"
Thought: The last letter of "banana" is "a".
Verification: [Generate explanations for and against this thought, then verify]

Step 3: Identify last letter of "cherry"
Thought: The last letter of "cherry" is "y".
Verification: [Generate explanations for and against this thought, then verify]

Step 4: Concatenate the last letters
Thought: Concatenating "e", "a", and "y" gives "eay".
Verification: [Generate explanations for and against this thought, then verify]

Final Answer: The concatenated last letters are "eay".

In each example, LoT would generate and verify multiple thoughts for each step, potentially revising and adapting the reasoning chain based on the verification results.