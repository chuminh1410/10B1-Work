def dictionaries_problem2(dict_to_use):
    """
    Given a dictionary, perform the following operations:
    1. Remove the key "Here".
    2. Add a key "There" with the value 10.
    3. If the key "Where" exists, update its value to 5.
    """
    dict_to_use.pop("Here")
    dict_to_use["There"] = 10
    if "Where" in dict_to_use:
        dict_to_use["Where"] = 5
    return dict_to_use


def test_dictionaries_problem2():
  assert dictionaries_problem2({'Here':5, 'Where': 9}) == {'There': 10, 'Where': 5}
  print("Test 2 completed with no errors. Well done!")
  
test_dictionaries_problem2()