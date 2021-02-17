#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    intro = 'Welcome to the hbnb shell.   Type help or ? to list commands.\n'
    prompt = '(hbnb) '

    def do_quit(self, arg):
        'Quit command to exit the program'
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
