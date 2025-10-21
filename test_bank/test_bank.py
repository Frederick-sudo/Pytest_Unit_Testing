import pytest
from bank import value


#__________________________________________________________________________
#Normal Case Testing

def test_hello_all_lower():
    assert value("hello") == "$0"

def test_h_first_all_lower():
    assert value("hiya") == "$20"

def test_h_notfirst_all_lower():
    assert value("whatsup") == "$100"


#__________________________________________________________________________
#Mixed Case Testing

def test_hello_mixed():
    assert value("HellO") == "$0"

def test_hello_caps():
    assert value("HELLO") == "$0"

def test_hello_with_space():
    assert value("Hello how are you doing") == "$0"

def test_h_first_mixed():
    assert value("HiThere") == "$20"

def test_h_first_caps():
    assert value("HITHERE") == "$20"

def test_h_first_with_space():
    assert value("Hi There") == "$20"

def test_h_notfirst_mixed():
    assert value("GoodMorNing") == "$100"

def test_h_notfirst_caps():
    assert value("GOODMORNING") == "$100"

def test_h_notfirst_mixed():
    assert value("Good Morning") == "$100"

#__________________________________________________________________________
#Edge Case Testing

def test_empty_string():
    with pytest.raises(IndexError):
        value("")

def test_all_digit():
    assert value("12345") == "$100"

def test_all_spec_char():
    assert value(".!?,()") == "$100"

def test_hello_inbetween():
    assert value("WhatsHelloMean") == "$0"


