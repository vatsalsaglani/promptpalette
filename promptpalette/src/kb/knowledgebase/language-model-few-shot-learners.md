---
Paper: Language Models are Few-Shot Learners
Link: https://arxiv.org/abs/2005.14165
---

The essence of few-shot prompting:

Few-shot prompting is a technique where a language model is given a small number of examples (typically 2-5) of a task within its input context, allowing it to understand and perform the task without any fine-tuning. This approach leverages the model's broad knowledge and adaptability to quickly grasp new tasks or formats based on just a handful of demonstrations.

Here are a couple of use cases with few-shot examples:

1. Sentiment Analysis

Prompt:
Review: The food was delicious and the service was excellent.
Sentiment: Positive

Review: The movie was boring and I fell asleep halfway through.
Sentiment: Negative

Review: The hotel room was clean but the noise from the street kept me up all night.
Sentiment: Mixed

Review: I can't wait to go back to that amusement park, it was so much fun!
Sentiment:

Expected output: Positive

2. Named Entity Recognition

Prompt:
Text: John Smith visited New York City last summer.
Entities: [John Smith: PERSON], [New York City: LOCATION]

Text: Apple Inc. announced a new iPhone model yesterday.
Entities: [Apple Inc.: ORGANIZATION], [iPhone: PRODUCT]

Text: The Eiffel Tower in Paris attracts millions of tourists every year.
Entities: [Eiffel Tower: LOCATION], [Paris: LOCATION]

Text: Shakespeare wrote Romeo and Juliet in the late 16th century.
Entities:

Expected output: [Shakespeare: PERSON], [Romeo and Juliet: WORK_OF_ART]

These examples demonstrate how a few demonstrations can set up the pattern and context for the model to then perform the task on a new input.

Here are the key examples of few-shot prompting described in the paper:

1. Translation task:
The paper shows an example of translating from English to French, with the prompt:
"English: I don't speak French.
French: Je ne parle pas français.
English: My name is John.
French:"

2. Arithmetic tasks:
Examples like "Q: What is 48 plus 76? A: 124."

3. Word unscrambling:
Prompts like "Unscramble 'lyinevitab' = inevitably"

4. Using novel words in a sentence:
The paper gives an example of defining a made-up word "Gigamuru" as a Japanese musical instrument, then asking the model to use it in a sentence.

5. Grammar correction:
Prompts like:
"Poor English input: I eated the purple berries.
Good English output: I ate the purple berries."

6. SAT analogy questions:
For example: "audacious is to boldness as (a) sanctimonious is to hypocrisy..."

7. News article generation:
The paper describes providing the model with a title and subtitle for a news article and having it generate the full text.

8. Closed-book question answering:
Giving the model questions without context, like "Q: Who won the 2020 US presidential election?"

These examples demonstrate how GPT-3 can perform various tasks with just a few examples in the prompt, without any fine-tuning.