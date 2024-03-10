#!/usr/bin/python3
"""the AirBnB console"""


import cmd

class HBNBCommand(cmd.Cmd):
    """
    Write a program called console.py that contains the entry point of the command interpreter:

    You must use the module cmd
    Your class definition must be: class HBNBCommand(cmd.Cmd):
    Your command interpreter should implement:
        quit and EOF to exit the program
        help (this action is provided by default by cmd but you should keep it updated and documented as you work through tasks)
        a custom prompt: (hbnb)
        an empty line + ENTER shouldn’t execute anything
    Your code should not be executed when imported
    """
    pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
