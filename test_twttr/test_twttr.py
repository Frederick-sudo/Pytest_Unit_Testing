import pytest
from twttr import shorten


#__________________________________________________________________________
#Normal Case Testing

def test_with_spaces():
    assert shorten("What is up") == "Wht s p"

def test_with_spec_char():
    assert shorten("Hey, nice to meet ya!") == "Hy, nc t mt y!"

def test_with_no_vowel():
    assert shorten("Rhythm") == "Rhythm"

def test_with_all_lower():
    assert shorten("apple") == "ppl"

def test_with_all_caps():
    assert shorten("BANANA") == "BNN"


#__________________________________________________________________________
#Mixed Case Testing

def test_num_check():
    assert shorten("ThisisCS50") == "ThssCS50"

def test_caps_print_test():
    assert shorten("POTTER") == "PTTR"

def test_punct_check():
    assert shorten("Hello!") == "Hll!"


#__________________________________________________________________________
#Edge Case Testing

def test_empty_string():
    assert shorten("") == ""

def test_one_char_consonant_lower():
    assert shorten("b") == "b"

def test_one_char_consonant_caps():
    assert shorten("G") == "G"

def test_one_char_vowel_lower():
    assert shorten("a") == ""

def test_one_char_vowel_caps():
    assert shorten("U") == ""

def test_all_vowel_lower():
    assert shorten("aueioau") == ""

def test_all_vowel_caps():
    assert shorten("AIEUOIUEO") == ""

def test_all_vowel_mixed():
    assert shorten("aEioeAUOeiAOIUIEO") == ""

def test_all_number():
    assert shorten("12345678") == "12345678"

def test_all_symbol():
    assert shorten("!@#!&*()") == "!@#!&*()"
