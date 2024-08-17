---
Paper: ReAct - Synergizing Reasoning and Acting in Language Models
Link: https://arxiv.org/abs/2210.03629v3
---

Based on the paper, here is a summary of the ReAct prompting technique:

Examples mentioned in the paper:
1. HotpotQA: A multi-hop question answering task requiring reasoning over multiple Wikipedia passages.
2. FEVER: A fact verification task where claims are labeled as SUPPORTS, REFUTES, or NOT ENOUGH INFO based on Wikipedia evidence.
3. ALFWorld: A text-based game for navigating and interacting with a simulated household.
4. WebShop: An online shopping task where an agent must purchase products based on user instructions.

Essence of ReAct prompting:

ReAct is a prompting technique that combines reasoning and acting in large language models (LLMs) to solve diverse tasks. It prompts LLMs to generate both verbal reasoning traces and task-specific actions in an interleaved manner.

Key ideas:
1. Augments the action space with language-based thoughts
2. Interleaves reasoning (thoughts) and acting (actions) steps
3. Allows dynamic reasoning to create, maintain, and adjust plans
4. Enables interaction with external environments to gather information

What it does:
1. Generates coherent language sequences as intermediate reasoning steps
2. Produces task-specific actions to interact with the environment
3. Uses reasoning to guide action planning and execution
4. Leverages actions to obtain additional information for reasoning
5. Maintains a working memory through the conversation context

Use cases:
1. Multi-hop question answering
2. Fact verification
3. Interactive decision-making tasks
4. Text-based games
5. Web navigation and interaction
6. Tasks requiring both reasoning and information retrieval

Examples of prompting with ReAct:

1. HotpotQA example:
Human: Aside from the Apple Remote, what other device can control the program Apple Remote was originally designed to interact with?

ReAct:
Thought: I need to search Apple Remote and find the program it was originally designed to interact with.
Action: Search[Apple Remote]
Observation: The Apple Remote is a remote control introduced in October 2005 by Apple...originally designed to control the Front Row media center program...
Thought: Apple Remote was originally designed to control the Front Row media center program. I need to search Front Row next and find what other device can control it.
Action: Search[Front Row]
Observation: Could not find [Front Row]. Similar: [Front Row Seat to Earth, Front Row Motorsports, Front Row software...]
Thought: Front Row is not found. I need to search "Front Row software".
Action: Search[Front Row software]
Observation: Front Row is a discontinued media center software...
Thought: Front Row (software) is controlled by an Apple Remote or the keyboard function keys. So the answer is keyboard function keys.
Action: Finish[keyboard function keys]

2. ALFWorld example:
Human: You are in the middle of a room. Looking quickly around you, you see a cabinet, a cabinet, a coffeemachine, a countertop, a stoveburner, and a toaster. Your task is to: Put some peppershaker on a drawer.

ReAct:
Think: To solve the task, I need to find a peppershaker, then find a drawer, and finally put the peppershaker on the drawer. First, I need to find a peppershaker. A peppershaker is more likely to appear in cabinets, countertops, or drawers.
Act: Go to cabinet 1
Obs: On the cabinet you see a vase.
Think: The peppershaker is not here. I'll check the other cabinet.
Act: Go to cabinet 2
Obs: On the cabinet you see a apple, a bread, a peppershaker, and a vase.
Think: Now I find a peppershaker. Next, I need to take it.
Act: Take peppershaker from cabinet 2
Obs: You pick up the peppershaker from the cabinet.
Think: Now I have the peppershaker. Next, I need to find a drawer and put it there.
Act: Go to drawer 1
Obs: The drawer is closed.
Act: Open drawer 1
Obs: You open the drawer. The drawer is open. In it you see a dishsponge and a spoon.
Think: Now I find an open drawer. Next, I need to put the peppershaker in/on it.
Act: Put peppershaker in/on drawer 1
Obs: You put the peppershaker in/on the drawer.

3. WebShop example:
Human: I would like a 3 ounce bottle of bright citrus deodorant for sensitive skin, and price lower than 50.00 dollars

ReAct:
Action: search[3 ounce bright citrus deodorant sensitive skin]
Observation: [Results shown with product options]
Think: B078GWRC1J and B078GTKVXY are bright citrus deodorant less than 50 dollars. I can check B078GWRC1J first.
Action: click[B078GWRC1J]
Observation: [Product details shown]
Think: For 3 ounce bottle of bright citrus deodorant for sensitive skin, the item has options 'bright citrus' and '3 ounce (pack of 1)' and seems good to buy.
Action: click[bright citrus]
Observation: You have clicked bright citrus.
Action: click[3 ounce (pack of 1)]
Observation: You have clicked 3 ounce (pack of 1).
Action: click[Buy Now]

In each example, ReAct interleaves reasoning (thoughts) with actions and observations, allowing the model to plan, execute, and adjust its approach based on new information from the environment.