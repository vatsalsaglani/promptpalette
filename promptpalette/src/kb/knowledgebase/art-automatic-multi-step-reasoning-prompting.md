---
Paper: ART - Automatic multi-step reasoning and tool-use for large language models
Link: https://arxiv.org/abs/2303.09014v1
---

Here are the key aspects of the ART (Automatic Reasoning and Tool-use) prompting technique:

Essence of the technique:
ART automatically generates multi-step reasoning decompositions for new tasks by retrieving and adapting relevant examples from a task library. It also incorporates tool use (like search, code generation/execution) into the reasoning steps.

Key ideas:
1. Uses a structured query language to represent multi-step reasoning as a program with tool calls
2. Maintains a library of seed tasks with authored reasoning programs 
3. Retrieves relevant examples from the task library for new tasks
4. Allows seamless integration of external tools during generation
5. Enables human feedback to improve performance on specific tasks

What it does:
- Automatically decomposes new tasks into multi-step reasoning programs
- Selects and uses appropriate tools as part of the reasoning process
- Generalizes reasoning patterns and tool use across tasks
- Allows easy incorporation of human feedback to improve performance

Use cases:
- Complex reasoning tasks requiring multiple steps
- Tasks benefiting from external tools or knowledge sources
- Arithmetic and mathematical reasoning
- Code generation and execution
- Question answering requiring search or decomposition

Examples from the paper:

1. Anachronisms task:
Input: President George H. W. Bush called his generals to the Oval Office at the outset of the Gulf War.

Q1: [tag] What are the entities in this sentence?
#1:
President George H. W. Bush
Gulf War

Q2: [search] When was President George H. W. Bush president?
#2: George H. W. Bush's tenure as the 41st president of the United States began with his inauguration on January 20, 1989, and ended on January 20, 1993.

Q3: [search] When was the Gulf War fought?
#3: The Gulf War was a 1990–1991 armed campaign waged by a 35-country military coalition in response to the Iraqi invasion of Kuwait.

Q4: [subquestion] Could these entities have co-existed based on their time periods alone?
#4: Yes. Their time periods intersect.

Q5: [generate output] Is this an anachronism?
#5: No

Q6: [EOQ]
Ans: No

2. Elementary Math task:
Input: Janet's ducks lay 16 eggs per day. She eats three for breakfast every morning and bakes muffins for her friends every day with four. She sells the remainder at the farmers' market daily for $2 per fresh duck egg. How much in dollars does she make every day at the farmers' market?

Q1: [generate python code] write down the arithmetic or algebra equations as python code, storing the answer as 'ans'
#1:
total_eggs = 16
eaten_eggs = 3
baked_eggs = 4
sold_eggs = total_eggs - eaten_eggs - baked_eggs
dollars_per_egg = 2
ans = sold_eggs * dollars_per_egg
print(ans)

Q2: [code execute] Execute the python code in #1 and get the value of "ans"
#2: 18

Q3: [EOQ]
Ans:18

3. Physics task:
Input: Identify the physics formula that would be most useful for finding the answer to each of the following word problems. A particle of mass 6.8 * 10 ^ -5 g and charge 58 mC moves in a region of space where the electric field is uniform and is 7.2 N/C in the x direction and zero in the y and z direction. If the initial velocity of the particle is given by vy = 1.7 * 10 ^ 6 m/s, vx = vz = 0, what is the speed of the particle at 0.7 s?

Q1: [subquestion] What quantity is being asked for in the problem?
#1: speed of the particle

Q2: [subquestion] What other information is given in the problem?
#2: mass of particle (6.8 * 10 ^ -5 g), charge(58 mC), electric field (7.2 N/C), initial velocity (vy = 1.7 * 10 ^ 6 m/s, vx = vz = 0)

Q3: [search] Given mass of the particle, charge and initial velocity of particle, and electric field, what can we compute for the particle? Give the physics formula.
#3:
We can compute acceleration of the particle, as follows:
a = (q/m) * E
This formula is derived from the Lorentz force law, which states that the force (F) on a particle of charge q in an electric field E is given by the equation:
F = ma = qE

Q4: [subquestion] What is the physics formula in the choices that is closest to F = ma = qE, a = (q/m) * E
#4: F = m * a

Q5: [EOQ]
Ans: F = m * a

These examples demonstrate how ART breaks down complex tasks into multiple steps, incorporates relevant tools (like search and code execution), and produces structured reasoning to arrive at the final answer.