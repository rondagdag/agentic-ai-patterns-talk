import os
import random
import subprocess
from pprint import pformat, pprint
from dotenv import load_dotenv
import nest_asyncio


def _check_ollama_availability():
    """Check if Ollama server is available and return list of available models."""
    try:
        # Try to check if ollama command is available and server is running
        result = subprocess.run(['ollama', 'list'], 
                              capture_output=True, 
                              text=True, 
                              timeout=3)
        return result.returncode == 0
    except (subprocess.TimeoutExpired, subprocess.CalledProcessError, FileNotFoundError):
        return False


def _get_ollama_models():
    """Get list of available Ollama models."""
    try:
        result = subprocess.run(['ollama', 'list'], 
                              capture_output=True, 
                              text=True, 
                              timeout=3)
        if result.returncode == 0:
            lines = result.stdout.strip().split('\n')[1:]  # Skip header
            models = []
            for line in lines:
                if line.strip():
                    model_name = line.split()[0]  # First column is the model name
                    # Convert to ollama: prefix format
                    models.append(f'ollama:{model_name}')
            return models
    except (subprocess.TimeoutExpired, subprocess.CalledProcessError, FileNotFoundError):
        pass
    return []


def initialize():
    load_dotenv(override=True)

    _ai_models = (
        [] + 
        (['openai:gpt-4o', 'openai:gpt-4o-mini'] if os.environ.get('OPENAI_API_KEY') else []) +
        (['gemini-1.5-pro', 'gemini-2.0-flash-exp'] if os.environ.get('GEMINI_API_KEY') else []) +
        (['claude-3-5-haiku-latest', 'claude-3-5-sonnet-latest'] if os.environ.get('ANTHROPIC_API_KEY') else []) +
        (['azure:gpt-4o', 'azure:gpt-4o-mini'] if os.environ.get('AZURE_API_KEY') else [])
    )
    print(f"Available AI models:\n{pformat(_ai_models)}")

# (_get_ollama_models() if _check_ollama_availability() else [])
    _ai_model = (
        os.environ['AI_MODEL']
        if os.environ.get('AI_MODEL')
        else random.choice(_ai_models) if _ai_models else None
    )
    print()
    print(f"Using AI model: {_ai_model}")

    nest_asyncio.apply()

    if os.environ.get('LOGFIRE_TOKEN'):
        import logfire
        logfire.configure(console=False)  
        logfire.instrument_asyncpg()

    # Return the configured model object for Ollama/Azure or model name for others
    if _ai_model and _ai_model.startswith('ollama:'):
        from pydantic_ai.models.openai import OpenAIModel
        from pydantic_ai.providers.openai import OpenAIProvider
        
        # Extract the actual model name (remove 'ollama:' prefix)
        model_name = _ai_model[7:]  # Remove 'ollama:' prefix
        ollama_base_url = os.environ.get('OLLAMA_BASE_URL', 'http://localhost:11434/v1')
        
        print(f"Configuring Ollama model: {model_name} at {ollama_base_url}")
        return OpenAIModel(
            model_name=model_name,
            provider=OpenAIProvider(base_url=ollama_base_url)
        )
    elif _ai_model and _ai_model.startswith('azure:'):
        from pydantic_ai.models.openai import OpenAIModel
        from pydantic_ai.providers.azure import AzureProvider
        
        # Extract the actual model name (remove 'azure:' prefix)
        model_name = _ai_model[6:]  # Remove 'azure:' prefix
        
        # Get Azure configuration from environment variables
        azure_endpoint = os.environ.get('AZURE_ENDPOINT')
        azure_api_version = os.environ.get('AZURE_API_VERSION', '2024-08-01-preview')
        azure_api_key = os.environ.get('AZURE_API_KEY')
        
        if not azure_endpoint:
            raise ValueError("AZURE_ENDPOINT environment variable is required for Azure AI Foundry models")
        if not azure_api_key:
            raise ValueError("AZURE_API_KEY environment variable is required for Azure AI Foundry models")
        
        print(f"Configuring Azure AI Foundry model: {model_name} at {azure_endpoint}")
        return OpenAIModel(
            model_name=model_name,
            provider=AzureProvider(
                azure_endpoint=azure_endpoint,
                api_version=azure_api_version,
                api_key=azure_api_key
            )
        )
    
    return _ai_model


def show(txt, title=None):
    try:
        # Try to use IPython display for markdown rendering
        from IPython.display import display, Markdown
        
        # Always try to display as markdown in Jupyter environments
        if title:
            display(Markdown(f"### {title}"))
        if txt:
            if type(txt) == str:
                # Check if the text contains markdown table or other markdown elements
                if ('```markdown' in txt or 
                    txt.strip().startswith('|') or 
                    any(marker in txt for marker in ['# ', '## ', '### ', '**', '__', '`', '[', ']('])):
                    # Remove markdown code block wrapper if present
                    clean_txt = txt.replace('```markdown\n', '').replace('\n```', '').strip()
                    display(Markdown(clean_txt))
                else:
                    display(Markdown(f"```\n{txt}\n```"))
            else:
                display(Markdown(f"```\n{pformat(txt)}\n```"))
        return
    except ImportError:
        # Fall back to regular print if IPython is not available
        pass
    
    # Fallback to original print-based implementation
    print()
    if title:
        print(title)
        print('-' * len(title))
        print()
    if txt:
        if type(txt) == str:
            print(txt)
        else:
            pprint(txt)
        print()
