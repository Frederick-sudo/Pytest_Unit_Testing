Project: "Detection of Specific Word and/or Letter" 

Project Completion Date: October 20,2025

Project Test Date: October 20, 2025

Tools: Python 3.11, pytest 8.3, pytest-cov 

Goal: To validate the tip calculator function "value(greeting)" that bases the amount of the tip on the type of input received. 
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

| ID     | Scenario                                      | Input                   | Expected          | Actual           | Status | Duration |
|--------|-----------------------------------------------|-------------------------|-------------------|------------------|--------|----------|
| TC_001 | Hello all lowercase                           | hello                   | $0                | $0               | Pass   | 0.001s   |
| TC_002 | H first position all lowercase                | hiya                    | $20               | $20              | Pass   | 0.001s   |
| TC_003 | H not first all lowercase                     | whatsup                 | $100              | $100             | Pass   | 0.001s   |
| TC_004 | Hello mixed case                              | HellO                   | $0                | $0               | Pass   | 0.001s   |
| TC_005 | Hello all caps                                | HELLO                   | $0                | $0               | Pass   | 0.001s   |
| TC_006 | Hello with spaces                             | Hello how are you doing | $0                | $0               | Pass   | 0.002s   |
| TC_007 | H first mixed case                            | HiThere                 | $20               | $20              | Pass   | 0.001s   |
| TC_008 | H first all caps                              | HITHERE                 | $20               | $20              | Pass   | 0.001s   |
| TC_009 | H first with spaces                           | Hi There                | $20               | $20              | Pass   | 0.001s   |
| TC_010 | H not first mixed case                        | GoodMorNing             | $100              | $100             | Pass   | 0.001s   |
| TC_011 | H not first all caps                          | GOODMORNING             | $100              | $100             | Pass   | 0.001s   |
| TC_012 | H not first with spaces                       | Good Morning            | $100              | $100             | Pass   | 0.002s   |
| TC_013 | Empty string (raises exception)               | ""                      | IndexError        | IndexError       | Pass   | 0.000s   |
| TC_014 | All digits                                    | 12345                   | $100              | $100             | Pass   | 0.001s   |
| TC_015 | All special characters                        | .!?,()                  | $100              | $100             | Pass   | 0.001s   |
| TC_016 | Hello substring in middle                     | WhatsHelloMean          | $0                | $0               | Pass   | 0.001s   |

