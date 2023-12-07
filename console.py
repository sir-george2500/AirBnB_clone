#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter.
    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(alxbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def help_quit(self):
        """Help message for the quit command."""
        print("Quit command to exit the program.")

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
