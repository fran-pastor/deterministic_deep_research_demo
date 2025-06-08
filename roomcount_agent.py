
#!/usr/bin/env python3
"""
room_count_agent.py
===================
A **single‑file** example (no extra helper functions) that uses the Agno framework
and OpenAI to extract the total number of rooms in a given hotel.

The heavy lifting—searching, parsing, weighting, confidence math—is encoded in
the system prompt. The Python code merely wires up the model, tools and
environment so learners can focus on the prompt engineering aspect.

Environment
-----------
OPENAI_API_KEY   – required for the LLM calls
TAVILY_API_KEY   – required by `TavilyTools` for Google search

More on Agno: https://docs.agno.com
"""

from __future__ import annotations

import os
from textwrap import dedent
from typing import Optional

from dotenv import load_dotenv
from pydantic import BaseModel, Field

from agno.agent import Agent
from agno.models.openai.chat import OpenAIChat
from agno.tools.tavily import TavilyTools

from rich.text import Text

###############################################################################
# Constants and Config
###############################################################################

REQUIRED_ENV_VARS = ("OPENAI_API_KEY", "TAVILY_API_KEY")

###############################################################################
# Data model
###############################################################################

class HotelRoomInfo(BaseModel):
    hotel_name: str = Field(..., description="Exact name of the hotel.")
    location: str = Field(..., description="City or location of the hotel.")
    total_rooms: Optional[int] = Field(None, description="Total number of rooms, if available.")
    confidence_score: Optional[float] = Field(None, description="Confidence from 0.0 (very uncertain) to 1.0 (very confident).")
    evidence_note: Optional[str] = Field(None, description="Brief note about which domains provided the data.")

    def __rich_console__(self, console, options):
        yield Text(self.json())

###############################################################################
# System Prompt
###############################################################################

# The core logic of search, parsing, and decision-making is embedded entirely
# in the system prompt below.
SYS = dedent("""
You are an autonomous web-research agent.

# Persistence
Keep working until the user’s query is fully resolved; do not yield control early.

# Tool-Calling
If unsure of any fact, call Tavily; do **not** guess.

# Planning
Before every tool call, draft a silent plan. After the call, reflect silently on whether the result advances the goal. Never reveal these thoughts.

## Task
Determine the **total number of guest rooms** for the hotel supplied by the user.

### Variables
• hotel_name: string   # exact name from user

### Workflow
1. **Generate ≥ 4 semantically distinct search queries.**
   • Brainstorm ≥ 6 synonyms/translations for “total number of guest rooms”.  
     – Include ≥ 1 English phrase **and** ≥ 1 phrase in the hotel’s local language (infer from location).  
   • Select four phrases differing by at least two content words.  
   • Build each query: `"hotel_name" <phrase>` (≤ 12 words, no Boolean operators unless required).

2. **Search the web** with Tavily for each query:  
   • Params: `search_depth="advanced", max_results=10, format="json", time_range="year"`.  
   • If the call fails or returns < 2 results, retry once with `search_depth="basic", max_results=20`.  
   • Record every explicit integer claimed as the room total, plus snippet and URL.

3. **Rank sources**  
   a. Hotel’s official site or fact sheet.  
   b. Reputable sources (tourism boards, major OTAs, investor materials, global news).  
   c. Others.

4. **Resolve conflicts**  
   • If an official-site number exists ⇒ choose it (`confidence = high`).  
   • Else choose the number appearing in **≥ 75 %** of reputable sources (`confidence = medium`).  
   • Else output `"unknown"` (`confidence = low`).

5. **Citations**: keep ≥ 2 distinct supporting URLs when available.

6. **Validate output**: `hotel_name` matches input exactly, `total_rooms` is an integer, URLs are valid.

### Output (return **only** this JSON)
```json
{
  "hotel_name": "...",
  "location": "...",
  "total_rooms": 123,
  "confidence_score": 0.85,
  "evidence_note": ""
}
```

### Example queries (for a hotel in Spain)
1. "Hotel Ejemplo" total guest rooms
2. "Hotel Ejemplo" número total de habitaciones
3. "Hotel Ejemplo" room count
4. "Hotel Ejemplo" cantidad total de cuartos

""")

###############################################################################
# Environment & Agent setup
###############################################################################

# Load env-vars from .env
load_dotenv()

# Fail fast if mandatory keys are missing
missing = [var for var in REQUIRED_ENV_VARS if not os.getenv(var)]
if missing:
    raise RuntimeError(f"Missing env vars: {', '.join(missing)}. See script docstring.")

# Instantiate the agent
agent = Agent(
    model=OpenAIChat(
        "gpt-4.1-2025-04-14",
        temperature=0.0,
    ),
    tools=[TavilyTools(
        search_depth="advanced",
        format="json"
    )],
    system_message=SYS,
    response_model=HotelRoomInfo,
    use_json_mode=True,
    show_tool_calls=False,
    stream=False,
    debug_mode=False
)

###############################################################################
# Entry point
###############################################################################

def query_hotels():
    queries = [
        ("Rede Andrade Solmar", "Joao Pessoa"),
        ("Bristol", "Benidorm"),
        ("Playa Moreia", "Mallorca"),
        ("Hostal Aravaca Garden", "Madrid"),
    ]
    for name, location in queries:
        try:
            prompt = f"How many total rooms does '{name}' in '{location}' have?"
            agent.print_response(prompt, stream=False)
        except Exception as e:
            print(f"Error querying {name} in {location}: {e}")

if __name__ == "__main__":
    query_hotels()