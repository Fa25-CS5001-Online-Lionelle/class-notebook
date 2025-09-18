""" 
Sample file to test what happens with loading files and main
"""

# This is from Live Session 01 ../module01/LiveSession.py
# build the string first 
def get_stars(num_stars: int) -> str:
    """Takes in `num_stars` and returns a string
    of length `num_stars` with only `*`

    Examples:
        >>> get_stars(5)
        '*****'
        >>> get_stars(0)
        ''
        >>> get_stars(1)
        '*'

    Args:
        num_stars (int): length of stars to return

    Returns:
        str: string of only stars of length num_stars
    """
    return '*' * num_stars

# print stars, 

def get_star_number() -> int:
    """ """
    number = input("How many stars to you want: ")
    num = int(number)
    return num


def main():
    print("In `main_test.py`")
    num = get_star_number()
    stars = get_stars(num)
    print(stars)
    print("Thank you!\n")

if __name__ == "__main__":
    print("I am in the main if block check for a file")
    main()  ## we see it a lot