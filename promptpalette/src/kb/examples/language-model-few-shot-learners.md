---
Paper: Language Models are Few-Shot Learners
Link: https://arxiv.org/abs/2005.14165
---

Here's a prompt with examples for Few-Shot Learning prompting, followed by a brief description of the technique:

```
You are an AI assistant capable of learning new tasks from just a few examples. When presented with a task and a few examples, use those to understand the pattern and complete the task for new inputs. Here's an example:

user: `Translate the following words from English to French:

English: Hello
French: Bonjour

English: Goodbye
French: Au revoir

English: Thank you
French: Merci

English: Please
French:`

assistant: Based on the pattern in the given examples, I can complete the translation:

English: Please
French: S'il vous plaît

The pattern shows English words or phrases being translated into their French equivalents. "Please" in French is "S'il vous plaît".

user: `Classify the sentiment of these movie reviews:

Review: The acting was superb and the plot kept me on the edge of my seat.
Sentiment: Positive

Review: I've never been so bored in my life. The characters were flat and uninteresting.
Sentiment: Negative

Review: While the special effects were impressive, the story lacked depth.
Sentiment: Mixed

Review: This film is an absolute masterpiece. I can't recommend it enough!
Sentiment:`

assistant: Based on the pattern in the given examples, I can classify the sentiment of the new review:

Review: This film is an absolute masterpiece. I can't recommend it enough!
Sentiment: Positive

The pattern shows that reviews expressing strong approval and enthusiasm are classified as "Positive". This review uses very positive language ("absolute masterpiece") and expresses strong recommendation, which aligns with the positive sentiment pattern seen in the examples.