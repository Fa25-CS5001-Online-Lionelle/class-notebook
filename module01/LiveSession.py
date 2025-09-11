""" 
Code that will be used for the live session
"""
import random

def print_stars(num_stars: int) -> None:
    """ longer doc string """
    print('*' * num_stars)

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

def mod_tests():
    """ examples for mod"""
    n = random.randint(0, 1000)
    print(n)
    print(n % 6)


def run():
    ## print n..3 number of stars, in order from n on down
    # printing
    # cycling through numbers
    # stars / strings
    print(get_stars(5))
    print(get_stars(4))
    print(get_stars(3))
    #print_stars(20)
    #print_stars(4)
    #print_stars(3)
    num = get_star_number()
    stars = get_stars(num)
    print(f"The number of stars is {num} and stars: " + stars)


if __name__ == "__main__":
    run()

