---
Paper: Self-Consistency Improves Chain of Thought Reasoning in Language Models
Link: https://arxiv.org/abs/2203.11171v4
---

Here's a prompt with examples for Self-Consistency Chain-of-Thought (CoT) prompting, followed by a brief description of the technique:

```
You are an AI assistant capable of generating multiple reasoning paths for complex problems. When presented with a question, generate at least three different reasoning approaches, then determine the most consistent answer across all paths. Here's an example:

user: `A store has a "Buy 2, Get 1 Free" promotion on books. Each book costs $12. If John buys 7 books, how much will he pay?`

assistant: I'll approach this problem in three different ways:

Approach 1:
1. Group books into sets of 3: 7 books = 2 full sets of 3 + 1 leftover book
2. Calculate cost for full sets: 2 sets × (2 × $12) = $48
3. Add cost of leftover book: $48 + $12 = $60
Total cost: $60

Approach 2:
1. Calculate total books John pays for: 7 - (7 ÷ 3) = 7 - 2 = 5 books
2. Multiply paid books by price: 5 × $12 = $60
Total cost: $60

Approach 3:
1. Calculate cost without promotion: 7 × $12 = $84
2. Calculate discount: (7 ÷ 3) rounded down × $12 = 2 × $12 = $24
3. Subtract discount from total: $84 - $24 = $60
Total cost: $60

All three approaches consistently yield $60 as the final answer. Therefore, John will pay $60 for 7 books under the "Buy 2, Get 1 Free" promotion.

user: ``Three friends split a restaurant bill. The total bill was $120, including a 20% tip. They agreed that Alice would pay 40% of the bill before tip, Bob would pay 35%, and Charlie would pay the rest. How much did each person pay?``

assistant: I'll approach this problem using three different methods:

Approach 1: Calculate individual contributions based on pre-tip bill
1. Calculate pre-tip bill: $120 ÷ 1.20 = $100
2. Calculate tip amount: $120 - $100 = $20
3. Calculate individual contributions:
   Alice: (40% × $100) + (40% × $20) = $40 + $8 = $48
   Bob: (35% × $100) + (35% × $20) = $35 + $7 = $42
   Charlie: (25% × $100) + (25% × $20) = $25 + $5 = $30
Total: $48 + $42 + $30 = $120

Approach 2: Calculate total individual percentages including tip
1. Alice's percentage of total bill: 40% × 1.20 = 48%
   Alice's payment: 48% × $120 = $57.60
2. Bob's percentage of total bill: 35% × 1.20 = 42%
   Bob's payment: 42% × $120 = $50.40
3. Charlie's percentage of total bill: 25% × 1.20 = 30%
   Charlie's payment: 30% × $120 = $36
Total: $57.60 + $50.40 + $36 = $144 (incorrect)

Approach 3: Calculate individual contributions and split the tip evenly
1. Calculate pre-tip contributions:
   Alice: 40% × $100 = $40
   Bob: 35% × $100 = $35
   Charlie: 25% × $100 = $25
2. Split tip evenly: $20 ÷ 3 ≈ $6.67 each
3. Add tip to individual contributions:
   Alice: $40 + $6.67 = $46.67
   Bob: $35 + $6.67 = $41.67
   Charlie: $25 + $6.67 = $31.67
Total: $46.67 + $41.67 + $31.67 ≈ $120 (with rounding)

Analyzing the results:
Approach 1 and Approach 3 yield similar results and add up to the correct total of $120. Approach 2 is incorrect as it results in a total higher than the bill amount.

Consistent answer:
Alice paid approximately $48
Bob paid approximately $42
Charlie paid approximately $30

These amounts are most consistent across the correct approaches and sum to the total bill of $120.