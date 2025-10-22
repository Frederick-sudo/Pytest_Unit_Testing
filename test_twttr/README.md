#Unit Testing with Pytest

#Project Overview
This project aims to test the "shorten(text)" function in twttr.py, which is a simple program that takes a string as an input, loops through them, removes all vowels found, and hands back the string but with all the found vowels removed. This test covers design for normal, mixed, and edge cases scenarios using pytest.

#Function Under Test
shorten(text: str) -> str

Removes all vowels (a,e,i,o,u) case insensitively from a given string, leaving other characters (letters, digits, punctuation) unchanged.

#Test Design Approach
These tests have been categorized into the following:
  Normal Cases -> typical words and sentences with vowels.
  Mixed Cases -> combinations of letters, numbers, and symbols.
  Edge Cases -> empty strings, all-vowel inputs, or no-vowel inputs.

This categorization ensures that these tests cover functional correctness, input variety coverage, and robustness testing.

#Sample Test Coverage
| Category  | Example Input  | Expected Output | Purpose            |
|-----------|----------------|-----------------|--------------------|
| Normal    | "Twitter"      | "Twttr"         | Typical word       |
| Mixed     | "This is CS50" | "Ths s CS50"    | Letters + digits   |
| Edge      | "AEIOUaeiou"   | ""              | All vowels removed |

#Tools Used
Python 3.x
Pytest -> for automated unit testing

#Running the Tests
bash
pytest -v test_twttr.py
