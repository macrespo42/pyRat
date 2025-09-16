# pyRat 🏴‍☠️🐀

The free AI agent, powered by Gemini (thanks google)

## Quickstart

First you need to install needed dependencies

```bash
pip install -r requirements.txt
```

then you need to put you google gemini api key in the .env file  
you got an .env.example if needed and the doc to get the free api key is [here](https://ai.google.dev/gemini-api/docs/api-key)

By default the Agents is configured to operate on the test project ./calculator inside the repo  
so you juste to run

```bash
python3 main.py "your prompt"
```

and it will act on calculator app

## Configuration

You can simply configure the project by tweaking parameters in [config.py](./config.py)

Several parameters are available:

- FILE_SIZE_LIMIT: The maximum character gemini can read from a file (usefull for not burning all your tokens on reading a gigantest file)
- ROOT: The working directory (by default ./calculator change by your project path)
- SYSTEM_PROMPT: The preprompt used by the agents customize to your need!
- MAX_ITER: The maximum iter of agents per prompt (he can do 20 actions per prompt by default)
