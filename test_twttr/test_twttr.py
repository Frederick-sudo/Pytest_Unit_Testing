import pytest
from twttr import shorten


#__________________________________________________________________________
#Normal Case Testing

def test_with_spaces():
    assert shorten("What is up") == "Wht s p"

def test_with_spec_char():
    assert shorten("Hey, nice to meet ya!") == "Hy, nc t mt y!"

#Test to see if function works without any vowels to replace.
def test_with_no_vowel():
    assert shorten("Rhythm") == "Rhythm"

#Test to see if function works without any uppercase vowels to replace.
def test_with_all_lower():
    assert shorten("apple") == "ppl"

#Test to see if function works without any lowercase vowels to replace.
def test_with_all_caps():
    assert shorten("BANANA") == "BNN"


#__________________________________________________________________________
#Mixed Case Testing

#Make sure function does not remove numbers, since they are not vowels
def test_num_check():
    assert shorten("ThisisCS50") == "ThssCS50"


#Test to see if function works as intended with all uppercase letters.
def test_caps_print_test():
    assert shorten("POTTER") == "PTTR"


#:| test twttr.py omitting punctuation
def test_punct_check():
    assert shorten("Hello!") == "Hll!"


#__________________________________________________________________________
#Edge Case Testing

def test_empty_string():
    assert shorten("") == ""

def test_one_char_consonant():
    assert shorten("b") == "b"
    assert shorten("G") == "G"

def test_one_char_vowel():
    assert shorten("a") == ""
    assert shorten("U") == ""

def test_all_vowel_lower():
    assert shorten("aueioau") == ""

def test_all_vowel_caps():
    assert shorten("AIEUOIUEO") == ""

def test_all_vowel_mixed():
    assert shorten("aEioeAUOeiAOIUIEO") == ""

def test_all_number():
    assert shorten("12345678") == "12345678"
    assert shorten("231748501") == "231748501"

def test_all_symbol():
    assert shorten("!@#!&*()") == "!@#!&*()"
