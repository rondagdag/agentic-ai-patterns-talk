from smolagents import CodeAgent, InferenceClientModel, tool
from typing import List, Callable, Dict, Any
from dotenv import load_dotenv
load_dotenv()

# Example knowledge base (dictionary format)
knowledge_base = {
    "smolagents": "Smolagents is a lightweight AI framework for building agentic applications.",
    "hugging face": "Hugging Face is an AI company that develops open-source tools and models.",
    "llm": "Large Language Models (LLMs) are AI systems trained to understand and generate text."
}

# Define a simple retrieval tool
@tool
def retrieve_info(query: str) -> str:
    """
    Retrieves relevant information from a predefined knowledge base.

    Args:
    query: A keyword to look up in the knowledge base.

    Returns:
    The retrieved information or a default message if not found.
    """
    return knowledge_base.get(query.lower(), "I don't have information on that topic.")

# Define a simple math tool
@tool
def multiply_numbers(a: int, b: int) -> int:
    """
    Multiplies two numbers.

    Args:
    a: The first number.
    b: The second number.

    Returns:
    The product of a and b.
    """
    return a * b

# Initialize the Augmented Code Agent
# Initialize the model: This model will power the agent's reasoning and code generation.
model = InferenceClientModel()
agent = CodeAgent(
    tools=[retrieve_info, multiply_numbers],  # Using retrieval and computation tools
    model=model  # LLM backend
)

# Example query combining retrieval and computation
response = agent.run("What is Smolagents? Also, what is 7 times 6?")

print(response)
