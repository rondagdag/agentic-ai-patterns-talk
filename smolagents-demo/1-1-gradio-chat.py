from smolagents import CodeAgent, GradioUI, InferenceClientModel, WebSearchTool
from smolagents import LiteLLMModel, ToolCallingAgent
# Import necessary modules from smolagents
# LiteLLMModel is used for lightweight LLMs, InferenceClientModel for remote
model = LiteLLMModel(
    model_id="ollama/llama3.2:latest",
    api_base="http://localhost:11434",  # Adjust if using a remote server
    api_key="ollama"  # Replace with your API key if required
)

agent = ToolCallingAgent(
    tools=[WebSearchTool()],
    model=model,
    verbosity_level=1,
    planning_interval=3,
    name="example_agent",
    description="This is an example agent.",
    step_callbacks=[],
    stream_outputs=True,
    # use_structured_outputs_internally=True,
)

GradioUI(agent, file_upload_folder="./data").launch()