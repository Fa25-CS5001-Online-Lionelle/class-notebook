# Code Walk File
# 
from typing import List, Tuple
import string

# going to give two numbers, n - the amount to go to
# second number is divisble by

def get_divs_from_value(n: int, x: int) -> list:
    """
    Takes in a number `n` and returns a list of
    all numbers divisible by `x`.


    Examples:
    >>> get_divs_from_value(5,2)
    [2, 4]
    >>> get_divs_from_value(10,2)
    [2, 4, 6, 8]
    >>> get_divs_from_value(0, 10)
    []
    >>> get_divs_from_value(5, 10)
    []


    Args:
        n (int): number we want to work to from 0 exclusive of n
        x (int): number it must evenly divide into

    Returns:
        list: all numbers from 0 to n that are divisible by x
    """
    index = 1
    rtn = []
    while index < n:
        if index % x == 0:
            rtn.append(index)
        index += 1

    return rtn



def minimum_val(lst: list) -> int | None:
    """
    Return smallest value in list

    Examples:
    >>> minimum_val([3, 5, 15, 25])
    3
    >>> minimum_val([22, 250, 33, 5])
    5
    >>> minimum_val([])
    None


    Args:
        lst (list): list of numbers

    Returns:
        int: smallest value
    """
    if not lst: return None

    index = 1
    min_val = lst[0]
    while index < len(lst):
 #       if min_val == None:
 #           min_val = lst[index]
        if min_val > lst[index]:
            min_val  = lst[index]
        index += 1
    return min_val

def my_substring(value: str, start: int, end: int | None = None) -> str:
    if end is None: 
        end = len(value)
    i = start
    rtn = ""
    while i < end:
        rtn += value[i]
        i += 1

    return rtn


def is_vs_equal_equal(one: list, two: list) -> None:

    ee =  one == two
    print(f"Equal equal test: {ee}")

    is_test = one is two  
    print(f"Is test {is_test}")

def floating_point_errors(one: int, two: int, three: int) -> int:
    rtn = one * 0.299 + two * 0.587 + three * 0.114
    print(rtn)
    return int(round(rtn, 0))

def comparing_floating_point(one: int, two: int, three: int, expected: int) -> bool:
    actual = one * 0.299 + two * 0.587 + three * 0.114

    if abs(expected - actual) < 0.000000000001:
        return True 
    return False 

# you can use this list for something like the following
# if command in _FILTER_OPERATION_OPTIONS:  
#    do something
# else:
#    assume it is a movie title
__FILTER_OPERATION_OPTIONS = ['<', '>', '=', '<=', '>=', '!=']

def check_filter(movie: Tuple[str, int], filter: str) -> bool:
    """Checks if the movie title contains the filter.

    The filter can either be a string  (case insensitive) that will map to the title,
    or a filter operation and a number. The filter operation can be
    one of the following: <, >, =, <=, >=, !=. Which is meant to check
    the rating of the movie based on the number that follows. 

    if the empty string ("") is passed in, then the function will return True.

    Examples:
        >>> check_filter(("Princess Bride", 10), "Bride")
        True
        >>> check_filter(("Princess Bride", 10), "bride")
        True
        >>> check_filter(("Princess Bride", 10), "> 3")
        True
        >>> check_filter(("Princess Bride", 10), "< 3")
        False
        >>> check_filter(("Princess Bride", 10), "= 10")
        True
        >>> check_filter(("Princess Bride", 10), "= 11")
        False
        >>> check_filter(("Princess Bride", 10), "!= 10")
        False
        >>> check_filter(("Princess Bride", 10), "")
        True
        >>> check_filter(("", 0), "")
        True


    Args:
        movie (Tuple[str, int]): The movie tuple
        filter (str): The filter to check

    Returns:
        bool: True the movie meets the filter requirements.
    """
    if filter == "": return True 
    movie_title, rating = movie 
    operation, number = filter.split() # this will actually error, may need other code!
    if operation in __FILTER_OPERATION_OPTIONS:
        if operation == "<":
            # do something
            return False
        

    if filter.casefold() in movie_title.casefold():
        return True 
    return False

__SPACER = 2
__MAX_STARS = 5

def print_movies(movies: List[Tuple[str, int]], filter: str = '', spacer: int = __SPACER, max_stars: int = __MAX_STARS) -> None:
    """Prints out a list of movies.

    Prints out the movies to the console along with star ratings. 

    Will filter the movies before printing based on the filter 
    passed into the function. See: check_filter() for more details.

    Uses the string format
        f"{convert_rating(rating):<{max_stars + spacer}}{movie}"

    For grading purposes, print the movies in the order that they
    appear in the list, as you loop through the list (do not sort the list, do not concatenate the strings, etc)

    Args:
        movies (List[Tuple[str, int]]): The list of movies
        filter (str, optional): The filter to apply. Defaults to ''.
        spacer (int, optional): The number of spaces between the stars and the movie title. Defaults to __SPACER.
        max_stars (int, optional): The maximum number of stars to print, used for spacing purposes. Defaults to __MAX_STARS.
    """
    star_rating = "*****"
    movie = "Princess Bride"
    print(f"'{star_rating:<{max_stars + spacer}}'{movie}")


def main():
    #print(get_divs_from_value(5, 2))
    #print(get_divs_from_value(10, 2))
    #print(get_divs_from_value(0, 2))
    #print(get_divs_from_value(5, 10))
    #print(minimum_val([3, 5, 15, 25]))
    #print( minimum_val([22, 250, 33, 5]))
    #print(minimum_val([]))

    hello = "Aloha"
    print(hello[3:])
    print(hello[:2])
    print(my_substring(hello, 3, 5))
    print(my_substring(hello, 3))

    one = [1, 2, 3]
    two = [1, 2, 3]

    is_vs_equal_equal(one, two)

    print(floating_point_errors(127, 127, 127))
    print(comparing_floating_point(127, 127, 127, 127))

    print_movies([])

if __name__ == "__main__":
    main()

