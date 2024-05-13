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
    res = strng.capitilize(string)
    assert res == result

@pytest.mark.parametrize('string, result', [("  nothing", "nothing"), ("Nothing  ", "Nothing  ")])
def test_trim(string, result):
    res = strng.trim(string)
    assert res == result

@pytest.mark.parametrize('string, delimeter, result', [("a,b,c,d", None, ["a", "b", "c", "d"]),
                                                       ("1:2:3:4", ":",["1", "2", "3", "4"] ),
                                                       ("Cat dog Mouse rabbit", " ", ["Cat", "dog", "Mouse", "rabbit"]),
                                                       ("1a2a3a4", "a", ["1", "2", "3", "4"])])
def test_to_list(string, delimeter, result):
    if delimeter is None:
        res = strng.to_list(string)
    else:    
      res = strng.to_list(string, delimeter)
    assert res == result

@pytest.mark.parametrize('string, symbol, result', [("nothing", "h", True), 
                                                    ("Nothing", "N", True), 
                                                    ("Nothing", "k", False),
                                                    ("1 2 3  Nothing", "2", True),
                                                    ("Nothing & wrong?", "&", True),
                                                    ("Nothing nothing", " ", True ),
                                                    ("", "", True),
                                                    ("", " ", False)])
def test_contains(string, symbol, result):
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
    res = strng.delete_symbol(string, symbol)
    assert res == result

@pytest.mark.parametrize('string, symbol, result', [("Nothing", "N", True),
                                                    ("nothing", "n", True),
                                                    ("1234", "1", True),
                                                    ("Nothing", "o", False),
                                                    ("Nothing", "n", False),
                                                    (" nothing ", " ", True),
                                                    ("nothing", "", False)])
def test_starts_with(string, symbol, result):
    res = strng.starts_with(string, symbol)
    assert res == result

@pytest.mark.parametrize('string, symbol, result', [("nothing", "g", True),
                                                    ("nothinG", "G", True),
                                                    ("1234", "4", True),
                                                    ("nothing", "n", False),
                                                    ("nothing", "G", False),
                                                    ("nothing ", " ", True),
                                                    ("nothing ", "g", False),
                                                    ("noting!", "!", True),
                                                    ("nothing", "", False)])
def test_end_with(string, symbol, result):
    res = strng.end_with(string, symbol)
    assert res == result    
  
@pytest.mark.parametrize('string, result', [("notning", False),
                                            ("b", False),
                                            (" ", True),
                                            ("123", False),
                                            ("!", False),
                                            ("", True)])
def test_is_empty(string, result):
    res = strng.is_empty(string)
    assert res == result  

@pytest.mark.parametrize('lst, joiner, result', [([1,2,3,4,5,6], None, "1, 2, 3, 4, 5, 6"),
                                                 (["a","b","c","d"], ":", "a:b:c:d"),
                                                 (["cat", "Dog", "mouse", "Rabbit"], "! ", "cat! Dog! mouse! Rabbit"),
                                                 ([1,"a",2,"b"], "c ", "1c ac 2c b"),
                                                 ([1, 2, 3, 4], " ", "1 2 3 4")]) 
def test_list_to_string(lst, joiner, result,):
    if joiner is None:
      res = strng.list_to_string(lst) 
    else:
      res = strng.list_to_string(lst, joiner)
    assert res == result
   
