---
Paper: Chain-of-Note: Enhancing Robustness in Retrieval-Augmented Language Models
Link: https://arxiv.org/abs/2311.09210v1
---

Here's a prompt with examples for Chain-of-Note (CoN) prompting, followed by a brief description of the technique:

```
You are an AI assistant capable of analyzing multiple documents and generating reading notes before answering questions. For each document, create a concise note highlighting key information relevant to the query. Then, use these notes to formulate your final answer. Here's an example:

user: `Who was the first person to win the Nobel Prize in two different scientific categories?`

assistant: Let me analyze the available documents and create reading notes for each:

Reading note for Document 1: This document discusses Marie Curie's life and achievements. It mentions that she won the Nobel Prize in Physics in 1903 and the Nobel Prize in Chemistry in 1911, making her the first person to win Nobel Prizes in two different scientific categories.

Reading note for Document 2: This document is about the history of the Nobel Prize. It confirms that Marie Curie was the first person to be awarded two Nobel Prizes in different fields (Physics and Chemistry).

Based on the information in these reading notes, I can answer the question:

The first person to win the Nobel Prize in two different scientific categories was Marie Curie. She won the Nobel Prize in Physics in 1903 and the Nobel Prize in Chemistry in 1911.

user: ``Verify the claim: "The Eiffel Tower was originally intended to be a temporary structure."`

assistant: I'll analyze the available documents and create reading notes for each:

Reading note for Document 1: This document discusses the history of the Eiffel Tower. It states that the tower was built for the 1889 World's Fair in Paris and was originally intended to stand for only 20 years. The structure was meant to be dismantled after the exhibition, but it was kept due to its usefulness for scientific experiments and communication purposes.

Reading note for Document 2: This document is about famous landmarks in Paris. It briefly mentions the Eiffel Tower but doesn't provide any information about its original intended duration.

Reading note for Document 3: This document focuses on the engineering aspects of the Eiffel Tower. It confirms that the tower was initially planned as a temporary exhibit for the 1889 World's Fair, with a 20-year permit. The document adds that the tower's usefulness for radio transmission saved it from demolition.

Based on the information in these reading notes, I can verify the claim:

The claim "The Eiffel Tower was originally intended to be a temporary structure" is SUPPORTED. Multiple sources confirm that the Eiffel Tower was initially planned as a temporary structure for the 1889 World's Fair, with an intended lifespan of 20 years. It was only later that the decision was made to keep the tower permanently, primarily due to its scientific and communication utility.