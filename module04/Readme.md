# ReadMe, Module 04 Live Session



- [x] How can we write our code so that it runs examples as tests the way the homework does (like when we're doing practice problems)? Or is that a whole later area -- (more advanced topic but will be happy to cover it)
- [x] "The most common mistake is not setting your user.name and user. email." from the Homework 4 Assignment details. Would you delve into this a little more?


## My additions

- [x] Explain the function mantra - and how that helps  
  (often people do it in the wrong order!)
- [x] Loop examples, debugging loops? any needed?
  - [x] Nested loop
  - [x] Count vowels in a string
- [x] Can you demonstrate git/github again (matches video)
  - [x] Big take-away - double check rendering in github when submit assignment.

## Nested Loop Debugging

| row | col | rtn | number |
| --- | --- | --- |  ----- |
|  0  |  0  |  "" |  3 (no change) |
|  0  |  1  | "0 "|  - |
|  0  |  2  | "0 1 " | - |
|  0  |  3 (false condition - inner loop) | "0 1 1" | - |  
|  1  |  0  | "0 1 1\n" | - |
....

## mantra for writing functions

* define
  * name 
  * parameters of function ("inputs/precondition")
    * types - important
  * returns (post-condition)
    * types
* document
  * docstring 
  * summary, start with one sentence, could be a paragraph.
  * examples - thinking of pre/post conditions
  * parameters (arguments)
  * returns - if any

## doctest


Doctest is actually a command line tool (like pycodestyle). So you can take any python file, but running it is slightly different due to how it is setup. Instead you need to do the following

```bash
> python -m doctest filename.py
```

You may also want to add the verbose argument 

```bash
> python -m doctest -v filename.py
```

> [!CAUTION]
> Remember, Macos and linux use `python3`, not python

## Common Mistake

![alt text](image.png)

If you get this error generated, you want to run from the command line

```bash
> git config --global user.name "Your Name"
> git config --global user.email "Your Email"
```

Git requires changes (commits) to be "signed" by the person doing it. These are used for that signing. After you set them once, you don't have to set them again. So if you get the above error, run those commands in your terminal, then try committing and pushing to github again. 