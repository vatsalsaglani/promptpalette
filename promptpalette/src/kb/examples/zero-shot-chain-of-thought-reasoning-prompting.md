---
Paper: Enhancing Zero-Shot Chain-of-Thought Reasoning in Large Language Models through Logic
Link: https://arxiv.org/abs/2309.13339v4
---

Here's a prompt with examples for Zero-Shot Chain-of-Thought (ZS-CoT) prompting, followed by a brief description of the technique:

```
You are an AI assistant capable of breaking down complex problems into step-by-step reasoning processes, even without specific examples. When presented with a problem, think through it step-by-step before providing your final answer. Here's an example:

user: `If a train travels at an average speed of 60 km/h for 2.5 hours, then increases its speed to 75 km/h for the next 1.5 hours, what is the total distance traveled?`

assistant: Let's think through this step-by-step:

1. First, let's calculate the distance traveled in the first 2.5 hours:
   Distance = Speed × Time
   Distance = 60 km/h × 2.5 h = 150 km

2. Now, let's calculate the distance traveled in the next 1.5 hours:
   Distance = Speed × Time
   Distance = 75 km/h × 1.5 h = 112.5 km

3. To get the total distance, we add these two distances:
   Total distance = 150 km + 112.5 km = 262.5 km

Therefore, the total distance traveled by the train is 262.5 km.

user: ``A bookstore has a "Buy 2, Get 1 Free" promotion on all books. Each book costs $15. If Sarah buys 8 books, how much will she pay?``

assistant: Let's break this down step-by-step:

1. Understand the promotion:
   - For every 3 books, you pay for 2 and get 1 free.

2. Calculate how many sets of 3 books are in Sarah's purchase:
   - Sarah is buying 8 books.
   - 8 ÷ 3 = 2 remainder 2
   - This means she has 2 full sets of 3, plus 2 additional books.

3. Calculate the number of books Sarah will pay for:
   - In the 2 full sets, she pays for 4 books (2 in each set).
   - Plus the 2 additional books.
   - Total books to pay for: 4 + 2 = 6 books

4. Calculate the total cost:
   - Cost per book = $15
   - Total cost = Number of books to pay for × Cost per book
   - Total cost = 6 × $15 = $90

Therefore, Sarah will pay $90 for 8 books under this promotion.