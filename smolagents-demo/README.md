# Smolagents Demo - Interactive Agentic AI Patterns

This directory contains interactive Python scripts demonstrating agentic AI patterns using [Smolagents](https://huggingface.co/docs/smolagents/), a lightweight framework from Hugging Face for building AI agents with Gradio web interfaces.

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- [Ollama](https://ollama.ai/) (recommended for local models)

### Installation

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up Ollama (recommended):**
   ```bash
   # Install Ollama
   brew install ollama  # macOS
   # or download from https://ollama.ai/
   
   # Pull the model
   ollama pull llama3.2:latest
   
   # Start Ollama server
   ollama serve
   ```

3. **Set up API Keys and Model Configuration**
   Create a `.env` file for your chosen provider:
   
   **For Azure AI Foundry (Recommended for Production):**
   ```bash
   AZURE_API_KEY=your-azure-api-key
   AZURE_ENDPOINT=https://your-resource.openai.azure.com/
   AZURE_API_VERSION=2024-08-01-preview
   ```
   
   **For Ollama (Local Models - No API key needed):**
   ```bash
   # For Hugging Face models
   HF_TOKEN=your_hugging_face_token
   
   # For other providers
   OPENAI_API_KEY=your_openai_key
   ANTHROPIC_API_KEY=your_anthropic_key
   ```

## 📁 Examples Overview

### Interactive Chat Interfaces (with Gradio UI)

#### `1-0-augmented-llm.py` - Basic Agent with Tools
**Run:** `python 1-0-augmented-llm.py`

- **Features:** Knowledge retrieval, math calculations
- **Tools:** Custom knowledge base lookup, number multiplication
- **UI:** Gradio chat interface at `http://localhost:7860`
- **Try:** "What is smolagents?" or "What is 15 times 8?"

#### `1-1-gradio-chat.py` - Web Search Agent
**Run:** `python 1-1-gradio-chat.py`

- **Features:** Web search capabilities, file uploads
- **Tools:** WebSearchTool for real-time information
- **UI:** Gradio chat interface at `http://localhost:7860`
- **Try:** "Search for recent AI news" or upload files for analysis

### Command-Line Examples (Terminal Output)

#### `2-1-prompt-chaining.py` - Sequential Processing
**Run:** `python 2-1-prompt-chaining.py`

**Pattern:** Prompt Chaining
- Generates blog post outline
- Validates and suggests improvements  
- Revises based on feedback
- **Output:** Shows each step in terminal

#### `2-2-routing-agent.py` - Smart Query Routing
**Run:** `python 2-2-routing-agent.py`

**Pattern:** Agent Routing
- Classifies customer queries
- Routes to specialized agents (general, refund, tech support)
- **Output:** Demonstrates routing for different query types

#### `2-3-orchestrator-workers.py` - Task Coordination
**Run:** `python 2-3-orchestrator-workers.py`

**Pattern:** Orchestrator-Workers
- Breaks complex tasks into subtasks
- Assigns to worker agents in parallel
- Synthesizes final report
- **Output:** Shows task decomposition and results

## 🎯 Using the Gradio Chat Interface

For interactive examples (`1-0-augmented-llm.py` and `1-1-gradio-chat.py`):

1. **Launch:** Run the script - browser opens automatically to `http://localhost:7860`
2. **Chat:** Type messages in the interface
3. **File Upload:** Drag & drop files (saved to `./data` folder)
4. **Tools:** Agent automatically uses available tools
5. **Stop:** Press `Ctrl+C` in terminal

### Example Conversations

**With Knowledge Agent (`1-0-augmented-llm.py`):**
- "What is smolagents?" → Uses knowledge retrieval
- "Calculate 7 times 6" → Uses math tool
- "Tell me about LLMs" → Combines knowledge and reasoning

**With Web Search Agent (`1-1-gradio-chat.py`):**
- "What's the latest news about AI?" → Live web search
- "Find information about Python frameworks" → Web search + analysis
- Upload a document → File analysis with search context

## 🔧 Configuration

### Azure AI Foundry Setup (Recommended for Production)

Azure AI Foundry provides enterprise-grade security, compliance, and data residency controls, making it ideal for production deployments.

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
   ```

💡 **Important**: The model name in `AI_MODEL` should match your **deployment name** in Azure AI Foundry, not necessarily the base model name.

### Ollama Setup (Local Models)

Ollama allows you to run large language models locally on your machine, providing privacy and no API costs.

1. **Install Ollama**:
   ```bash
   # macOS
   brew install ollama
   
   # Or download from https://ollama.ai/
   ```

2. **Pull and Run Models**:
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

3. **Configure in Python Scripts**:
   - No `.env` file needed for Ollama
   - Models run locally without API keys
   - Set `AI_MODEL=ollama:llama3.2:latest` in your environment or script

### Switching Models

Edit the `model_id` in any Python file:

```python
# For Azure AI Foundry
model = LiteLLMModel(
    model_id="gpt-4o",  # Your Azure deployment name
    api_base="https://your-resource.openai.azure.com/",
    api_key="your-azure-api-key",
    api_version="2024-08-01-preview"
)

# For local Ollama models
model = LiteLLMModel(
    model_id="ollama/llama3.2:latest",  # or llama3.2:3b for faster responses
    api_base="http://localhost:11434",
    api_key="ollama"
)

# For cloud models (requires API keys in .env)
model = InferenceClientModel(model_id="microsoft/DialoGPT-medium")
```

### Adding Custom Tools

See `1-0-augmented-llm.py` for examples of creating custom tools:

```python
@tool
def your_custom_tool(input: str) -> str:
    """Description of what your tool does."""
    # Your tool logic here
    return result
```

## 🛠 Troubleshooting

**Azure AI Foundry Issues:**
- Verify API key, endpoint, and deployment name are correct
- Check Azure resource is active and deployment is running
- Ensure API version is supported (use `2024-08-01-preview`)
- Check Azure portal for quota limits and billing status

**Ollama Connection Issues:**
- Ensure Ollama is running: `ollama serve`
- Check model is available: `ollama list`
- Verify Ollama is accessible: `curl http://localhost:11434/api/tags`
- Try pulling the model again: `ollama pull llama3.2:latest`

**Gradio Interface Issues:**
- Check port 7860 is available
- Try different port: `GradioUI(agent).launch(server_port=7861)`
- Clear browser cache or try incognito mode

**Missing Dependencies:**
```bash
# Install specific packages if needed
pip install smolagents[litellm]
pip install smolagents[toolkit] 
pip install python-dotenv gradio
```

**Model Performance Tips:**
- **Azure**: Use GPT-4o for best results, GPT-4o-mini for faster/cheaper responses
- **Ollama**: Use `llama3.2:3b` for faster responses on lower-end hardware
- **Ollama**: Use `llama3.2:latest` (8B) for better quality responses

## 📚 Learn More

- **Smolagents Documentation:** https://huggingface.co/docs/smolagents/
- **Gradio Documentation:** https://gradio.app/docs/
- **LiteLLM Documentation:** https://docs.litellm.ai/