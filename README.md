
# Deterministic AI Agent for Precise Web Data Extraction

## Overview

This repository presents a practical demonstration of how probabilistic AI technologies, specifically GPT-based models, can be effectively guided to achieve deterministic, reliable, and verifiable results in complex information extraction tasks. The demonstration illustrates how clearly defined workflows and meticulous prompt engineering can direct an AI agent to systematically and accurately retrieve information from web sources.

The showcased example involves determining the precise number of guest rooms available in hotels, using methodical online research and source validation.

## Why Deterministic Agents?

Probabilistic AI models, while powerful, often yield inconsistent results due to their inherent ambiguity. By explicitly embedding structured instructions and decision-making workflows into the agent's prompt, the outcomes become deterministic—ensuring accuracy, repeatability, and trustworthiness essential for critical and advanced agentic processes.

## Project Highlights

- **Structured Interaction**: Leverages the Agno framework to manage structured agent interactions.
- **GPT Integration**: Utilizes OpenAI's GPT models for intelligent parsing and response generation.
- **Advanced Web Research**: Employs Tavily for thorough web data retrieval and validation.

## Installation and Setup

### Virtual Environment

Create and activate a Python virtual environment:

```bash
virtualenv .venv
source .venv/bin/activate
```

### Dependencies

Install required Python packages:

```bash
pip install -r requirements.txt
```

Dependencies include:
- Agno
- OpenAI
- Tavily
- Pydantic
- python-dotenv

(Refer to [`requirements.txt`](requirements.txt) for exact versions.)

### Environment Configuration

Define your API keys in a `.env` file:

```bash
OPENAI_API_KEY=your_openai_key_here
TAVILY_API_KEY=your_tavily_key_here
```

## Running the Agent

Execute the script to run the deterministic AI agent:

```bash
python roomcount_agent.py
```

## Testing and Validation

The repository includes an example test script, `test_roomcount_agent.py`, demonstrating validation cases to ensure deterministic and correct agent behavior.

Run tests using:

```bash
python test_roomcount_agent.py
```

## In-depth Explanation

For a comprehensive exploration of how deterministic AI agents enhance the accuracy and reliability of complex automated processes, read the detailed LinkedIn article:

- [Deterministic AI Agents for Reliable Information Extraction](https://www.linkedin.com/pulse/demo-deep-research-determinista-fran-pastor-yjvwf)

## License

This project is available under the [Apache License 2.0](LICENSE). Feel free to use, modify, and distribute the code, provided appropriate credit is given to this repository.

Explore and leverage deterministic AI workflows for precise and trustworthy information extraction!