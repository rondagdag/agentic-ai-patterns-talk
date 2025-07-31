from smolagents import CodeAgent, LiteLLMModel, InferenceClientModel, WebSearchTool, ToolCallingAgent
import pprint
from dotenv import load_dotenv
load_dotenv()

# Initialize the LLM model
model = LiteLLMModel(
    model_id="ollama/llama3.2:latest",
    api_base="http://localhost:11434",  # Adjust if using a remote server
    api_key="ollama"  # Replace with your API key if required
)

# model = InferenceClientModel()

# Define the two-step workflow
def prompt_chaining_workflow(topic: str) -> str:
    """
    Implements a two-step prompt chaining workflow to generate a structured blog post outline.

    Args:
        topic (str): The topic of the blog post.

    Returns:
        str: The validated outline.
    """
    agent = ToolCallingAgent(model=model, tools=[WebSearchTool()])

    # Step 1: Generate a blog post outline
    outline_prompt = f"Generate a structured outline for a blog post on '{topic}'."
    outline = agent.run(outline_prompt)
    print("\nOutline Generated:\n", outline)

    # Step 2: Validate the outline
    validation_prompt = f"Review the following outline and suggest improvements:\n{outline}"
    suggested_improvements = agent.run(validation_prompt)
    print("\nSuggested Improvements:\n", suggested_improvements)

    # Step 3: Revise the outline based from suggested improvements
    revision_prompt = f"Revise the outline based on the following suggestions:\n{suggested_improvements}\nOutline:\n{outline}"
    revised_outline = agent.run(revision_prompt)
    print("\nRevised Outline:\n", revised_outline)

    # # Step 3: Convert the outline to JSON format
    # json_prompt = f"Convert the following outline to JSON format with arrays:\n{validated_outline}"
    # json_outline = agent.run(json_prompt)
    # print("\nJSON Outline:\n", json_outline)

    # # Step 4: Pretty-print the JSON outline
    # pp = pprint.PrettyPrinter(indent=4)
    # formatted_json_outline = pp.pformat(json_outline)
    # print("\nFormatted JSON Outline:\n", formatted_json_outline)

    return validated_outline

# Run the workflow with an example topic
prompt_chaining_workflow("The Future of AI Agents")
