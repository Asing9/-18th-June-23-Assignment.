'''1. What is the role of the 'else' block in a try-except statement? Provide an example
scenario where it would be useful.

a=int(input('Enter first no:'))
b=int(input('Enter second no:'))
try:
    div=a/b
    print(div)
except ZeroDivisionError:
    print('Divide by zero not possible')
else:
    print('Exception not occur')


2. Can a try-except block be nested inside another try-except block? Explain with an
example.


3. How can you create a custom exception class in Python? Provide an example that
demonstrates its usage.


class InvalidAgeError(Exception):
    def __init__(self,value):
        self.value = value

try:
    age=int(input('how old are you : '))
    if age<0 or age>120:
        raise InvalidAgeError('age not valid')
    print(f'You are {age} years old')
except ValueError:
    print('invalid int was entered')
except InvalidAgeError as iae:
    print(iae)

4. What are some common exceptions that are built-in to Python?

ZeroDivisionError
SyntaxError
ValueError
TypeError
ArithmeticError
NameError
Exception

5. What is logging in Python, and why is it important in software development?

logging means tracaking when software run. it is important for debugging, testing

6. Explain the purpose of log levels in Python logging and provide examples of when
each log level would be appropriate.

debug : useful for debugging purpose
info: provider info things are working as we want
warnings:warn something happenned unexpectedly
error:inform when program in some trouble
critical: inform when progra in serious trouble

7. What are log formatters in Python logging, and how can you customise the log
message format using formatters?

logging.basicConfig(filename='app.log',
                    level=10,
                    filemode='w',
                    format="%(asctime)s:%(name)s:%(levelname)s:%(message)s:%(process)s:%(lineno)s",
                    datefmt='%d-%b-%y %H:%M:%S')

8. How can you set up logging to capture log messages from multiple modules or
classes in a Python application?


9. What is the difference between the logging and print statements in Python? When
should you use logging over print statements in a real-world application?

logging is use for create a record in systems log table, while print does not,

10. Write a Python program that logs a message to a file named "app.log" with the
following requirements:
● The log message should be "Hello, World!"
● The log level should be set to "INFO."
● The log file should append new log entries without overwriting previous ones.


import logging

logging.basicConfig(filename='app.log', level=logging.INFO)

logging.info("hello world")

11. Create a Python program that logs an error message to the console and a file named
"errors.log" if an exception occurs during the program's execution. The error
message should include the exception type and a timestamp.


import logging

logging.basicConfig(filename='error.log',level=logging.INFO,format="%(asctime)s:%(name)s:%(message)s",)

class Type1Error(Exception):
    pass

try:
    ag= int(input("age should be greater than 18 :"))
    if ag<18:

        raise Type1Error("not allowed")
    logging.info(" a user login ")
except Exception as obj:

    logging.exception("not allowed")

'''