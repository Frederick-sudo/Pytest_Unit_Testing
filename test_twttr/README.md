Project: Unit Testing of "shorten(text)" Function
Tools: Python 3.11, pytest 8.3, pytest-cov
Goal: Verify correctness and robustness of vowel-removal logic across normal, edge, and mixed input types.

Summary:
Total Tests: 18
Pass Rate: 100%
Coverage: 100% (Function + Branch)

Test Coverage:
Total test cases: 18
Pass rate: 100%

Test Results:
| ID     | Scenario                                      | Input                | Expected          | Actual           | Status | Duration |
|--------|-----------------------------------------------|----------------------|-------------------|------------------|--------|----------|
| TC_001 | Remove vowels from phrase with spaces         | What is up           | Wht s p           | Wht s p          | Pass   | 0.001s   |
| TC_002 | Handle sentence with special characters       | Hey, nice to meet ya!| Hy, nc t mt y!    | Hy, nc t mt y!   | Pass   | 0.002s   |
| TC_003 | Input contains no vowels                      | Rhythm               | Rhythm            | Rhythm           | Pass   | 0.001s   |
| TC_004 | All lowercase vowels removed                  | apple                | ppl               | ppl              | Pass   | 0.001s   |
| TC_005 | All uppercase vowels removed                  | BANANA               | BNN               | BNN              | Pass   | 0.001s   |
| TC_006 | Word with letters and numbers                 | ThisisCS50           | ThssCS50          | ThssCS50         | Pass   | 0.001s   |
| TC_007 | All uppercase letters                         | POTTER               | PTTR              | PTTR             | Pass   | 0.001s   |
| TC_008 | Text with punctuation marks                   | Hello!               | Hll!              | Hll!             | Pass   | 0.001s   |
| TC_009 | Empty string                                  | ""                   | ""                | ""               | Pass   | 0.000s   |
| TC_010 | Single lowercase consonant                    | b                    | b                 | b                | Pass   | 0.000s   |
| TC_011 | Single uppercase consonant                    | G                    | G                 | G                | Pass   | 0.000s   |
| TC_012 | Single lowercase vowel                        | a                    | ""                | ""               | Pass   | 0.000s   |
| TC_013 | Single uppercase vowel                        | U                    | ""                | ""               | Pass   | 0.000s   |
| TC_014 | All lowercase vowels only                     | aueioau              | ""                | ""               | Pass   | 0.001s   |
| TC_015 | All uppercase vowels only                     | AIEUOIUEO            | ""                | ""               | Pass   | 0.001s   |
| TC_016 | Mixed case vowels only                        | aEioeAUOeiAOIUIEO    | ""                | ""               | Pass   | 0.002s   |
| TC_017 | Numeric string                                | 12345678             | 12345678          | 12345678         | Pass   | 0.001s   |
| TC_018 | Symbols only                                  | !@#!&()              | !@#!&()           | !@#!&()          | Pass   | 0.001s   |

