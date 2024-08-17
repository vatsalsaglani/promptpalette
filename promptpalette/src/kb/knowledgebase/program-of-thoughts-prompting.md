---
Paper: Program of thoughts prompting - Disentangling computation from reasoning for numerical reasoning tasks
Link: https://arxiv.org/abs/2211.12588
---

Examples of Program of Thoughts (PoT) prompting mentioned in the paper:

1. Solving a linear equation:
```python
interest_rate = Symbol('interest_rate')
sum_in_two_years_with_XXX_interest = 20000 * (1 + interest_rate)**3 - 2000
solve(sum_in_two_years_with_XXX_interest - interest_rate * 20000 * 3 - 1000, interest_rate)
```

2. Iterative calculation:
```python
total_cost = 90
cost_of_watering_and_feeding = 3
cost_of_each_lemon = 1.5
num_of_lemon_per_year = 7
ans = 0
while total_cost > 0:
    total_cost += cost_of_watering_and_feeding
    total_cost -= num_of_lemon_per_year * cost_of_each_lemon
    ans += 1
```

Essence of Program of Thoughts (PoT) prompting:

PoT is a technique that uses language models to generate Python code to solve complex numerical reasoning tasks. It separates the reasoning process from the computation, allowing for more accurate and efficient problem-solving.

Key ideas:
1. Disentangle computation from reasoning
2. Use programming language (Python) to express thoughts
3. Leverage external tools (Python interpreter) for computation
4. Break down complex problems into steps
5. Bind semantic meanings to variable names

Use cases:
1. Math word problems
2. Financial calculations
3. Scientific computations
4. Data analysis tasks
5. Any problem requiring multi-step numerical reasoning

Additional examples of PoT prompting:

1. Calculating compound interest:
```python
principal = 1000
rate = 0.05
years = 5
compound_interest = principal * (1 + rate)**years - principal
ans = compound_interest
```

2. Solving a quadratic equation:
```python
from sympy import Symbol, solve
x = Symbol('x')
equation = x**2 + 5*x + 6
solution = solve(equation)
ans = solution
```

3. Calculating the area of a complex shape:
```python
import math

rectangle_length = 10
rectangle_width = 5
circle_radius = 2

rectangle_area = rectangle_length * rectangle_width
circle_area = math.pi * circle_radius**2
total_area = rectangle_area + circle_area
ans = total_area
```