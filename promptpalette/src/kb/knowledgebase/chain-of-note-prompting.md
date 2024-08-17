---
Paper: Chain-of-Note: Enhancing Robustness in Retrieval-Augmented Language Models
Link: https://arxiv.org/abs/2311.09210v1
---

Based on the paper, here is a summary of the Chain-of-Note (CoN) prompting technique:

Examples mentioned in the paper:
1. Question answering on HotpotQA, TriviaQA, and WebQ datasets
2. Fact verification on FEVER dataset
3. Handling real-time questions outside the model's training data using RealTimeQA

Essence of Chain-of-Note (CoN) prompting:

CoN is a framework designed to enhance the robustness of retrieval-augmented language models (RALMs) by generating sequential reading notes for retrieved documents. This approach allows for a comprehensive assessment of document relevance to the input query before formulating a final response.

Key ideas:
1. Generate reading notes for each retrieved document
2. Evaluate the relevance of documents to the query
3. Identify critical and reliable information within documents
4. Filter out irrelevant or less credible content
5. Integrate information to formulate a final answer
6. Acknowledge limitations when information is insufficient

What it does:
1. Improves the ability to discern and disregard noisy information in irrelevant retrieved documents
2. Enhances the model's capability to leverage its intrinsic knowledge when appropriate
3. Enables the model to acknowledge when it lacks sufficient knowledge to answer a query
4. Provides more precise and contextually relevant responses
5. Improves overall QA performance and robustness in both noisy and unknown scenarios

Use cases:
1. Open-domain question answering
2. Fact verification
3. Handling real-time or out-of-domain questions
4. Improving robustness in scenarios with noisy or irrelevant retrieved documents
5. Enhancing model performance in knowledge-intensive tasks

Examples of prompting with CoN:

1. Question Answering:
Human: Who performed "It Must Have Been Love"?

CoN system:
Reading note for Document 1: This passage confirms that "It Must Have Been Love" is a song written by Per Gessle and performed by the Swedish pop duo Roxette. It became their third number one hit in the United States.
Reading note for Document 2: This passage discusses a different song, "It Must Be Love," written and recorded by Labi Siffre in 1971. It's not relevant to the question about "It Must Have Been Love."
Final answer: Based on the information provided in the passages, the answer is Roxette.

2. Fact Verification:
Human: Verify the claim: "The first Jnanpith Award recipient was an author in Malayalam."

CoN system:
Reading note for Document 1: This passage states that the first Jnanpith Award was given to G. Sankara Kurup in 1965 for his collection of poems, Odakkuzhal.
Reading note for Document 2: This passage mentions that G. Sankara Kurup was among the finalists for the Jnanpith Award and that he wrote in Malayalam.
Final answer: The claim is SUPPORTED. The passages confirm that G. Sankara Kurup, who wrote in Malayalam, was the first recipient of the Jnanpith Award.

3. Handling Unknown Scenarios:
Human: When is the fourth movie of the Divergent series coming out?

CoN system:
Reading note for Document 1: This passage discusses the Divergent series as a trilogy of science fiction films but doesn't mention a fourth movie.
Reading note for Document 2: This passage mentions that the third Divergent film was a box office disappointment, leading to budget cuts for a potential fourth film. However, it doesn't provide a release date for a fourth movie.
Final answer: Based on the information given in the passages and my current knowledge, the answer is unknown. The passages don't confirm a release date for a fourth Divergent movie, and there's uncertainty about its production due to the poor performance of the third film.

In each example, CoN generates reading notes for the retrieved documents, assesses their relevance to the question, and formulates a final answer based on the available information. When information is insufficient or irrelevant, CoN guides the model to acknowledge its limitations.