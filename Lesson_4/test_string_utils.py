import pytest
from string_utils import StringUtils
strng = StringUtils()

@pytest.mark.parametrize('string, result', [("nothing", "Nothing"), 
                                            ("Nothing", "Nothing"), 
                                            ("", ""), 
                                            (" ", " "), 
                                            ("123", "123"), 
                                            ("nothing 123 Nothing", "Nothing 123 Nothing")])
def test_capitilize(string, result):
    strng = StringUtils()
    res = strng.capitilize(string)
    assert res == result

@pytest.mark.parametrize('string, result', [("  nothing", "nothing"), ("Nothing  ", "Nothing  ")])
def test_trim(string, result):
    strng = StringUtils()
    res = strng.trim(string)
    assert res == result

#@pytest.mark.parametrize('string, result, delimeter = ","', [("a,b,c,d", ["a", "b", "c", "d"], None)])
#def test_to_list(string, result, delimeter = ","):
   # strng = StringUtils()
  #  res = strng.trim(string, delimeter)
   # assert res == result

@pytest.mark.parametrize('string, symbol, result', [("nothing", "h", True), 
                                                    ("Nothing", "N", True), 
                                                    ("Nothing", "k", False),
                                                    ("1 2 3  Nothing", "2", True),
                                                    ("Nothing & wrong?", "&", True),
                                                    ("Nothing nothing", " ", True ),
                                                    ("", "", True),
                                                    ("", " ", False)])
def test_contains(string, symbol, result):
    strng = StringUtils()
    res = strng.contains(string, symbol)
    assert res == result

@pytest.mark.parametrize('string, symbol, result', [("nothing", "t", "nohing"),
                                                    ("nothing", "n", "othig"),
                                                    ("Nothing", "n", "Nothig"),
                                                    ("Nothing", "thi", "Nong"),
                                                    ("Nothing wrong", " ", "Nothingwrong"),
                                                    ("Nothing wrong", "", "Nothing wrong"),
                                                    ("Nothing? Wrong!", "?", "Nothing Wrong!"),
                                                    ("No 123 thing", "2", "No 13 thing"),
                                                    ("No 123 thing", " 1", "No23 thing")])
def test_delete_symbol(string, symbol, result):
    strng = StringUtils()
    res = strng.delete_symbol(string, symbol)
    assert res == result