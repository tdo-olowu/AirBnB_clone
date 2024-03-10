#!/usr/bin/python3
"""the AirBnB console"""


import cmd


class HBNBCommand(cmd.Cmd):
    """
    Your code should not be executed when imported
    """
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """what to do when EOF is met"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
           and prints the id. Ex: $ create BaseModel
        """
        pass

    def do_show(self, line):
        """Prints the string representation of an instance
        """
        pass

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        """
        pass

    def do_all(self, line):
        """Prints all string representation of all instances
        """
        pass

    def do_update(self, line):
        """Updates an instance based on the class name and id
        """
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
