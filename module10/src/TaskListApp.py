import sys 

from TaskList import loadListFromFile, saveToFile, TaskList

def main(args : list):
    # assume file name is being passed to me
    tlist = loadListFromFile(args[1])
    for i, index in enumerate(range(0, tlist.size)):
        print(f"{i+1}: {tlist.getItem(index)}")  
    
    for i in range(0, len(args)):
        print(i, args[i])
    




if __name__ == "__main__":
    main(sys.argv)