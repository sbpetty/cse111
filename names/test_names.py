from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest


def test_make_full_name():
    assert make_full_name("John", "Doe") == "Doe; John"
    assert make_full_name("Rikki tikki tembo no sorembo", "Chari bari ruchi pip peri pembo") == "Chari bari ruchi pip peri pembo; Rikki tikki tembo no sorembo"
    assert make_full_name("a", "z") == "z; a"
    assert make_full_name("42", "68") == "68; 42"
    assert make_full_name("Mary-Jane", "Parker-Smith") == "Parker-Smith; Mary-Jane"
    assert make_full_name("", "") == "; "

    return


def test_extract_family_name():
    assert extract_family_name("Doe; John") == "Doe"
    assert extract_family_name("Chari bari ruchi pip peri pembo; Rikki tikki tembo no sorembo") == "Chari bari ruchi pip peri pembo"
    assert extract_family_name("z; a") == "z"
    assert extract_family_name("68; 42") == "68"
    assert extract_family_name("Parker-Smith; Mary-Jane") == "Parker-Smith"
    assert extract_family_name("; ") == ""

    return


def test_extract_given_name():
    assert extract_given_name("Doe; John") == "John"
    assert extract_given_name("Chari bari ruchi pip peri pembo; Rikki tikki tembo no sorembo") == "Rikki tikki tembo no sorembo"
    assert extract_given_name("z; a") == "a"
    assert extract_given_name("68; 42") == "42"
    assert extract_given_name("Parker-Smith; Mary-Jane") == "Mary-Jane"
    assert extract_given_name("; ") == ""

    return


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
