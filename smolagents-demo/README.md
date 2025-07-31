# agentic-ai-patterns-talk

## How to Run the Code

1. **Install Python dependencies**
	You can install all required dependencies using the provided `requirements.txt` file:
	```bash
	pip install -r requirements.txt
	```
	pip install smolagents python-dotenv
	```

2. **Get your Hugging Face token**
	- Go to https://huggingface.co/settings/tokens
	- Click "New token" and copy your token.

3. **Log in to Hugging Face**
	Run this command in your terminal and paste your token when prompted:
	```bash
	huggingface-cli login
	```

4. **(Optional) Set environment variables**
	If your code or model provider requires an API key (e.g., Nebius), create a `.env` file in the project root:
	```
	NEBIUS_API_KEY=your_api_key_here
	```

5. **Run the code**
	```bash
	python 1-augmented-llm.py
	```

You should see the agent's response printed in your terminal.