# example of a simple "data class"




class ListItem:
    """_summary_
    """
    __shortName : str
    __details : str 
    __completed : bool 

    def __init__(self, shortName: str, details: str = '', completed: bool = False):
        """_summary_

        Args:
            shortName (_type_): _description_
            details (str, optional): _description_. Defaults to ''.
            completed (bool, optional): _description_. Defaults to False.
        """
        self.shortName = shortName
        self.details = details
        self.__completed = completed
        
    @property
    def shortName(self):
        return self.__shortName

    @shortName.setter  
    def shortName(self, value : str):
        if not value:
            raise TypeError("Must have a value for shortName")
        self.__shortName = value


    def toggle_status(self) -> bool:
        self.__completed = not self.__completed
        return self.__completed 

    def __repl__(self) -> str: 
        """

        Returns:
            str: _description_
        """
        return self.__str__() 
    

    @property
    def details(self):
        return self.__details 
    

    @details.setter 
    def details(self, value : str):
        ## make sure value is str
        self.__details = value

    def __str__(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """
        return f"{self.shortName:<10} | {self.details:<30} | {'x' if self.__completed else 'o'}"
    
    def asList(self) -> list:
        return [self.shortName, self.details, self.__completed]

    
if __name__ == "__main__":
    item = ListItem("Item01")
    item2 = ListItem("Item02", "This has details")
    item3 = ListItem("Item03", "Details", True)

    print(item, item2, item3, sep="\n")
    print(item.shortName)
    
