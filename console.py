#!/usr/bin/python3
"""Module contain HBNBCommand class to use the command interpreter"""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """[class HBNBCommand]"""
    prompt = '(hbnb) '

    valid_class = {'BaseModel': BaseModel}

    def emptyline(self):
        """Print a new line"""
        return False

    def do_quit(self, arg):
        'Quit command to exit the program\n'
        return True

    def do_EOF(self, arg):
        'Quit command to exit the program\n'
        return True

    def do_create(self, args):
        len_args = len(args)
        if len_args < 1:
            print("** class name missing **")
        else:
            if args[0] in HBNBCommand.valid_class.keys():
                if len_args == 1:
                    new_object = HBNBCommand.valid_class[args[0]]()
                else:
                    result = self.create_aux(args[1:])
                    if result is None:
                        print("** Object fails **")
                        return
                    new_object = HBNBCommand.valid_class[args[0]](**result)
                print(new_object.id)
                new_object.save()
            else:
                print("** class doesn't exist **")

    def create_aux(self, m_list):
        """[Auxiliar method to do_create]
        """
        try:
            result = dict([x.split("=") for x in m_list])
        except ValueError:
            print("Format error for attribute:value pair")
            return None
        for key in result.keys():
            if '.' in result[key]:
                try:
                    result[key] = float(result[key])
                    continue
                except (TypeError, ValueError):
                    pass
            else:
                try:
                    result[key] = int(result[key])
                except (TypeError, ValueError):
                    pass
            if (result[key].count('"') == (result[key].count('\\"') +
                                           2) and " " not in result[key]):
                result[key] = str(result[key].replace("_", " "))[1:-1]
            else:
                print("String Format Error for {}".format(result[key]))
                return None
        return result

    def to_show(self, args):
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        all_objs = storage.all()
        for objs in all_objs.keys():
            if objs == args[1] and args[0] in str(type(all_objs[objs.id])):
                print(all_objs[objs])
                return
        print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
