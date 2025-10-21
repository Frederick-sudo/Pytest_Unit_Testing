import pytest
from plates import is_valid


#__________________________________________________________________________
#Normal Case Testing

def test_with_char_and_digit():
    assert is_valid("TY20") == True

def test_char_only_caps():
    assert is_valid("CABLE") == True

def test_char_only_lower():
    assert is_valid("cable") == True

def test_min_input_caps():
    assert is_valid("OP") == True

def test_min_input_lower():
    assert is_valid("op") == True

def test_max_input_caps():
    assert is_valid("INYTWO") == True

def test_max_input_char_lower():
    assert is_valid("inytwo") == True

def test_input_one_digit():
    assert is_valid("Gold2") == True


#__________________________________________________________________________
#Mixed Case Testing

def test_char_only_mixed():
    assert is_valid("CaBlE") == True

def test_min_input_mixed():
    assert is_valid("oP") == True

def test_max_input_char_mixed():
    assert is_valid("inYTWo") == True

def test_max_input_mixed():
    assert is_valid("TwIc33") == True


#__________________________________________________________________________
#Edge Case Testing

def test_one_char():
    assert is_valid("A") == False

def test_seven_char():
    assert is_valid("AUWIN20") == False

def test_no_char():
    assert is_valid("") == False

def test_all_punct():
    assert is_valid(".,?") == False

def test_with_punct():
    assert is_valid("Hi,!") == False

def test_with_space():
    assert is_valid("Hey Hi") == False

def test_digit_only():
    assert is_valid("21735") == False

def test_digit_at_start():
    assert is_valid("22Be") == False

def test_digit_between_char():
    assert is_valid("T1tle") == False

def test_first_digit_zero():
    assert is_valid("Vr0") == False
