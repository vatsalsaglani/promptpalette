---
Paper: Contrastive Chain-of-Thought Prompting
Link: https://arxiv.org/abs/2311.09277v1
---

Examples of Contrastive Chain-of-Thought (CCoT) prompting mentioned in the paper:

1. Arithmetic reasoning example:
Question: James has 30 teeth. His dentist drills 4 of them and caps 7 more teeth than he drills. What percentage of James' teeth does the dentist fix?

Correct Explanation: The dentist drills 4 teeth, so there are 30 - 4 = 26 teeth left. The dentist caps 7 more teeth than he drills, so he caps 4 + 7 = 11 teeth. Therefore, the dentist fixes a total of 4 + 11 = 15 teeth. To find the percentage of teeth the dentist fixes, we divide the number of teeth fixed by the total number of teeth and multiply by 100: 15/30 x 100 = 50%

Wrong Explanation: The dentist fixes a total of 4 + 7 = 11 teeth. To find the percentage, we divide the number of teeth fixed by the total number of teeth and multiply by 100: 11/30 x 100 = 36.67%

2. Factual reasoning example:
Question: Who is the grandchild of Dambar Shah?

Correct Explanation: Dambar Shah (? - 1645) was the father of Krishna Shah. Rudra Shah was the child of Krishna Shah (? - 1661). So the final answer (the name of the grandchild) is: Rudra Shah.

Wrong Explanation: Dambar Shah (? - 1645) was the child of Krishna Shah. Rudra Shah was the father of Krishna Shah (? - 1661). So the final answer (the name of the grandchild) is: Rudra Shah.

Essence of Contrastive Chain-of-Thought (CCoT) prompting:

CCoT is an enhancement to the traditional Chain-of-Thought (CoT) prompting method. It involves providing both correct and incorrect reasoning demonstrations to the language model, allowing it to learn from both positive and negative examples.

Key ideas:
1. Combines valid and invalid reasoning demonstrations
2. Helps models distinguish between correct and incorrect reasoning steps
3. Enhances the model's ability to avoid common reasoning mistakes
4. Can be automatically generated from existing correct rationales
5. Compatible with other techniques like self-consistency

Use cases:
1. Arithmetic reasoning tasks
2. Factual question answering
3. Logical reasoning problems
4. Multi-step problem-solving
5. Any task that benefits from step-by-step reasoning

Additional examples of CCoT prompting:

1. Physics problem:
Question: A car travels 120 km in 2 hours. What is its average speed in m/s?

Correct Explanation: First, we calculate the speed in km/h: 120 km / 2 hours = 60 km/h. To convert to m/s, we multiply by 1000 m/km and divide by 3600 s/h: 60 * 1000 / 3600 = 16.67 m/s.

Wrong Explanation: We divide 120 by 2 to get 60 km/h. Then we simply convert km to m by multiplying by 1000, so the answer is 60,000 m/s.

2. Historical reasoning:
Question: Who became the President of the United States after John F. Kennedy's assassination?

Correct Explanation: John F. Kennedy was assassinated on November 22, 1963. At that time, Lyndon B. Johnson was serving as Vice President. According to the U.S. Constitution, when a President dies in office, the Vice President immediately becomes President. Therefore, Lyndon B. Johnson became President after Kennedy's assassination.

Wrong Explanation: After John F. Kennedy's assassination, his brother Robert F. Kennedy became President because he was next in line for the presidency as a family member. This is why Robert Kennedy ran for President in 1968.