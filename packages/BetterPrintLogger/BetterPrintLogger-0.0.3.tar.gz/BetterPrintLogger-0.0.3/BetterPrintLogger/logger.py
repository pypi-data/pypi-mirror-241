"""
Logging oriented print statements

v 0.0.1

*****************************************
IMPORT
*****************************************

import logger as log

*****************************************
FUNCTIONS:
*****************************************

log.title(input:str)
    print input as it is with *'s above and below 

log.info(input:str):
    print input preceeded by "[ INFO ]"

log.error(input:str):
    print input preceeded by "[ ERROR ]"

log.warning(input:str):
    print input preceeded by "[ WARNING ]"

"""


TITLE_PADDING = 30
WARNING = "[ WARNING ]"
ERROR = "[ ERROR   ]"
INFO = "[ INFO    ]"

def title(input:str):
    print("*"*(TITLE_PADDING + len(input)))
    print(" "*15+input+" "*15)
    print("*"*(TITLE_PADDING + len(input)))

def info(input:str):
    print(f"{INFO}  {input}")

def error(input:str):
    print(f"{ERROR}  {input}")

def warning(input:str):
    print(f"{WARNING}  {input}")


