# Module 07 Live Session



## General Recursion

- [x] I'm getting, just through trial and error, that the way to make recursion work for many of the homework problems is to put the recursive call in the return statement. Can you talk about why this is the case? 


## Testing
- [x] How to write an example/doctest when an error is the expected result?  
  - short answer - you don't, that is what unit testing is for, like your tests file


## Others
- [x] While there are man-pages in bash, is there an equivalent manual documentation system for built-in python functions?  
  - `help(func)` function! from homework 01 🙂 
  - example: `help(print)`
  - example: `help(str.isalnum)`  
  - However, the online documentation is often more detailed with better examples



## Homework 07 Questions



- [x] For the recursive functions in word_lib.py, should all iterations be handled strictly through recursion, or can loops be used when recursion isn’t practical? 
  - Everything in word_lib.py is recursion - yes, all can be done with loops, but that is intentional with this assignment.. in the doc stats builder, those are all loops, intentionally
- [x] When testing our recursive functions, do you expect us to include print statements for debugging, or should our final submission only contain the completed function definitions and doctests?  
  - Question about "evidence of testing"


