Project: "Massachusetts Vanity Plate Validator" 

Project Completion Date: October 20,2025

Project Test Date: October 21, 2025

Tools: Python 3.11, pytest 8.3, pytest-cov 

Goal: To validate license plates as per the rules there which are: should be 2-6 characters, the first 2 characters should be alphabets, the first digit should not be 0, and when a digit starts all other characters that follow must be a digit.
_________________________________________
Summary: 

Total Tests: 16 

Pass Rate: 100% 

Coverage: 100% (Function + Branch)
_________________________________________
Test Coverage: 

Total test cases: 16 

Pass rate: 100%
_________________________________________
Test Results:
| ID     | Scenario                                      | Input         | Expected          | Actual           | Status | Duration |
|--------|-----------------------------------------------|---------------|-------------------|------------------|--------|----------|
| TC_001 | Valid 2-letter plate                          | AB            | Valid             | Valid            | Pass   | 0.001s   |
| TC_002 | Valid 6-letter plate                          | ABC123        | Valid             | Valid            | Pass   | 0.001s   |
| TC_003 | Valid vanity plate                            | ABCD          | Valid             | Valid            | Pass   | 0.001s   |
| TC_004 | Valid letters + digits                        | AB12          | Valid             | Valid            | Pass   | 0.001s   |
| TC_005 | Too short (1 char)                            | A             | Invalid           | Invalid          | Pass   | 0.000s   |
| TC_006 | Too long (7+ chars)                           | ABCDEFG       | Invalid           | Invalid          | Pass   | 0.000s   |
| TC_007 | Starts with digit                             | 1ABC          | Invalid           | Invalid          | Pass   | 0.000s   |
| TC_008 | Contains period                               | AB.C          | Invalid           | Invalid          | Pass   | 0.000s   |
| TC_009 | Contains space                                | AB CD         | Invalid           | Invalid          | Pass   | 0.000s   |
| TC_010 | Contains comma                                | AB,C          | Invalid           | Invalid          | Pass   | 0.000s   |
| TC_011 | First digit is 0                              | AB01          | Invalid           | Invalid          | Pass   | 0.000s   |
| TC_012 | Letters after digits                          | AB12C         | Invalid           | Invalid          | Pass   | 0.000s   |
| TC_013 | Mixed invalid chars                           | AB!12         | Invalid           | Invalid          | Pass   | 0.000s   |
| TC_014 | Single letter                                 | A             | Invalid           | Invalid          | Pass   | 0.000s   |
| TC_015 | All digits                                    | 123           | Invalid           | Invalid          | Pass   | 0.000s   |
| TC_016 | Special chars only                            | !@#           | Invalid           | Invalid          | Pass   | 0.000s   |

