# basicPython
This repository contains a basic python setup.

## Setup the development environment
* We use Pycharm community edition as an IDE (https://www.jetbrains.com/de-de/pycharm/download/#section=windows).
* Make sure to set the correct git username before committing to the repository:
For this, add the following lines to projectfolder/.git/config  
  [user]  
        name = myuser  
        email = mymail@xxx.com
* As package manager, we use pipenv. Install it via
'pip install pipenv' on the terminal.

## Coding conventions
### Naming
* We use the camel case notation in all situations:
    * class names start with a capital letter
    * all others starts with a lowercase letter

## Testing
* We use the python unittest package to write unittests. For every file, we create a new testing file. The filename, the testing class and all testcases have 'test' as name prefixes.




