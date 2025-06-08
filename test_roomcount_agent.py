from typing import Optional, List, Dict
from roomcount_agent import agent as roomcount_agent
from agno.eval.accuracy import AccuracyEval, AccuracyResult
from agno.models.openai import OpenAIChat

test_cases: List[Dict[str, str]] = [
    {
        "prompt": "How many total rooms does 'Rede Andrade Solmar' in 'Joao Pessoa' have?",
        "expected": "total_rooms=79",
    },
    {
        "prompt": "How many total rooms does 'Bristol' in 'Benidorm' have?",
        "expected": "total_rooms=212",
    },
    {
        "prompt": "How many total rooms does 'Playa Moreia' in 'Mallorca' have?",
        "expected": "total_rooms=133",
    },
    {
        "prompt": "How many total rooms does 'Hostal Aravaca Garden' in 'Madrid' have?",
        "expected": "total_rooms=25",
    },
]


def run_accuracy_tests():
    scores: List[float] = []

    for idx, case in enumerate(test_cases, start=1):

        eval_case = AccuracyEval(
            num_iterations=5,
            model=OpenAIChat(id="o4-mini"),
            agent=roomcount_agent,
            input=case["prompt"],
            expected_output=case["expected"],
            additional_guidelines="The agent must return exactly: hotel_name, location, total_rooms, confidence_score, evidence_note. And we must compare exactly the number of 'total_rooms'.",
        )

        result: Optional[AccuracyResult] = eval_case.run(print_results=True)
        assert result is not None and result.avg_score >= 8

        scores.append(result.avg_score)

if __name__ == "__main__":
    run_accuracy_tests()
