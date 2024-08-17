import asyncio
from promptpalette import Composer

api_key = "YOUR OPENAI API KEY"
provider = "openai"
model_name = "gpt-4o"

# api_key = "YOUR CLAUDE API KEY"
# provider = "claude"
# model_name = "claude-3-5-sonnet-20240620"

composer = Composer(api_key=api_key, provider=provider, model_name=model_name)

requirements_objectives = """Title: AI-Powered Financial Advisor Chatbot
Objective:
Develop a chatbot that can provide personalized financial advice to users, including investment suggestions, budget planning, and explanations of complex financial concepts.
Key Requirements:

Personalized responses based on user's financial situation and goals
Ability to explain complex financial concepts in simple terms
Provide step-by-step guidance for creating budgets
Generate and explain investment portfolio recommendations
Use up-to-date financial data and regulations in its advice
Handle follow-up questions and maintain context throughout the conversation
Integrate with a Python-based financial calculation tool for precise numerical analysis
Maintain a professional yet friendly tone
Provide sources or reasoning for its recommendations when asked

Additional Considerations:

The chatbot should be able to handle a wide range of financial literacy levels
It should be capable of adapting its language and explanations based on user feedback
The system should recognize when a question is beyond its capability and suggest seeking professional financial advice


Available Tools:
Python Execution Engine: Give python code in <python> code block
"""

# print(asyncio.run(composer(requirements_objectives)))
print(
    asyncio.run(
        composer(
            "I want to classify if a given tweet is positive or negative. And then provide tags or categories under positive or negative classified"
        )))
