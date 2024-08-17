---
Paper: Chain-of-Table - Evolving Tables in the Reasoning Chain for Table Understanding
Link: https://arxiv.org/abs/2401.04398v2
---

The essence of the Chain-of-Table prompting technique is:

Key ideas:
1. Uses tabular data explicitly in the reasoning chain by iteratively transforming the input table
2. Guides language models to generate a sequence of table operations that represent the reasoning steps
3. Dynamically plans and executes operations to modify the table in response to the specific question
4. Stores intermediate reasoning results directly in the evolving table structure

What it does:
- Prompts the language model to select and execute atomic table operations (e.g. add column, select rows, group by, sort)
- Iteratively transforms the input table through multiple reasoning steps
- Generates arguments for each operation to specify how to modify the table 
- Produces a chain of intermediate tables that represent the reasoning process
- Uses the final transformed table to generate the answer

Use cases:
- Table-based question answering
- Fact verification using tabular data
- Complex multi-step reasoning over structured data
- Enhancing LLM performance on tasks requiring tabular understanding

Examples from the paper:

1. Question answering on WikiTQ dataset:

Question: Which country had the most cyclists finish within the top 10?

Chain of operations:
1. f_add_column(Country) 
2. f_select_row(row 1, row 10)
3. f_select_column(Country)
4. f_group_by(Country)
5. f_sort_by(Count)

Final table:
Group | Country | Count
1     | ITA     | 3
2     | ESP     | 3
3     | RUS     | 2
4     | FRA     | 2

Answer: Italy

2. Physics question:

Question: Identify the physics formula that would be most useful for finding the answer to each of the following word problems. A particle of mass 6.8 * 10^-5 g and charge 58 mC moves in a region of space where the electric field is uniform and is 7.2 N/C in the x direction and zero in the y and z direction. If the initial velocity of the particle is given by vy = 1.7 * 10^6 m/s, vx = vz = 0, what is the speed of the particle at 0.7 s?

Chain of operations:
1. f_add_column(Given Quantities)
2. f_add_column(Required Quantity) 
3. f_add_column(Relevant Formula)
4. f_select_column(Given Quantities, Required Quantity, Relevant Formula)

Final table:
Given Quantities | Required Quantity | Relevant Formula
mass, charge,    | Speed at 0.7 s    | F = ma = qE
electric field,  |                   | a = (q/m) * E
initial velocity |                   |

Answer: F = m * a

3. Fact verification on TabFact dataset:

Statement: There are no Cardiff wins that have a draw greater than 27.

Chain of operations:
1. f_select_column(cardiff win, draw)
2. f_select_row(cardiff win > 0)
3. f_sort_by(draw)

Final table:
cardiff win | draw
19          | 16
0           | 27
2           | 0

Answer: True

These examples demonstrate how Chain-of-Table guides the language model through a series of table transformations to reason about the data and arrive at the correct answer. The technique allows for dynamic, multi-step reasoning tailored to each specific question or statement.