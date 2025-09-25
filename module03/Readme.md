# Module 03 - Live Help Session

## Topics


- [ ] Would you discuss in detail how we should be thinking about edge cases as they relate to the distance colors group activity earlier in the week?
- [ ] How to check for a string vs an int to avoid edge cases where numbers are entered instead of characters. (Example: accepting input for employee_name in PyNative - (Exercise 4) Create a function with a default argument - [Practice Problem]
- [ ] return formats / type hints 
  - [ ] Advanced: mypy example
- [ ] avoiding magic numbers for constants that seem super obvious - is it ever overkill or should we always do it? 
- [ ] Common helper methods (ex: Bigger) and where to find them

- [ ] If there's time could you demo the PyCodeStyle features a little further.
- [ ] If there's time, please show an example in Python Tutor Visualize Code


## Edge Cases

### String vs int checking??

## return formats / type hints




## pycodestyle

A tool you can use to double check style before submitting.

### Install

To install you will want to run on windows

```bash
pip install pycodestyle
```

on linux / macOs

```bash
pip3 install pycodestyle
```

### Usage

```bash
pycodestyle filename.py
```

However, there are a number of options that we ignore in our autograder. They are:

* 'E121', # Continuation line under-indented for hanging indent
* 'E126', # Continuation line over-indented for hanging indent
* 'W291', # Trailing whitespace 
* 'W503', # Line break before binary operator
* 'W504', # Line break after binary operator
* 'E501' # Relaxing the line length due to comments commonly going over 80


so if you want to match the autograder exactly, you should try

```bash
pycodestyle --ignore=E501,W504,W503,W291,E126,E121  filename.py
```

Note that we may not be using the "exact" same ignore list for all the assignments. It has migrated a bit over the semesters. 

#### Autoformatters (advanced)
There are also many auto formatters out there you can install as a vs code extension, such as black formatter. They can be useful, but sometimes aggressive - so you will want to double check all the changes made.  A common one is that it may move a doctest to a new line, which will then cause the doctest to fail.

Example:

```python
>>> recommend_adjustment(2.0, 7.0)
   'Significant contrast improvement needed - consider much darker or lighter colors'
```

may get an auto formatter to put in a line return. That will make the doctest assume the line return is required. You either have to manually fix it each time, or add the following to the doctest. 


```python
>>> recommend_adjustment(2.0, 7.0)  # doctest: +NORMALIZE_WHITESPACE
   'Significant contrast improvement needed - consider much darker or lighter colors'
```

That will allow new lines in the string, but the doctest will assume all spaces/new lines are a single space.  Reminder: look at the raw markdown - the html rendering of the page could be adding what looks to be spaces. 


## Type Checking (Advanced)

Type hints are optional, but it is a industry standard practice. Often in industry, a number of tools are ran on the code to confirm validity and a "type checker" is one of them. For python, the most common one is `mypy`. 

### install

To install, you will need to use `pip` again

```bash
pip install mypy
```

or on linux/macos

```bash
pip3 install mypy
```

### Testing

To test a file (or files), it is

```bash
mypy filename.py file2.py
```

it is also common to add the strict option

```bash
mypy --strict filename.py
```

It is important to note, if your main doesn't have `-> None` on it, it will actually skip that function, and any function called from it. Unless you enable `--strict` or `--check-untyped-defs`

With all the said, having `pylance` setup in vs code, it will type check for you.  This is all in the name of finding errors *before* you run your code!
