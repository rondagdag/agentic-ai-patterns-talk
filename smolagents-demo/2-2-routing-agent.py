from smolagents import CodeAgent, LiteLLMModel, InferenceClientModel, tool
from dotenv import load_dotenv
load_dotenv()

# Initialize the LLM model
model = LiteLLMModel(
    model_id="ollama_chat/llama3.2:3b",
    api_base="http://localhost:11434",  # Adjust if using a remote server
    api_key="ollama"  # Replace with your API key if required
)

# model = InferenceClientModel()

# Define specialized agents
general_agent = CodeAgent(model=model, tools=[])
refund_agent = CodeAgent(model=model, tools=[])
tech_support_agent = CodeAgent(model=model, tools=[])

# Routing function
def classify_query(query: str) -> str:
    """
    Classifies a customer query into a category.

    Args:
        query (str): The customer's question.

    Returns:
        str: The category (general, refund, tech).
    """
    agent = CodeAgent(model=model, tools=[])
    classification_prompt = (
        f"Classify this customer query into one of the following categories: "
        f"'general', 'refund', or 'tech'. Only return the category name.\n\nQuery: {query}"
    )
    return agent.run(classification_prompt).strip().lower()

# Routing agent
def routing_agent(user_query: str) -> str:
    """
    Routes the query to the appropriate agent based on classification.

    Args:
        user_query (str): The customer's question.

    Returns:
        str: The response from the appropriate agent.
    """
    category = classify_query(user_query)

    if "refund" in category:
        response = refund_agent.run(f"Handle this refund request: {user_query}")
    elif "tech" in category:
        response = tech_support_agent.run(f"Provide technical support for: {user_query}")
    else:
        response = general_agent.run(f"Answer this general customer inquiry: {user_query}")

    return response

# Example queries
queries = [
    "I need help setting up my phone.",
    "How do I get a refund for my purchase?",
    "What are your store hours?"
]

# Run the routing agent for each query
for q in queries:
    print(f"\nUser Query: {q}")
    print("Agent Response:", routing_agent(q))