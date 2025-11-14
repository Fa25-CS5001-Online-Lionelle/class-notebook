import csv
from ListItem import ListItem 


class TaskList():
    """ Class for containing multiple task"""

    __items : list[ListItem] = []
    __name : str 

    def __init__(self, name):
        self.__name = name


    @property
    def name(self):
        return self.__name 

    def addItem(self, task : ListItem) -> None:
        if isinstance(task, ListItem):
            self.__items.append(task)
        else:
            raise TypeError("Can only add ListItem types")

    @property
    def size(self) -> int:
        return len(self.__items)
    
    def getListCopy(self) -> list[ListItem]:
        return self.__items.copy()
    
    def getItem(self, index: int) -> ListItem:
        ## check that index > 0
        return self.__items[index]



def loadListFromFile(filename : str, listname : str = "My Task List") -> TaskList:
    tList = TaskList(listname)
    with open(filename, "r") as f:
        csv_reader = csv.reader(f) # "line","item","completed" => ['line', 'item', 'completed']
        for row in csv_reader:
            if len(row) == 3:
                ## for project alright -> extra points if you don't assume correct - feature
                completed = False
                if row[2] == 'True':
                    completed = True
                item = ListItem(row[0], row[1], completed)
                tList.addItem(item)
            else:
                pass # ignore line, maybe print error about reading
    
    return tList

def saveToFile(filename: str, tList: TaskList) -> None:
    with open(filename, "w") as f:
        csv_writer = csv.writer(f)
        counter = 0 
        while counter < tList.size:
            item = tList.getItem(counter)
            csv_writer.writerow(item.asList())
            counter += 1


if __name__ == "__main__":
    item = ListItem("Item01")
    item2 = ListItem("Item02", "This has details")
    item3 = ListItem("Item03", "Details", True)

    list = TaskList("My List")
    list.addItem(item)
    list.addItem(item2)
    list.addItem(item3)

    print("DEBUG size of list", list.size)

    print(item, item2, item3, sep="\n")
    print(item.shortName)


