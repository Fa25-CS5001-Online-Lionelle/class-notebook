# This example shows both standard recursion 
# and tail recursion

## BAD USE of RECURSION 

# def func(something):
    # basecase
    # func(something-1) + func(something-2) + func(something-3)

# 1 = 1
# 2 = 4
# 3 = 7
# 4 = 10



# reverse a string

def reverse_str(word: str) -> str:
    """
    Examples:
    >>> reverse_str("hello")
    'olleh'
    >>> reverse_str("")
    ''
    >>> reverse_str("olleh")
    'hello'
    """
    if not word:
        return ''
    ## last letter would be:  word[len(word) - 1]
    return word[-1] + reverse_str(word[0:-1]) 

def reverse_str_2(word: str) -> str: 

    if not word:
        return ''
    
    rest = word[0:-1]
    reversed = word[-1] + reverse_str_2(rest)
    return reversed

def reverse_str_3(word: str) -> str: 
    """Make it lowercase and alpha only"""
    if not word:
        return ''
    
    last = word[-1]
    if last.isalpha():
        last = last.casefold() 
        return last + reverse_str_3(word[0:-1])
    else:
        return reverse_str_3(word[0:-1])

#word[1:-1]
# return word[0] == word[-1]  and recursive_call(word[1:-1])

## more advanced --- but useful to know

## tail recursion - keeps track of the state, as a param

def reverse_str_tail(word, acc=""):
    if not word:
        return acc  
    return reverse_str_tail(word[1:], word[0] + acc)

# "hello", '' -> ello, h
# ello, h -> llo, eh
# llo, eh -> lo, leh
# lo, leh -> o, lleh
# o, lleh -> '', olleh 
# '', olleh -> ''


# flatten a list
def flatten_tail(nested_list, acc=None):
    if acc is None:
        acc = []

    if not nested_list:
        return acc

    first = nested_list[0]
    rest = nested_list[1:]

    if isinstance(first, list) or isinstance(first, tuple):
        return flatten_tail(first + rest, acc)
    else:
        return flatten_tail(rest, acc + [first])


def main():
    print(f"hello should be {reverse_str('olleh')}")
    print(f"testing for True does hello == reverse_str('olleh'):", "hello" == reverse_str('olleh'))


if __name__ == "__main__":
    main()
