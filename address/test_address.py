from address import extract_city, extract_state, extract_zipcode
import pytest


def test_extract_city():
    assert extract_city("525 S Center St, Rexburg, ID 83460") == "Rexburg"
    assert extract_city("123 Main St, Anytown, NY 12345") == "Anytown"
    assert extract_city(",   ,") == ""
    assert extract_city("239429385720 E 8th North, Salt Lake City, UT 23472897021934871023") == "Salt Lake City"
    assert extract_city(",              Ottowa                ,") == "Ottowa"

    return



# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])