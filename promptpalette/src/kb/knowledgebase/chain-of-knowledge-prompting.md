---
Paper: Chain-of-Knowledge - Grounding Large Language Models via Dynamic Knowledge Adapting over Heterogeneous Sources
Link: https://arxiv.org/abs/2305.13269v4
---

Thank you for providing that paper on Chain-of-Knowledge (CoK) prompting. I'll summarize the key aspects of this technique and provide some examples.

Essence of Chain-of-Knowledge (CoK) Prompting:

Chain-of-Knowledge is a framework that augments large language models (LLMs) by dynamically incorporating grounding information from heterogeneous knowledge sources. It aims to improve factual accuracy and reduce hallucination in generated outputs for knowledge-intensive tasks.

Key ideas:
1. Uses multiple heterogeneous knowledge sources across different domains (factual, medical, physics, biology)
2. Dynamically selects relevant knowledge domains for each question
3. Employs an adaptive query generator (AQG) to create queries for different types of knowledge sources
4. Progressively corrects rationales using retrieved knowledge to minimize error propagation
5. Combines structured (e.g., SPARQL, SQL) and unstructured (natural language) query capabilities

The method works in three stages:
1. Reasoning preparation: Generate preliminary rationales and identify relevant knowledge domains
2. Dynamic knowledge adapting: Retrieve knowledge, correct rationales progressively
3. Answer consolidation: Generate final answer based on corrected rationales

Use cases:
- Knowledge-intensive question answering
- Fact-checking and verification
- Multi-hop reasoning tasks
- Domain-specific (medical, scientific) question answering
- Improving factual accuracy in general language generation tasks

Examples of Chain-of-Knowledge Prompting:

1. Factual Question Answering:

Question: What year was the Argentine actor who directed El Tio Disparate born?

CoK Process:
a) Reasoning preparation:
   Identified domains: factual (Wikidata, Wikipedia)
   
b) Dynamic knowledge adapting:
   Rationale 1: First, the Argentine actor who directed El Tio Disparate is Fernando Birri.
   Retrieve (Wikidata): SELECT ?answer WHERE { wd:El_Tio_Disparate wdt:director ?answer . } -> Palito Ortega
   Retrieve (Wikipedia): Who directed El Tio Disparate? -> El Tio Disparate is directed by Palito Ortega.
   Corrected rationale 1: The Argentine actor who directed El Tio Disparate is Palito Ortega.

   Rationale 2: Palito Ortega was born in 1941.
   Retrieve (Wikidata): SELECT ?answer WHERE { wd:Palito_Ortega wdt:date_of_birth ?answer . } -> 8 March 1941
   Retrieve (Wikipedia): When was Palito Ortega born? -> Palito Ortega was born on 8 March 1941.
   Corrected rationale 2: Palito Ortega was born on 8 March 1941.

c) Answer consolidation:
   The answer is 1941.

2. Medical Question Answering:

Question: What conditions may feature splenomegaly?

CoK Process:
a) Reasoning preparation:
   Identified domains: medical (Flashcard, UpToDate)

b) Dynamic knowledge adapting:
   Rationale: Splenomegaly is a condition in which the spleen is enlarged.
   Generated query: What conditions may feature splenomegaly?
   Retrieved knowledge: Normocytic anemia with extravascular hemolysis is associated with enlargement of the spleen.
   Corrected rationale: Splenomegaly, or enlargement of the spleen, can be associated with conditions such as normocytic anemia with extravascular hemolysis.

c) Answer consolidation:
   Conditions that may feature splenomegaly include normocytic anemia with extravascular hemolysis, as the spleen plays a role in removing damaged red blood cells from circulation.

3. Physics Question Answering:

Question: Which object has the most thermal energy?

CoK Process:
a) Reasoning preparation:
   Identified domains: factual, physical (ScienceQA Physics, PhysicsClassroom)

b) Dynamic knowledge adapting:
   Rationale: Thermal energy depends on temperature and mass.
   Generated query: How does mass and temperature affect thermal energy?
   Retrieved knowledge: Thermal energy is directly proportional to both mass and temperature. An object with higher mass or higher temperature will have more thermal energy.
   Corrected rationale: Thermal energy is determined by both the mass and temperature of an object. An object with greater mass or higher temperature will possess more thermal energy.

c) Answer consolidation:
   To determine which object has the most thermal energy, we need to consider both its mass and temperature. The object with the highest combination of mass and temperature will have the most thermal energy.

These examples demonstrate how CoK dynamically retrieves and incorporates knowledge from various sources to improve the factual accuracy and reasoning of LLMs in different domains.