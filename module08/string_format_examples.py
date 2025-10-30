# some examples for string format


RGB_FORMATTER = """{{"red": {}, "green": {}, "blue": {}}}"""

def json_format(rgb: tuple) -> str: 
    """
    takes in a tuple of rgb values, returns
    a string of 
    {"red:", red_value, "green:", green_value, "blue:", blue_value}

        {"lines": 1, "words": 2, "vowels": 3, "palindromes": 4, "sentence_palindromes": 5}
    Args:
        values (tuple): _description_

    Returns:
        str: _description_
    """
    return RGB_FORMATTER.format(*rgb)

def format_string(rgb: tuple) -> str:
    """
    Passes in a tuple of three values, and returns (r,g,b) as the
    string with r = values[0], g = values[1], b = values[2]

    Args:
        rgb (tuple): triplet of three values, between 0-255 for each value

    Returns:
        str: String (r,g,b) with r,g,b matching their value
    """
    r, g, b = rgb # takes my 3 value tuple, and stores it as r, g, b respectively
    return f"({r},{g},{b})"



def main():
    print(format_string((25, 0, 10)))
    print(format_string((255, 255, 255)))
    print(format_string((0, 0, 0)))

    print(json_format((25, 0, 10)))
    print(json_format((255, 255, 255)))
    print(json_format((0, 0, 0)))


if __name__ == "__main__":
    main()