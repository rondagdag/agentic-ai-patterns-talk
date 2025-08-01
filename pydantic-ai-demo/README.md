# Building Effective Agents with Pydantic AI 🍌

*BELLO!* Welcome to Gru's laboratory for agentic AI patterns using minion-themed examples!

Code examples for the agentic AI patterns discussed in the excellent article
[Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)
by [Erik Schluntz](https://github.com/eschluntz) and [Barry Zhang](https://github.com/ItsBarryZ)
of Anthropic, inspired, ported and adapted from the
[code samples](https://github.com/anthropics/anthropic-cookbook/tree/main/patterns/agents)
by the authors.

The examples rely on [Pydantic AI](https://ai.pydantic.dev/), an agentic AI
orchestration library that is particularly well-suited for implementing these patterns
with clarity and precision. All examples use a fun minion theme to demonstrate how
AI agents can work together in Gru's evil laboratory operations!

These examples complement the original code accompanying the article and hopefully
serve a dual purpose, demonstrating both the foundational agentic AI patterns discussed
in the article and the use of Pydantic AI in a delightful minion context.

## Minion Laboratory Notebooks 🔬

### 1. Basic Workflows: Minion Task Management
**File:** [`basic_workflows.ipynb`](basic_workflows.ipynb) [📖](https://nbsanity.com/intellectronica/building-effective-agents-with-pydantic-ai/blob/main/basic_workflows.ipynb)

Learn the fundamental agentic AI patterns through minion operations:

- **🔗 Prompt Chaining**: Transform minion performance data through sequential processing steps, from raw reports to formatted analytics tables
- **🛤️ Routing**: Automatically route minion support tickets to specialized teams (Banana Supply, Gadget Support, Security, Training) based on content analysis
- **⚡ Parallelization**: Analyze stakeholder impacts across multiple groups (Minions, Scientists, Gru, Suppliers) simultaneously for faster processing

**How to run**: Open the notebook and execute cells sequentially. Each section demonstrates a different workflow pattern with minion-themed examples.

### 2. Orchestrator and Workers: Minion Team Coordination
**File:** [`orchestrator_workers.ipynb`](orchestrator_workers.ipynb) [📖](https://nbsanity.com/intellectronica/building-effective-agents-with-pydantic-ai/blob/main/orchestrator_workers.ipynb)

Master the art of delegating complex tasks to specialized minion workers:

- **🎯 Task Orchestration**: Break down complex minion operations (like creating training manuals) into specialized subtasks
- **👥 Parallel Worker Execution**: Deploy multiple minion workers with different specializations (enthusiastic, technical, banana-focused) to handle tasks simultaneously
- **📋 Result Integration**: Collect and organize outputs from all worker minions into comprehensive results

**How to run**: Execute the notebook cells to see how an orchestrator agent analyzes a complex minion task, breaks it into specialized subtasks, and coordinates multiple worker agents to complete them in parallel.

### 3. Evaluator and Optimizer: Minion Quality Control
**File:** [`evaluator_optimizer.ipynb`](evaluator_optimizer.ipynb) [📖](https://nbsanity.com/intellectronica/building-effective-agents-with-pydantic-ai/blob/main/evaluator_optimizer.ipynb)

Implement continuous improvement through AI-powered evaluation and optimization:

- **🔍 Iterative Generation**: Create solutions and continuously improve them based on feedback
- **✅ Quality Evaluation**: Use AI agents to critically assess code quality, efficiency, and best practices
- **🔄 Feedback Loop**: Automatically refine solutions until they meet high standards (PASS/NEEDS_IMPROVEMENT/FAIL evaluations)
- **📈 Chain of Thought**: Track the improvement process and reasoning behind each iteration

**How to run**: Run the notebook to see the evaluator-optimizer pattern in action with a coding challenge (implementing an O(1) stack with getMin()). Watch as the system iteratively improves the solution based on detailed feedback.

## Setup Instructions 🛠️

Follow these steps to get your minion laboratory up and running:

1. **Environment Configuration**
   ```bash
   cp dot.env .env
   ```

2. **API Keys Setup**
   Fill in the API keys for one or more of your LLM provider(s) in the `.env` file

3. **Model Selection**
   Set `AI_MODEL` to the model you want to use
   (see https://ai.pydantic.dev/models/ for supported providers and models)

   **Examples:**
   ```bash
   # OpenAI
   OPENAI_API_KEY=sk-123456789
   AI_MODEL=openai:gpt-4o
   ```
   ```bash
   # Google Gemini
   GEMINI_API_KEY=ABC-123_xyz
   AI_MODEL=gemini-1.5-pro
   ```
   ```bash
   # Anthropic Claude
   ANTHROPIC_API_KEY=ABC-sk-123456789
   AI_MODEL=claude-3-5-sonnet-latest
   ```
   ```bash
   # Azure AI Foundry
   AZURE_API_KEY=your-azure-api-key
   AZURE_ENDPOINT=https://your-endpoint.openai.azure.com/
   AZURE_API_VERSION=2024-08-01-preview
   AI_MODEL=azure:gpt-4o
   ```
   ```bash
   # Ollama (local models - requires Ollama installation)
   AI_MODEL=ollama:llama3.2:latest
   # No API key needed for Ollama
   ```
   
   💡 **Pro Tip**: You can omit the `AI_MODEL` variable to randomly select from all available models with configured API keys - great for comparing different models!

4. **Optional: Ollama Setup (for local models)**
   ```bash
   # Install Ollama
   brew install ollama  # macOS
   # or download from https://ollama.ai/
   
   # Pull a model
   ollama pull llama3.2:latest
   
   # Start Ollama server
   ollama serve
   ```

5. **Optional: Azure AI Foundry Setup**
   To use Azure AI Foundry models, you'll need to:
   
   1. **Create an Azure AI Foundry Project**:
      - Go to [Azure AI Foundry](https://ai.azure.com/)
      - Create a new project or use an existing one
      - Navigate to your project's **Models** section
   
   2. **Deploy a Model**:
      - Click **Deploy model** in your Azure AI Foundry project
      - Select from available models (e.g., GPT-4o, GPT-4o-mini)
      - Complete the deployment process
      - Note the **deployment name** (this will be your model name)
   
   3. **Get Your Credentials**:
      - **API Key**: Go to your project **Settings** → **Keys and Endpoints**
      - **Endpoint**: Your Azure OpenAI endpoint URL (format: `https://your-resource.openai.azure.com/`)
      - **API Version**: Use `2024-08-01-preview` (or check Azure docs for latest)
   
   4. **Configure Environment Variables**:
      ```bash
      AZURE_API_KEY=your-azure-api-key
      AZURE_ENDPOINT=https://your-resource.openai.azure.com/
      AZURE_API_VERSION=2024-08-01-preview
      AI_MODEL=azure:gpt-4o  # Use your deployment name here
      ```
   
   💡 **Important**: The model name in `AI_MODEL` should match your **deployment name** in Azure AI Foundry, not necessarily the base model name.
   
   🔐 **Security**: Azure AI Foundry provides enterprise-grade security, compliance, and data residency controls, making it ideal for production deployments.

6. **Optional: Observability Setup**
   Set the `LOGFIRE_TOKEN` variable to instrument Pydantic AI and monitor agent calls with [Pydantic Logfire](https://logfire.pydantic.dev/).

## Running the Notebooks 🚀

### Prerequisites
Make sure you have Python 3.8+ and Jupyter installed. If using VS Code, the Python and Jupyter extensions are recommended.

### Quick Start
1. Open any notebook file (`.ipynb`) in your preferred environment
2. The first cell in each notebook will automatically install required dependencies:
   ```python
   %pip install -r requirements.txt
   ```
3. Run cells sequentially - each notebook is designed to be self-contained
4. Watch the minions work their magic! 🍌

### Best Practices
- **Sequential Execution**: Run notebook cells in order for the best experience
- **Environment Variables**: Ensure your `.env` file is properly configured before running
- **Model Selection**: Try different models by changing the `AI_MODEL` variable to see how different LLMs handle minion tasks
- **Observability**: Enable Logfire logging to see detailed agent interactions and decision-making processes

**BELLO!** You're now ready to explore agentic AI patterns with Gru's minion laboratory! 🎉