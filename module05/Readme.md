# Module 05 - Live Session


## Posted Questions

### General 
- [ ] Code walks - overview
- [ ] What is a "substring" ?


- [ ] Would you discuss built-in Python modules.
- [ ] Dealing with floating point errors (calc-brightness truncate), and rounding errors


### Homework 05
- [ ] Would you generally discuss check_filter() and how you want us to think about:
  - [ ] "# if command in _FILTER_OPERATION_OPTIONS: "
- [ ] There are already 8 docstring tests for check_filter(), do you want us to come up with more tests?



## Python Built-ins

Language definitions and rules are often small, but modern languages often have 'builtin' libraries that help expand the language. A string is a great example, it is actually a collection of characters in a set order but we just string them as "strings". 

Python has *a lot* well beyond the scope of this class. You often learn about them by searching references:

* [https://docs.python.org/3/library/index.html](https://docs.python.org/3/library/index.html)

A strength of python is the use of modules, so if want to use the String module, i would do the following


```python

import string ## imports the module

print(string.capwords("Isn't this fun?"))
```


Note: if the specification system built in - you don't have to import, but most of the standard library you still need to import!  


## Homework 05

```python
# you can use this list for something like the following
# if command in _FILTER_OPERATION_OPTIONS:  
#    do something
# else:
#    assume it is a movie title
__FILTER_OPERATION_OPTIONS = ['<', '>', '=', '<=', '>=', '!=']
```

