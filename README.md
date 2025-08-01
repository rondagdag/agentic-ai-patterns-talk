# Building Effective Agents with Pydantic AI 🍌

*BELLO!* Welcome to Gru's laboratory for agentic AI patterns using minion-themed examples!

This repository contains two complementary sets of examples demonstrating agentic AI patterns:

1. **Pydantic AI Demo** - Advanced patterns with minion-themed Jupyter notebooks
2. **Smolagents Demo** - Interactive Python scripts with Gradio UI support

Code examples for the agentic AI patterns discussed in the excellent article
[Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)
by [Erik Schluntz](https://github.com/eschluntz) and [Barry Zhang](https://github.com/ItsBarryZ)
of Anthropic, inspired, ported and adapted from the
[code samples](https://github.com/anthropics/anthropic-cookbook/tree/main/patterns/agents)
by the authors.

The Pydantic AI examples rely on [Pydantic AI](https://ai.pydantic.dev/), an agentic AI
orchestration library that is particularly well-suited for implementing these patterns
with clarity and precision. The Smolagents examples use [Smolagents](https://huggingface.co/docs/smolagents/index), 
a lightweight framework from Hugging Face for building interactive AI agents.

All examples demonstrate how AI agents can work together to solve complex tasks!

## Quick Start Guide 🚀

### Prerequisites

**Required:**
- Python 3.8+ 
- Git

**Optional (for local models):**
- [Ollama](https://ollama.ai/) for running local LLMs

### Choose Your Adventure:

**🎯 Want interactive chat interfaces?** → Start with [Smolagents Demo](#smolagents-demo-)
**📚 Want comprehensive learning with notebooks?** → Start with [Pydantic AI Demo](#pydantic-ai-demo-)

---

## Smolagents Demo 🤖

Interactive Python scripts demonstrating agentic patterns with Gradio web interfaces.

### Setup

1. **Navigate to the smolagents demo:**
   ```bash
   cd smolagents-demo
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up Ollama (recommended for local models):**
   
   **Install Ollama:**
   ```bash
   # macOS
   brew install ollama
   
   # Or download from https://ollama.ai/
   ```
   
   **Pull the required model:**
   ```bash
   ollama pull llama3.2:latest
   ```
   
   **Start Ollama server:**
   ```bash
   ollama serve
   ```

4. **Optional: Set up cloud API keys**
   
   Create a `.env` file if using cloud providers:
   ```bash
   # For Hugging Face models
   HF_TOKEN=your_hugging_face_token
   
   # For other providers (OpenAI, Anthropic, etc.)
   OPENAI_API_KEY=your_openai_key
   ANTHROPIC_API_KEY=your_anthropic_key
   ```

### Running the Examples

#### 1. **Augmented LLM with Gradio Chat** (`1-0-augmented-llm.py`)
Basic agent with tools and interactive chat interface.

```bash
python 1-0-augmented-llm.py
```
- **Features:** Knowledge retrieval, math calculations
- **Tools:** Custom retrieval tool, multiplication tool
- **Access:** Opens Gradio interface at `http://localhost:7860`

#### 2. **Web Search Agent with Gradio Chat** (`1-1-gradio-chat.py`)
Agent with web search capabilities and chat interface.

```bash
python 1-1-gradio-chat.py
```
- **Features:** Web search, file uploads
- **Tools:** WebSearchTool
- **Access:** Opens Gradio interface at `http://localhost:7860`

#### 3. **Prompt Chaining** (`2-1-prompt-chaining.py`)
Sequential processing for blog post generation.

```bash
python 2-1-prompt-chaining.py
```
- **Pattern:** Chained prompts for outline → validation → revision
- **Output:** Terminal output showing each step

#### 4. **Routing Agent** (`2-2-routing-agent.py`)
Intelligent query routing to specialized agents.

```bash
python 2-2-routing-agent.py
```
- **Pattern:** Query classification and routing
- **Agents:** General, refund, technical support
- **Output:** Terminal responses for different query types

#### 5. **Orchestrator-Workers** (`2-3-orchestrator-workers.py`)
Task decomposition and parallel execution.

```bash
python 2-3-orchestrator-workers.py
```
- **Pattern:** Task breakdown → parallel execution → synthesis
- **Output:** Terminal showing subtasks and final report

### Using the Gradio Chat Interface

When you run files `1-0-augmented-llm.py` or `1-1-gradio-chat.py`:

1. **Launch:** The script automatically opens your browser to `http://localhost:7860`
2. **Chat:** Type messages in the chat interface
3. **File Upload:** Drag and drop files for analysis (saved to `./data` folder)
4. **Tools:** The agent automatically uses available tools based on your queries
5. **Stop:** Press `Ctrl+C` in terminal to stop the server

**Example queries to try:**
- "What is smolagents?" (uses knowledge retrieval)
- "What is 15 times 8?" (uses math tool)
- "Search for recent AI news" (uses web search - file `1-1` only)

---

## Pydantic AI Demo 🍌

Advanced agentic patterns demonstrated through minion-themed Jupyter notebooks.

### Setup Instructions �️

1. **Navigate to the pydantic-ai demo:**
   ```bash
   cd pydantic-ai-demo
   ```

2. **Environment Configuration**
   ```bash
   cp dot.env .env
   ```

3. **Choose Your Model Provider**
   
   **Azure AI Foundry (Recommended for Production):**
   
   Azure AI Foundry provides enterprise-grade security, compliance, and data residency controls.
   
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
   
   4. **Configure Environment Variables in `.env`**:
      ```bash
      AZURE_API_KEY=your-azure-api-key
      AZURE_ENDPOINT=https://your-resource.openai.azure.com/
      AZURE_API_VERSION=2024-08-01-preview
      AI_MODEL=azure:gpt-4o  # Use your deployment name here
      ```
   
   💡 **Important**: The model name in `AI_MODEL` should match your **deployment name** in Azure AI Foundry, not necessarily the base model name.
   
   **Ollama (Local Models - Free and Private):**
   
   Ollama allows you to run large language models locally on your machine.
   
   1. **Install Ollama**:
      ```bash
      # macOS
      brew install ollama
      
      # Or download from https://ollama.ai/
      ```
   
   2. **Pull and Start Models**:
      ```bash
      # Pull the model (first time only)
      ollama pull llama3.2:latest
      
      # For faster responses on lower-end hardware
      ollama pull llama3.2:3b
      
      # Start Ollama server (runs in background)
      ollama serve
      
      # Verify installation
      ollama list
      ```
   
   3. **Configure Environment Variables in `.env`**:
      ```bash
      AI_MODEL=ollama:llama3.2:latest
      # No API key needed for Ollama
      ```
   
   **Other Cloud Providers:**
   ```bash
   # OpenAI
   OPENAI_API_KEY=sk-123456789
   AI_MODEL=openai:gpt-4o
   
   # Google Gemini
   GEMINI_API_KEY=ABC-123_xyz
   AI_MODEL=gemini-1.5-pro
   
   # Anthropic Claude
   ANTHROPIC_API_KEY=ABC-sk-123456789
   AI_MODEL=claude-3-5-sonnet-latest
   ```
   
   💡 **Pro Tip**: You can omit the `AI_MODEL` variable to randomly select from all available models with configured API keys - great for comparing different models!

4. **Optional: Observability Setup**
   Set the `LOGFIRE_TOKEN` variable to instrument Pydantic AI and monitor agent calls with [Pydantic Logfire](https://logfire.pydantic.dev/).

### Minion Laboratory Notebooks 🔬

### 1. Basic Workflows: Minion Task Management
**File:** [`basic_workflows.ipynb`](pydantic-ai-demo/basic_workflows.ipynb) [📖](https://nbsanity.com/intellectronica/building-effective-agents-with-pydantic-ai/blob/main/basic_workflows.ipynb)

Learn the fundamental agentic AI patterns through minion operations:

- **🔗 Prompt Chaining**: Transform minion performance data through sequential processing steps, from raw reports to formatted analytics tables
- **🛤️ Routing**: Automatically route minion support tickets to specialized teams (Banana Supply, Gadget Support, Security, Training) based on content analysis
- **⚡ Parallelization**: Analyze stakeholder impacts across multiple groups (Minions, Scientists, Gru, Suppliers) simultaneously for faster processing

**How to run**: Open the notebook and execute cells sequentially. Each section demonstrates a different workflow pattern with minion-themed examples.

### 2. Orchestrator and Workers: Minion Team Coordination
**File:** [`orchestrator_workers.ipynb`](pydantic-ai-demo/orchestrator_workers.ipynb) [📖](https://nbsanity.com/intellectronica/building-effective-agents-with-pydantic-ai/blob/main/orchestrator_workers.ipynb)

Master the art of delegating complex tasks to specialized minion workers:

- **🎯 Task Orchestration**: Break down complex minion operations (like creating training manuals) into specialized subtasks
- **👥 Parallel Worker Execution**: Deploy multiple minion workers with different specializations (enthusiastic, technical, banana-focused) to handle tasks simultaneously
- **📋 Result Integration**: Collect and organize outputs from all worker minions into comprehensive results

**How to run**: Execute the notebook cells to see how an orchestrator agent analyzes a complex minion task, breaks it into specialized subtasks, and coordinates multiple worker agents to complete them in parallel.

### 3. Evaluator and Optimizer: Minion Quality Control
**File:** [`evaluator_optimizer.ipynb`](pydantic-ai-demo/evaluator_optimizer.ipynb) [📖](https://nbsanity.com/intellectronica/building-effective-agents-with-pydantic-ai/blob/main/evaluator_optimizer.ipynb)

Implement continuous improvement through AI-powered evaluation and optimization:

- **🔍 Iterative Generation**: Create solutions and continuously improve them based on feedback
- **✅ Quality Evaluation**: Use AI agents to critically assess code quality, efficiency, and best practices
- **🔄 Feedback Loop**: Automatically refine solutions until they meet high standards (PASS/NEEDS_IMPROVEMENT/FAIL evaluations)
- **📈 Chain of Thought**: Track the improvement process and reasoning behind each iteration

**How to run**: Run the notebook to see the evaluator-optimizer pattern in action with a coding challenge (implementing an O(1) stack with getMin()). Watch as the system iteratively improves the solution based on detailed feedback.

### Running the Notebooks 🚀

#### Prerequisites
Make sure you have Python 3.8+ and Jupyter installed. If using VS Code, the Python and Jupyter extensions are recommended.

#### Quick Start
1. Open any notebook file (`.ipynb`) in your preferred environment
2. The first cell in each notebook will automatically install required dependencies:
   ```python
   %pip install -r requirements.txt
   ```
3. Run cells sequentially - each notebook is designed to be self-contained
4. Watch the minions work their magic! 🍌

#### Best Practices
- **Sequential Execution**: Run notebook cells in order for the best experience
- **Environment Variables**: Ensure your `.env` file is properly configured before running
- **Model Selection**: Try different models by changing the `AI_MODEL` variable to see how different LLMs handle minion tasks
- **Observability**: Enable Logfire logging to see detailed agent interactions and decision-making processes

---

## Ollama Installation Guide 🦙

For running local models with both demos, install Ollama:

### Installation

**macOS:**
```bash
# Using Homebrew (recommended)
brew install ollama

# Or download from website
curl -fsSL https://ollama.ai/install.sh | sh
```

**Linux:**
```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

**Windows:**
Download installer from [https://ollama.ai/download](https://ollama.ai/download)

### Recommended Models to Install

```bash
# For general use (good balance of speed and quality)
ollama pull llama3.2:latest

# For faster responses (smaller model)
ollama pull llama3.2:3b

# For better quality (larger model)
ollama pull llama3.1:8b

# For coding tasks
ollama pull codellama:latest
```

### Starting Ollama

```bash
# Start the Ollama service (runs on localhost:11434)
ollama serve
```

### Testing Your Installation

```bash
# Test that Ollama is working
ollama run llama3.2:latest "Hello, how are you?"
```

### Using with the Demos

Both demo projects are pre-configured to use Ollama with `llama3.2:latest`. If you want to use a different model:

**For Smolagents:** Edit the `model_id` in the Python files:
```python
model = LiteLLMModel(
    model_id="ollama/your-preferred-model:tag",
    api_base="http://localhost:11434",
    api_key="ollama"
)
```

**For Pydantic AI:** Set the `AI_MODEL` in your `.env` file:
```bash
AI_MODEL=ollama:your-preferred-model:tag
```

---

## Troubleshooting 🔧

### Common Issues

**Azure AI Foundry Issues:**
- Verify API key, endpoint, and deployment name are correct
- Check Azure resource is active and deployment is running
- Ensure API version is supported (use `2024-08-01-preview`)
- Check Azure portal for quota limits and billing status
- Verify the model name in `AI_MODEL` matches your deployment name exactly

**Ollama Connection Errors:**
- Ensure Ollama service is running: `ollama serve`
- Check the model is pulled: `ollama list`
- Verify port 11434 is not blocked
- Try pulling the model again: `ollama pull llama3.2:latest`
- Test connectivity: `curl http://localhost:11434/api/tags`

**Missing Dependencies:**
- Run `pip install -r requirements.txt` in the appropriate demo folder
- For Jupyter issues, install: `pip install jupyter notebook`

**API Key Issues:**
- Double-check your `.env` file configuration
- Ensure API keys have proper permissions
- For Hugging Face: `huggingface-cli login`

**Permission Errors:**
- On macOS/Linux, you might need: `chmod +x` for shell scripts
- For Python issues: check virtual environment activation

**Model Performance Tips:**
- **Azure**: Use GPT-4o for best results, GPT-4o-mini for faster/cheaper responses
- **Ollama**: Use `llama3.2:3b` for faster responses on lower-end hardware
- **Ollama**: Use `llama3.2:latest` (8B) for better quality responses

### Getting Help

- **Pydantic AI Docs:** https://ai.pydantic.dev/
- **Smolagents Docs:** https://huggingface.co/docs/smolagents/
- **Ollama Docs:** https://ollama.ai/docs

---

**BELLO!** You're now ready to explore agentic AI patterns with Gru's minion laboratory! 🎉