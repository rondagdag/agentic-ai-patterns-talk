from smolagents import CodeAgent, InferenceClientModel, tool
import pprint
from dotenv import load_dotenv
load_dotenv()

# Initialize the LLM model
model = InferenceClientModel()

# Define the two-step workflow
def prompt_chaining_workflow(topic: str) -> str:
    """
    Implements a two-step prompt chaining workflow to generate a structured blog post outline.

    Args:
        topic (str): The topic of the blog post.

    Returns:
        str: The validated outline.
    """
    agent = CodeAgent(model=model, tools=[])

    # Step 1: Generate a blog post outline
    outline_prompt = f"Generate a structured outline for a blog post on '{topic}'."
    outline = agent.run(outline_prompt)
    print("\nOutline Generated:\n", outline)

    # Step 2: Validate the outline
    validation_prompt = f"Review the following outline and suggest improvements:\n{outline}"
    validated_outline = agent.run(validation_prompt)
    print("\nValidated Outline:\n", validated_outline)

    # Step 3: Convert the outline to JSON format
    json_prompt = f"Convert the following outline to JSON format with arrays:\n{validated_outline}"
    json_outline = agent.run(json_prompt)
    print("\nJSON Outline:\n", json_outline)

    # Step 4: Pretty-print the JSON outline
    pp = pprint.PrettyPrinter(indent=4)
    formatted_json_outline = pp.pformat(json_outline)
    print("\nFormatted JSON Outline:\n", formatted_json_outline)

    return formatted_json_outline

# Run the workflow with an example topic
prompt_chaining_workflow("The Future of AI Agents")
