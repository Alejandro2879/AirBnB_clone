#!/usr/bin/python3
"""Module contain HBNBCommand class to use the command interpreter"""
import cmd
from models.base_model import BaseModel


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

    def do_create(self, nameins):
        """ Create a new instance """
        nameClas = [
            "BaseModel"
        ]
        if len(nameins) == 0:
            print("** class name missing **")
            return
        for name in nameClas:
            if name != nameins:
                print("** class doesn't exist **")
                return
        new_instance = BaseModel()
        print(new_instance.id)
        return
        


if __name__ == '__main__':
    HBNBCommand().cmdloop()
