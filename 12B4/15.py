def dictionaries_problem3():
  """
  Create and return a dictionary that contains all the letters of the alphabet
  with their values being their location in the alphabet. As a programmer you 
  should obviously start with 0. 

  Example: 
    d = {'A': 0, 'B': 2 ... 'Z': 25}

  Hint: Use the chr() and ord() functions to help you. 

  """
for i in range(ord("A"),ord("Z")):
    

  
def test_dictionary_problem3():
    assert dictionaries_problem3() == {'A': 0, 'C': 2, 'B': 1, 'E': 4, 'D': 3, 'G': 6, 'F': 5, 'I': 8, 'H': 7, 'K': 10, 'J': 9, 'M': 12, 'L': 11, 'O': 14, 'N': 13, 'Q': 16, 'P': 15, 'S': 18, 'R': 17, 'U': 20, 'T': 19, 'W': 22, 'V': 21, 'Y': 24, 'X': 23, 'Z': 25}
    print("Test 3 completed with no errors. Well done!")