#!/usr/bin/python3
"""
This module contains the methods for the console.
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """This class defines the console commands.
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Exit the console.
        """
        return True

    def do_EOF(self, arg):
        """Exit the console when pressing Ctrl+D or typing "EOF".
        """
        print()
        return True

    # Help updates: (end all of them with a new line)
    def help_quit(self):
        """Help for quit command.
        """
        print("Quit command to exit the program")
        print()

    def help_EOF(self):
        """Help for EOF.
        """
        print("Press Ctrl+'D' to exit the program")
        print()

    # Miscellaneous code:
    def emptyline(self):
        """What it does with enters and empty lines.
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
