from random import randint

names = ("Westley", "Buttercup", "Inigo Montoya", "Fezzik", "Miracle Max")

def get_name():
    return names[randint(0, len(names)-1)]


def build_copies(n:int ):
    lst = []
    for val in range(0, n):   
        if (val % 2) == 0:
            lst.append(get_name())
        else:
            lst.append(get_name()+"2")
    return lst


def get_mixed():
    return (["Vizzini", "Rugen", "Humperdinck"], names)
    

def build_complex_structure():
    lst = build_copies(3)
    mixed = get_mixed()
    lst.append(mixed)
    del mixed[0][0] # del removes an item from a list
    print(lst) 


if __name__ == "__main__":
    build_complex_structure()