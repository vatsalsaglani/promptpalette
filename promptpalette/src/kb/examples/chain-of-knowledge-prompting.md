---
Paper: Chain-of-Knowledge - Grounding Large Language Models via Dynamic Knowledge Adapting over Heterogeneous Sources
Link: https://arxiv.org/abs/2305.13269v4
---

Here's a prompt with examples for Chain of Knowledge (CoK) prompting, followed by a brief description of the technique:

```
You are an AI assistant capable of using multiple knowledge sources to answer questions accurately. When presented with a query, identify relevant knowledge domains, retrieve information from appropriate sources, and progressively refine your reasoning. Here's an example:

user: `What year was the Argentine actor who directed El Tio Disparate born?`

assistant: To answer this question, I'll need to use multiple knowledge sources. Let me break it down step by step:

1. Identify relevant knowledge domains: Film history, Argentine cinema

2. Retrieve information about El Tio Disparate:
Action: Search[El Tio Disparate director]
Result: El Tio Disparate was directed by Palito Ortega.

1. Verify Palito Ortega's nationality and profession:
Action: Search[Palito Ortega nationality profession]
Result: Palito Ortega is an Argentine singer, actor, and film director.

1. Find Palito Ortega's birth year:
Action: Search[Palito Ortega birth date]
Result: Palito Ortega was born on March 8, 1941.

Based on this chain of knowledge, I can now answer the question:

The Argentine actor who directed El Tio Disparate, Palito Ortega, was born in 1941.

user: ``What conditions may feature splenomegaly?``

assistant: To answer this medical question about splenomegaly, I'll need to use specialized medical knowledge sources. Let's break it down:

1. Identify relevant knowledge domains: Medical, specifically hematology and gastroenterology

2. Define splenomegaly:
Action: Search[Medical dictionary: splenomegaly]
Result: Splenomegaly is an enlargement of the spleen beyond its normal size.

3. Retrieve information about conditions associated with splenomegaly:
Action: Search[Medical database: conditions associated with splenomegaly]
Result: Several conditions may feature splenomegaly, including:

a) Infections:
   - Viral infections (e.g., mononucleosis, HIV)
   - Bacterial infections (e.g., endocarditis)
   - Parasitic infections (e.g., malaria)

b) Hematologic disorders:
   - Leukemias
   - Lymphomas
   - Hemolytic anemias

c) Liver diseases:
   - Cirrhosis
   - Portal hypertension

d) Autoimmune disorders:
   - Lupus
   - Rheumatoid arthritis

e) Metabolic disorders:
   - Gaucher's disease
   - Niemann-Pick disease

f) Cancers:
   - Metastatic cancers affecting the spleen

Based on this chain of knowledge from medical sources, I can provide a comprehensive answer:

Splenomegaly, or enlargement of the spleen, may feature in various conditions including:
1. Infections (viral, bacterial, or parasitic)
2. Hematologic disorders (leukemias, lymphomas, hemolytic anemias)
3. Liver diseases (cirrhosis, portal hypertension)
4. Autoimmune disorders (lupus, rheumatoid arthritis)
5. Metabolic disorders (Gaucher's disease, Niemann-Pick disease)
6. Certain cancers, especially those metastasizing to the spleen

It's important to note that splenomegaly is a symptom rather than a disease itself, and its presence should prompt further medical investigation to determine the underlying cause.