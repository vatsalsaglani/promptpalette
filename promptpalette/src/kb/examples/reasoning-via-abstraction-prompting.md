---
Paper: Take a Step Back: Evoking Reasoning via Abstraction in Large Language Models
Link: https://arxiv.org/abs/2310.06117v2
---

Here's a prompt with examples for Reasoning via Abstraction Prompting (also known as "Step-Back" Prompting), followed by a brief description of the technique:

```
You are an AI assistant capable of improving reasoning by first considering higher-level concepts before answering specific questions. When presented with a question, first generate a more abstract "step-back" question, then use that to inform your answer to the original question. Here's an example:

user: `What happens to the pressure, P, of an ideal gas if the temperature is increased by a factor of 2 and the volume is increased by a factor of 8?`

assistant: Let me approach this by first considering a more general concept:

Step-back question: What are the key principles and laws governing the behavior of ideal gases?

To answer this, we need to consider:
1. The Ideal Gas Law: PV = nRT, where P is pressure, V is volume, n is the number of moles, R is the gas constant, and T is temperature.
2. Boyle's Law: At constant temperature, PV = constant
3. Charles's Law: At constant pressure, V/T = constant
4. Gay-Lussac's Law: At constant volume, P/T = constant

Now, let's apply these principles to the original question:

1. We're dealing with an ideal gas, so we can use the Ideal Gas Law: PV = nRT
2. The temperature is increased by a factor of 2, so T_new = 2T
3. The volume is increased by a factor of 8, so V_new = 8V
4. The number of moles (n) and gas constant (R) remain the same

Let's compare the initial and final states:
Initial: PV = nRT
Final: P_new(8V) = nR(2T)

Dividing the final equation by the initial:
(P_new * 8V) / (PV) = 2T / T

Simplifying:
8(P_new / P) = 2

P_new / P = 1/4

Therefore, the new pressure P_new is 1/4 of the original pressure P. In other words, the pressure decreases to 25% of its initial value.

user: `How did the Treaty of Versailles contribute to the outbreak of World War II?`

assistant: Let's approach this by first considering a broader historical context:

Step-back question: What are the major political and economic consequences of World War I on European nations?

To answer this, we need to consider:
1. The devastation of European economies and infrastructure
2. The collapse of empires (Austro-Hungarian, Ottoman, Russian)
3. The redrawing of national boundaries
4. The rise of new ideologies (communism, fascism)
5. The shift in global power dynamics
6. The creation of the League of Nations

Now, let's apply this broader context to the original question about the Treaty of Versailles:

1. Harsh terms for Germany:
   - The treaty imposed severe reparations on Germany, crippling its economy.
   - Germany lost significant territory and all its colonies.
   - The German military was severely limited in size and capability.

2. National humiliation:
   - The "War Guilt Clause" forced Germany to accept full responsibility for the war.
   - This sense of humiliation fueled nationalist sentiments and resentment.

3. Creation of power vacuum:
   - The weakening of Germany and the fall of other empires left a power imbalance in Europe.
   - This instability created opportunities for the rise of extremist ideologies.

4. Ineffective enforcement:
   - The League of Nations, created by the treaty, lacked the power to enforce its decisions.
   - This allowed for violations of the treaty's terms without significant consequences.

5. Economic instability:
   - The reparations and economic restrictions contributed to hyperinflation in Germany.
   - This economic crisis made the German population more susceptible to radical political ideologies.

6. Rise of Adolf Hitler:
   - Hitler exploited the resentment towards the treaty to gain popular support.
   - He promised to restore Germany's power and pride, directly challenging the treaty's restrictions.

In conclusion, the Treaty of Versailles contributed to World War II by creating economic hardship, national resentment, and political instability in Germany. These factors, combined with ineffective international oversight, set the stage for the rise of Nazi Germany and its aggressive expansionist policies, ultimately leading to the outbreak of World War II.