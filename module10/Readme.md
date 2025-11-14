# Module 10 - Classes Live Session



Objects / Classes
- [x] What does it look like to add attributes after the original definition of the class? Lecture videos talked about coffee shots and car upgrades that changed the price, and I’m not clear on where the information behind those changes was stored/defined.
- [x] During our team activity discussion around the pro/cons of using the Movie class, optional attributes came up. Can you talk about best practices around optional attributes?
- [x] Command line / file locations


## Ideas / Brainstorm 
```
+---------------------------------------+
|             ListItem                  |
|-------------------------------------  |
| name : str                            |
| description : str (longer, optional?) |
| completed :  boolean                  |
+---------------------------------------+
| getter for name  : str                |
| setter for name  : none               |
| get/set description                   |
| toggle_status() : boolean (updated status?)
| __str__ : str                         |
+---------------------------------------+   |
```


```
+------------------------------+
| TaskList                     |
| ----------------------       |
| items : list[ListItem]       |
| name? : str                  |
+ ------------------------ --- +
| newList aka __init__         |
| removeTask(index) : ListItem |
| addTask(ListItem) :          |
| addItem(str, str, boolean)   |
| size : int                   |
|                              |
+------------------------------+
```

## Feature Ideas

1. Menu System - lets me do
   1. add items
   2. remove items? (less important)
   3. mark items completed
   4. save to a file
   5. open from a file
2. read from a file to load items
3. save to a file 
4. load a file from command line args
   1. help message from command line args
