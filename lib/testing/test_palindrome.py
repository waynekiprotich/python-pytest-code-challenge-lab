import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from palindrome import longest_palindromic_substring

class TestPalindrome:
    
    @pytest.mark.parametrize("input_str, expected_options", [
        ("babad", ["bab", "aba"]),
        ("cbbd", ["bb"]),
        ("racecar", ["racecar"]),
        ("ac", ["a", "c"]) 
    ])
    def test_basic_cases(self, input_str, expected_options):
        result = longest_palindromic_substring(input_str)
        assert result in expected_options, f"Failed for '{input_str}': Expected one of {expected_options}, got '{result}'"

    def test_empty_string(self):
        assert longest_palindromic_substring("") == ""

    def test_single_character(self):
        assert longest_palindromic_substring("a") == "a"
        assert longest_palindromic_substring("Z") == "Z"

    def test_all_same_characters(self):
        assert longest_palindromic_substring("aaaaa") == "aaaaa"

    def test_no_repeating_characters(self):
        result = longest_palindromic_substring("abcdef")
        assert len(result) == 1
        assert result in "abcdef"

    def test_long_string(self):
        long_str = "a" * 1000
        assert longest_palindromic_substring(long_str) == long_str