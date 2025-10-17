


def splitAndConvert(filter: str) -> int:
    """"""
    _, val = filter.split() # splits on whitespace \w
    value = int(val)
    return value


def filter(nameCombo: tuple, filter: str) -> bool:
    """Filters names based on grades values.

    Can have:
    Name contains filter, if filter doesn't start with a operator

    Can have operators >, <, ==, >=

    > value
    < value
    == value
    >=

    operator value

    if filter is empty, just assumes true


    Args:
        namesCombo (tuple): (name, grade) tuple
        filter (str): the string to return true or false if it matches the filter

    Returns:
        bool: true if matches, false if not
    """
    if not filter: 
        return True

    name, grade = nameCombo

    if filter.startswith(">="):
        value = splitAndConvert(filter)
        return grade >= value    
    elif filter.startswith(">"):
        value = splitAndConvert(filter)
        return grade > value
    elif filter.startswith("<"):
        value = splitAndConvert(filter)
        return grade < value
    elif filter.startswith("=="):
        value = splitAndConvert(filter)
        return grade == value



    if(filter.casefold() in name.casefold()): 
        return True

    return False




def main():
    grades = (("Amy Pond", 4), ("Rory Williams", 2), ("River Song", 3), ("Clara Osborn", 1), ("The Doctor", 0))

    amy = grades[0]
    print(f"Filter(amy, '') returns {filter(amy, '')}")
    print(f"Filter(amy, 'amy') returns {filter(amy, 'amy')}")
    print(f"Filter(amy, '> 1') returns {filter(amy, '> 1')}")

    filter_in = input("How do you want to filter the grades? ")

    for person in grades:
        if filter(person, filter_in):
            print(person[0])


def my_append(lst, value) -> list:
    lst += [value]
    return lst

def main_old2():
    lst = [1, 2, 3]
    lst.append(10)
    print(lst)
    my_append(lst, 10)
    print(lst)

def main_old() :
    list1 = [[10, 20], 2]
    list2 = [3, 4]
    list3 = [5, 6]
    
    my_tuple = (list1.copy(), list2.copy(), list3.copy())
    my_tuple[0][1] *= 10 # yes, no?
    my_tuple[0][0][0] = 3
    print(my_tuple)
    
    print(list1)




if __name__ == "__main__":
    main()