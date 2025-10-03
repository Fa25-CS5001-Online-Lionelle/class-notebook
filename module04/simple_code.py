def add_numbers(a: int | float, b: int | float) -> int | float:
    """
    Adds two numbers together.
    
    Examples:
    >>> add_numbers(1, 2)
    3
    >>> add_numbers(5, 7)
    12
    >>> add_numbers(-1, 1)
    0
    >>> add_numbers(5, 7.0)
    12.0
    
    Parameters:
        a (int): First number
        b (int): Second number
    
    Returns:
        int: Sum of a and b
    """
    return a + b 

VOWELS = "AEIOU"
# example 1 - counting vowels
def count_vowels(text: str) -> int:
    """
    Counts the vowels in a string. Will
    count all vowels, including both upper
    and lowercase in a string, using the vowel
    `aeiou`. 


    Examples:
    >>> count_vowels("cat")
    1
    >>> count_vowels("a")
    1
    >>> count_vowels("Mississippi")
    4
    >>> count_vowels("Mc Donald's")
    2
    >>> count_vowels("crypt")
    0
    >>> count_vowels("pc")
    0
    >>> count_vowels("")
    0
    >>> count_vowels("aeiou")
    5
    >>> count_vowels("AEIOU")
    5
    >>> count_vowels("cAt")
    1
    >>> count_vowels("MIssissIppi")
    4


    Args:
        text (str): any valid string

    Returns:
        int: The number of vowels in a string.
    """
    counter = 0
    index = 0
    n = len(text)
    text = text.upper()
    while index < n: # condition
        if text[index] in VOWELS:
            counter += 1
        index += 1
    return counter

# example 2 - build a matrix in strings
# 0 1
# 1 0

# 0 1 1
# 1 0 1
# 1 1 0
 
def matrix_builder(number: int) -> str:
    r"""
    Takes in an number and builds a matrix
    with 0 on the diagonal an 1s on every other point.

    Diagonal is defined when index row matches
    col for 0s, then 1s for every other part. Returns
    a string with new lines, so visually a matrix.

    Examples:
    >>> matrix_builder(0)
    ''
    >>> matrix_builder(1)
    '0'
    >>> matrix_builder(2)
    '0 1\n1 0'
   
    Args:
        number (int): the dimension of the matrix, number x number

    Returns:
        str: a string based matrix with 0 along diagonal 
    """
    rtn = ""
    row = 0
    while row < number:
        col = 0
        while col < number:
            if row == col:
                rtn += "0"
            else:
                rtn += "1"
            if col < number - 1:
                rtn += " "
            col += 1
        if row < number - 1:
            rtn += "\n"
        row += 1
    return rtn