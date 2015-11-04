# Python common Utilities

This repository houses generic functionality that is often used in many types of projects but is not included in the standard libraries of programming languages.


## Contributing to the project

#### SETUP:
###### Install python modules (__[link](https://docs.python.org/2/install/)__):
- run python setup.py install inside the project root to install required modules
     
###### Setup the unittests environment:
- make a test.config file inside the /test directory
    - copy the contents from the example.config
    - check/modify the email, database and other settings

###### Ignore files from version control:
- add the /test/test.config file to the version control ignored list
- ignore all test.log files for version control


## Development environment and used technologies

Python 2.7.10 is currently supported

The project was developed using [PyCharm Community Edition 4.5.4 IDE](https://www.jetbrains.com/pycharm/)

