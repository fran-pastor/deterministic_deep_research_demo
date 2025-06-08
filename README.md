# Deterministic AI Agent for Accurate Information Extraction

## Overview

This repository demonstrates the effective use of AI agents to deterministically and accurately extract specific information from web resources. Using a robust, structured approach, the agent consistently achieves its intended goal without deviation.

The project illustrates this capability through an example focused on determining the total number of rooms in hotels by conducting systematic online research and validating sources for reliability and accuracy.

## Why This Approach?

The key benefit of the demonstrated process is determinism combined with accuracy. Traditional AI agents might yield variable results or stray from their initial objectives due to ambiguity or misinterpretation. However, by clearly defining workflows and embedding precise instructions within the agent's system prompt, the outcomes become highly reliable, verifiable, and repeatable.

## Implementation

This demonstration uses:

- **Agno framework** for structured agent interactions.
- **OpenAI's GPT models** for understanding and generating text responses.
- **Tavily** for advanced web searches, ensuring comprehensive data retrieval.

See [`requirements.txt`](requirements.txt) for full dependency details.

## Setup

### Install Dependencies

Run the following command to install the required Python packages:

pip install -r requirements.txt

### Environment Variables

Create a `.env` file in the project root with the necessary API keys:

OPENAI_API_KEY=your_openai_key_here
TAVILY_API_KEY=your_tavily_key_here

## Usage

After setting the environment variables, execute the agent by running:

python roomcount_agent.py

## Example Tests

The `test_roomcount_agent.py` script provides example cases demonstrating and validating the deterministic behavior of the agent.

## Further Reading

For an in-depth explanation of how deterministic AI agents enhance accuracy and reliability in automated research processes, refer to the detailed article on LinkedIn:

- [Deterministic AI Agents for Reliable Information Extraction](https://www.linkedin.com/example-article)

## License

This project is licensed under the [Apache License 2.0](LICENSE). You're free to use, modify, and distribute this code, provided appropriate credit is given by referencing this repository.

Enjoy exploring deterministic and accurate AI agent workflows!
