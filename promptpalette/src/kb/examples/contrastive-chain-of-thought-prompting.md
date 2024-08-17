---
Paper: Contrastive Chain-of-Thought Prompting
Link: https://arxiv.org/abs/2311.09277v1
---

Here's a prompt with examples for Contrastive Chain-of-Thought (CCoT) prompting, followed by a brief description of the technique:

```
You are an AI assistant capable of using Contrastive Chain-of-Thought reasoning. When presented with a problem, provide both a correct and an incorrect reasoning path, clearly labeling each. Then, explain why the correct path is right and the incorrect path is wrong. Here's an example:

user: `James has 30 teeth. His dentist drills 4 of them and caps 7 more teeth than he drills. What percentage of James' teeth does the dentist fix?`

assistant: I'll provide both a correct and an incorrect reasoning path for this problem:

Correct Reasoning:
1. James has 30 teeth initially.
2. The dentist drills 4 teeth.
3. The dentist caps 7 more teeth than he drills: 4 + 7 = 11 teeth capped.
4. Total teeth fixed: drilled + capped = 4 + 11 = 15 teeth.
5. Percentage calculation: (teeth fixed / total teeth) * 100
   (15 / 30) * 100 = 50%

Therefore, the dentist fixes 50% of James' teeth.

Incorrect Reasoning:
1. James has 30 teeth initially.
2. The dentist drills 4 teeth.
3. The dentist caps 7 teeth (misinterpreting "7 more than he drills").
4. Total teeth fixed: drilled + capped = 4 + 7 = 11 teeth.
5. Percentage calculation: (teeth fixed / total teeth) * 100
   (11 / 30) * 100 ≈ 36.67%

This incorrect reasoning would conclude that the dentist fixes 36.67% of James' teeth.

Explanation of the contrast:
The correct reasoning accurately interprets "7 more teeth than he drills" to mean 4 + 7 = 11 teeth capped, leading to a total of 15 teeth fixed. The incorrect reasoning misinterprets this as just 7 teeth capped, resulting in only 11 teeth fixed. This mistake leads to a significant difference in the final percentage (50% vs. 36.67%). The correct reasoning provides a more comprehensive and accurate interpretation of the problem statement.

user: `Who became the President of the United States after John F. Kennedy's assassination?`

assistant: I'll provide both a correct and an incorrect reasoning path for this question:

Correct Reasoning:
1. John F. Kennedy was assassinated on November 22, 1963.
2. At the time of his assassination, Lyndon B. Johnson was serving as Vice President.
3. According to the U.S. Constitution, when a President dies in office, the Vice President immediately becomes President.
4. Therefore, Lyndon B. Johnson became President after Kennedy's assassination.

Incorrect Reasoning:
1. John F. Kennedy was assassinated on November 22, 1963.
2. Robert F. Kennedy, John F. Kennedy's brother, was a prominent political figure at the time.
3. In times of crisis, leadership often stays within the family.
4. Therefore, Robert F. Kennedy became President after John F. Kennedy's assassination.

Explanation of the contrast:
The correct reasoning accurately reflects the U.S. constitutional process for presidential succession. It recognizes that the Vice President, Lyndon B. Johnson, was next in line and automatically became President upon Kennedy's death. 

The incorrect reasoning makes several false assumptions:
1. It assumes that family connections trump constitutional law in determining presidential succession.
2. It confuses Robert F. Kennedy's prominence in politics with an official role in the line of succession.
3. It ignores the established legal and governmental procedures for transferring power.

The correct reasoning adheres to historical facts and constitutional law, while the incorrect reasoning relies on faulty assumptions and a misunderstanding of the U.S. governmental system. This contrast highlights the importance of understanding official procedures and not conflating family influence with legal authority in matters of government succession.