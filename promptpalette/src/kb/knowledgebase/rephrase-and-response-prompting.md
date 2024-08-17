---
Paper: Rephrase and Respond: Let Large Language Models Ask Better Questions for Themselves
Link: https://arxiv.org/abs/2311.04205v2
---

Examples of Rephrase and Respond (RaR) prompting mentioned in the paper:

1. Even day question:
Original: "Was Barack Obama born in an even day?"
RaR: "Did the former United States President, Barack Obama, have his birthday fall on an even numbered day of a month?"

2. Coin flip question:
Original: "A coin is heads up. aluino flips the coin. arthor flips the coin. Is the coin still heads up? Flip means reverse."
RaR: "The coin started out being heads up. Then, Aluino flipped the coin, reversing its side. After that, Arthor also flipped the coin, reversing its side again. Is the coin facing heads up now? Considering the action of flipping the coin means to reverse its side, after two flips, the coin would indeed be back in its original position."

3. Last letter concatenation:
Original: "Take the last letters of the words in "Beth Joel" and concatenate them."
RaR: "Can you merge the last letters from each of the words in the name "Beth Joel" together? What would the resultant combination look like?"

Essence of Rephrase and Respond (RaR) prompting:

RaR is a prompting technique that allows language models to rephrase and expand on the original question before providing an answer. The idea behind it is to address potential misunderstandings or ambiguities in the original question by letting the model clarify and contextualize the query in its own words.

Key aspects:
1. Self-clarification: The model rephrases the question to better align with its understanding.
2. Expansion: Additional context or details are added to make the question more precise.
3. Improved alignment: Helps bridge the gap between human and AI frames of thought.
4. Single-step process: Rephrasing and answering occur in a single prompt.

Use cases:
1. Complex reasoning tasks
2. Ambiguous or poorly worded questions
3. Tasks requiring specific domain knowledge
4. Improving zero-shot performance on various benchmarks
5. Enhancing model performance without fine-tuning

Additional examples of RaR prompting:

1. Mathematical reasoning:
Original: "What's the area of a circle with radius 5?"
RaR: "To find the area of a circle with a radius of 5 units, we need to use the formula A = πr², where π is approximately 3.14159 and r is the radius. Let's calculate this step by step."

2. Historical context:
Original: "Who won the American Civil War?"
RaR: "The American Civil War was fought from 1861 to 1865 between the Union (Northern states) and the Confederacy (Southern states). When we ask who 'won' this conflict, we're typically referring to which side achieved its primary objectives and emerged in a stronger position. Let's examine the outcome of the war."

3. Language task:
Original: "Translate 'hello' to French."
RaR: "To translate the English greeting 'hello' into French, we need to consider the context and level of formality. In French, there are different ways to say hello depending on the situation. Let's explore the most common translation and explain its usage."