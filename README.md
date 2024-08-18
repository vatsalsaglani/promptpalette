# PromptPalette

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1qujWVI-nd0HBnQz49GsRoido4mIOA7N8?usp=sharing)


PromptPalette is a powerful and flexible Python package designed to streamline the process of creating optimized prompts for large language models. It combines strategy selection and prompt writing to generate tailored system prompts for various AI applications.

## Features

- Automatic selection of appropriate prompting strategies based on given requirements and objectives
- Crafting of detailed, task-specific prompts using selected strategies
- Support for multiple AI providers (OpenAI, Anthropic)
- Asynchronous operation for improved performance
- Easy integration with existing AI workflows

## Installation

You can install PromptPalette using pip:

```bash
pip install git+https://github.com/vatsalsaglani/promptpalette.git
```

## Quick Start

Here's a simple example of how to use PromptPalette:

```python
import asyncio
from promptpalette import Composer

api_key = "YOUR_API_KEY"
provider = "openai"  # or "claude"
model_name = "gpt-4o"  # or "claude-3-5-sonnet-20240620"

composer = Composer(api_key=api_key, provider=provider, model_name=model_name)

requirements_objectives = """Develop a chatbot that can provide personalized financial advice to users, including investment suggestions, budget planning, and explanations of complex financial concepts.
Key Requirements:

Personalized responses based on user's financial situation and goals
Ability to explain complex financial concepts in simple terms
Provide step-by-step guidance for creating budgets
Generate and explain investment portfolio recommendations
"""

async def main():
    prompt = await composer(requirements_objectives)
    print(prompt)

asyncio.run(main())
```

## Advanced Usage

PromptPalette can handle a variety of tasks, from complex system designs to simple classification problems. Here's an example of using it for sentiment analysis:

```python
async def main():
    prompt = await composer("I want to classify if a given tweet is positive or negative. And then provide tags or categories under positive or negative classified")
    print(prompt)

asyncio.run(main())
```

## Configuration

PromptPalette supports different AI providers (`openai` and `claude`) and models. You can configure it by passing the appropriate parameters to the `Composer` class:

```python
composer = Composer(api_key="YOUR_API_KEY", provider="openai", model_name="gpt-4o")
```
