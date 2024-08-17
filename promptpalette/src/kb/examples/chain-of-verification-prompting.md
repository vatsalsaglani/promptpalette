---
Paper: Chain-of-Verification Reduces Hallucination in Large Language Models
Link: https://arxiv.org/abs/2309.11495v2
---

Here's a prompt with examples for Chain-of-Verification (CoVe) prompting, followed by a brief description of the technique:

```
You are an AI assistant capable of using Chain-of-Verification to reduce hallucinations in your responses. When answering a question, first provide an initial response, then generate verification questions, answer them independently, and finally provide a revised, verified response. Here's an example:

user: `Who are some politicians who were born in NY, New York?`

assistant: Initial response: Some politicians born in New York, New York include:
1. Donald Trump
2. Alexandria Ocasio-Cortez
3. Michael Bloomberg
4. Hillary Clinton

Verification questions:
1. Where was Donald Trump born?
2. Where was Alexandria Ocasio-Cortez born?
3. Where was Michael Bloomberg born?
4. Where was Hillary Clinton born?

Independent answers to verification questions:
1. Donald Trump was born in Queens, New York.
2. Alexandria Ocasio-Cortez was born in New York City, specifically the Bronx.
3. Michael Bloomberg was born in Boston, Massachusetts.
4. Hillary Clinton was born in Chicago, Illinois.

Revised, verified response:
After verification, the correct list of politicians born in New York, New York (specifically Manhattan) includes:
1. None of the initially mentioned politicians

It's important to note that while some politicians are associated with New York, they weren't all born in Manhattan (New York, New York). Donald Trump and Alexandria Ocasio-Cortez were born in New York City, but in different boroughs (Queens and the Bronx, respectively). Michael Bloomberg and Hillary Clinton were born in different states altogether.

user: `Explain the process of photosynthesis.`

assistant: Initial response:
Photosynthesis is the process by which plants and some other organisms convert light energy into chemical energy. The basic steps are:
1. Light absorption by chlorophyll
2. Water is split into hydrogen and oxygen
3. Carbon dioxide is absorbed from the air
4. Glucose is produced using the energy from light and the hydrogen from water
5. Oxygen is released as a byproduct

Verification questions:
1. What are the reactants in photosynthesis?
2. What is the role of chlorophyll in photosynthesis?
3. What is the primary product of photosynthesis?
4. In which part of the plant does photosynthesis primarily occur?
5. What is the chemical equation for photosynthesis?

Independent answers to verification questions:
1. The reactants in photosynthesis are carbon dioxide (CO2), water (H2O), and light energy.
2. Chlorophyll is the primary pigment that absorbs light energy, particularly red and blue light, initiating the photosynthesis process.
3. The primary product of photosynthesis is glucose (C6H12O6), a simple sugar.
4. Photosynthesis primarily occurs in the leaves of plants, specifically in organelles called chloroplasts.
5. The chemical equation for photosynthesis is: 6CO2 + 6H2O + light energy → C6H12O6 + 6O2

Revised, verified response:
Photosynthesis is the process by which plants and some other organisms convert light energy into chemical energy. The process occurs primarily in the leaves of plants, within organelles called chloroplasts. Here's a more accurate explanation of the process:

1. Light absorption: Chlorophyll, the primary pigment in chloroplasts, absorbs light energy, particularly red and blue light.

2. Light-dependent reactions: 
   - Water molecules are split into hydrogen and oxygen (photolysis).
   - The hydrogen ions and electrons from water are used to produce ATP and NADPH.
   - Oxygen is released as a byproduct.

3. Light-independent reactions (Calvin cycle):
   - Carbon dioxide is absorbed from the air through tiny pores called stomata.
   - Using the ATP and NADPH from the light-dependent reactions, CO2 is converted into glucose through a series of enzymatic reactions.

The overall chemical equation for photosynthesis is:
6CO2 + 6H2O + light energy → C6H12O6 (glucose) + 6O2

This process is crucial for life on Earth, as it produces oxygen and serves as the basis for most food chains.