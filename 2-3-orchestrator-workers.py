from smolagents import CodeAgent, InferenceClientModel, tool
from dotenv import load_dotenv
load_dotenv()

# Initialize the LLM model
model = InferenceClientModel()

# Create Worker Agents
worker_agent_1 = CodeAgent(model=model, tools=[], add_base_tools=True)  # Handles first subtask
worker_agent_2 = CodeAgent(model=model, tools=[], add_base_tools=True)  # Handles second subtask

# Define Orchestrator function
def orchestrator(task: str) -> str:
    """
    The orchestrator dynamically breaks down a task, assigns subtasks to worker agents, 
    and synthesizes the final response.

    Args:
        task (str): The user's complex task request.

    Returns:
        str: The synthesized final response.
    """
    # Step 1: Generate subtasks
    orchestrator_agent = CodeAgent(model=model, tools=[])
    subtask_prompt = f"Break down the following task into 2 clear subtasks:\n\nTask: {task}"
    subtasks = orchestrator_agent.run(subtask_prompt).split("\n")

    print("\nGenerated Subtasks:")
    for i, subtask in enumerate(subtasks, 1):
        print(f"{i}. {subtask}")

    # Step 2: Assign tasks to workers
    response_1 = worker_agent_1.run(f"Complete the following subtask: {subtasks[0]}")
    response_2 = worker_agent_2.run(f"Complete the following subtask: {subtasks[1]}")

    # Step 3: Synthesize final response
    synthesis_prompt = (
        f"Combine the following responses into a well-structured final report:\n\n"
        f"Subtask 1 result: {response_1}\n\n"
        f"Subtask 2 result: {response_2}\n"
    )
    final_response = orchestrator_agent.run(synthesis_prompt)

    print("\nFinal Report:\n", final_response)
    return final_response

# Run the orchestrator with an example task
orchestrator("Write a report on the benefits and challenges of AI in healthcare.")
