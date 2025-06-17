import unittest
from unittest.mock import patch
from app import filters

class FilterSafetyTests(unittest.TestCase):

    @patch("app.filters.gemini.generate_content")
    def test_is_prompt_safe_llm_safe(self, mock_generate):
        mock_generate.return_value.text = "SAFE"
        self.assertTrue(filters.is_prompt_safe_llm("How do I get a snow pass?"))

    @patch("app.filters.gemini.generate_content")
    def test_is_prompt_safe_llm_unsafe(self, mock_generate):
        mock_generate.return_value.text = "UNSAFE"
        self.assertFalse(filters.is_prompt_safe_llm("How to make a bomb?"))

    @patch("app.filters.gemini.generate_content")
    def test_is_prompt_safe_llm_unexpected(self, mock_generate):
        mock_generate.return_value.text = "maybe"
        self.assertFalse(filters.is_prompt_safe_llm("unclear input"))

if __name__ == "__main__":
    unittest.main()
