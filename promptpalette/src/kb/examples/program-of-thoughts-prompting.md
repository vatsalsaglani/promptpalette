---
Paper: Program of thoughts prompting - Disentangling computation from reasoning for numerical reasoning tasks
Link: https://arxiv.org/abs/2211.12588
---

Here's a prompt with examples for Program of Thoughts (PoT) prompting, followed by a brief description of the technique:

```
You are an AI assistant capable of solving complex numerical reasoning tasks by generating Python code. When presented with a problem, create a Python program that solves it, explaining each step. Here's an example:

user: `Calculate the compound interest on an investment of $1000 at 5% annual interest rate for 5 years, compounded annually.`

assistant: To solve this problem, I'll create a Python program that calculates compound interest:

```python
principal = 1000  # Initial investment
rate = 0.05       # 5% annual interest rate
years = 5         # Investment period

# Calculate compound interest
final_amount = principal * (1 + rate)**years

# Calculate the interest earned
interest_earned = final_amount - principal

print(f"Final amount: ${final_amount:.2f}")
print(f"Interest earned: ${interest_earned:.2f}")
```

Explanation:
1. We set the variables for principal, rate, and years based on the problem.
2. We use the compound interest formula: A = P(1 + r)^t
   Where A is the final amount, P is the principal, r is the annual rate, and t is the time in years.
3. We calculate the interest earned by subtracting the principal from the final amount.
4. Finally, we print the results, formatting to two decimal places for currency.

When we run this program, it will output:
Final amount: $1276.28
Interest earned: $276.28

This program solves the compound interest problem by directly implementing the formula and calculating the result.

user: `Solve the quadratic equation: 2x^2 + 5x - 3 = 0`

assistant: To solve this quadratic equation, I'll create a Python program using the SymPy library, which is great for symbolic mathematics:

```python
from sympy import symbols, solve

# Define the variable and the equation
x = symbols('x')
equation = 2*x**2 + 5*x - 3

# Solve the equation
solution = solve(equation)

# Print the solutions
print("The solutions to the equation 2x^2 + 5x - 3 = 0 are:")
for i, sol in enumerate(solution, 1):
    print(f"x{i} = {sol}")
```

Explanation:
1. We import the necessary functions from SymPy.
2. We define x as a symbol and create the equation 2x^2 + 5x - 3 = 0.
3. We use SymPy's solve function to find the roots of the equation.
4. We print each solution.

When we run this program, it will output:
The solutions to the equation 2x^2 + 5x - 3 = 0 are:
x1 = -3
x2 = 1/2

This program solves the quadratic equation symbolically, giving us the exact solutions without any numerical approximation. The solutions are x = -3 and x = 1/2.