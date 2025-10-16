# Module 06 Live Session Notes


## Mutability / Immutability 
- [ ] Would you review the final diagraming exercise provided in the group activity just to clarify content.
  - [ ] Also the diagram for the weekly challenge - `my_tuple = ([1, 2], [3, 4], [5, 6])`


## Objects, functions, python confusion - oh my!
- [ ] I am confused about when to use method after a dot and when to use method before brackets. For example, len() vs. .append(). I read that one is a built-in tool while the other can be used only with objects, but is there a better way to remember this? I was thinking dot is used to modify objects while the (former) is used to find specific details about the objects, like len(), min(), max(), etc. Is this the right way to think of this?
    * Actually `val.method` .. like `.append()` is when the information is focused on that exact object - often modifying, but can also just means it needs that exact object to work. 
    * **Functions** like `len()`, `min()`, `max()` - work on any object of a certain structure (sequence in those cases)  
      Mainly for ease of use, not all languages uses that - but part of the confusion.  
      These are more like the functions you write 

- [ ] I am also a little confused about the methods syntax. This example in particular: operation, number = filter. split() . How do we know when "operation" will be treated as a variable and get assigned a value?
  * This is actually a returns question - will cover that more
  
