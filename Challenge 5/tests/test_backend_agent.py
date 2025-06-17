import unittest
from evaluation.evaluator import evaluate_text
from app.backend import generate_bot_response
from tabulate import tabulate

def save_dataframe_to_txt(df, file_path):
    with open(file_path, "w") as f:
        f.write(tabulate(df, headers="keys", tablefmt="grid", showindex=False))

class BotEvaluationTest(unittest.TestCase):
    def test_valid_response(self):
        """Test that a valid LLM response is fluent and grounded."""
        question = "what about uplowed roads?"

        # Direct LLM response instead of generate_bot_response()
        expected_responses = (
            "You can report an unplowed road by contacting your local ADS regional office. Each region has a dedicated hotline for snow-related service requests and emergencies. "
            "To report an unplowed road, reach out to your local ADS regional office. Every region operates a hotline specifically for snow-related service requests and emergencies."
        )

        result = generate_bot_response(question)
        df = evaluate_text(result, expected_responses)
        save_dataframe_to_txt(df, "output/valid_response_output.txt")

        fluency = float(df["fluency_score"].iloc[0])
        groundedness = float(df["groundedness_score"].iloc[0])

        self.assertGreaterEqual(fluency, 3.0, "Fluency score is too low for valid response")
        self.assertGreaterEqual(groundedness, 3.0, "Groundedness score is too low for valid response")

    def test_irrelevant_response(self):
        """Test that an irrelevant LLM response has low groundedness."""
        question = "how to apply for drivers license?"

        # Irrelevant LLM response
        expected_response = "Apply from the Driver Permit website."

        result = generate_bot_response(question)
        df = evaluate_text(result, expected_response)
        save_dataframe_to_txt(df, "output/irrelevant_response_output.txt")

        groundedness = float(df["groundedness_score"].iloc[0])
        self.assertLessEqual(groundedness, 4.0, f"Expected low groundedness for unrelated query, got {groundedness}")

if __name__ == "__main__":
    unittest.main()
