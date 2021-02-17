#!/usr/bin/python3
"""Module contain HBNBCommand class to use the command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """[class HBNBCommand]"""
    prompt = '(hbnb) '

    def emptyline(self):
        """Print a new line"""
        return False

    def do_quit(self, arg):
        'Quit command to exit the program\n'
        return True

    def do_EOF(self, arg):
        'Quit command to exit the program\n'
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
