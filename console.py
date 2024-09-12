#!/usr/bin/env python3
"""Module for console"""
import cmd
import shlex
import re
import ast
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City


def split_curly_braces(extra_arg):
    """
    Splits the curly braces for the update method.
    """
    curly_braces = re.search(r"\{(.*?)\}", extra_arg)

    if curly_braces:
        id_with_comma = shlex.split(extra_arg[:curly_braces.span()[0]])
        instance_id = [i.strip(",") for i in id_with_comma][0]

        str_data = curly_braces.group(1)
        try:
            arg_dict = ast.literal_eval("{" + str_data + "}")
        except (SyntaxError, ValueError):
            print("** invalid dictionary format **")
            return None, None
        return instance_id, arg_dict
    else:
        commands = extra_arg.split()
        if len(commands) >= 3:
            return commands[0], {commands[1]: commands[2]}
        return commands[0], {}


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand console class.
    """
    prompt = "(hbnb) "
    valid_classes = ["BaseModel", "User", "Amenity",
                     "Place", "Review", "State", "City"]

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    def do_EOF(self, arg):
        """EOF (Ctrl+D) signal to exit the program."""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_create(self, arg):
        """
        Create a new instance of BaseModel and save it to the JSON file.
        Usage: create <class_name>
        """
        commands = shlex.split(arg)

        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(f"{commands[0]}()")
            storage.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        Show the string representation of an instance.
        Usage: show <class_name> <id>
        """
        commands = shlex.split(arg)

        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(commands[0], commands[1])
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Delete an instance based on the class name and id.
        Usage: destroy <class_name> <id>
        """
        commands = shlex.split(arg)

        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(commands[0], commands[1])
            if key in objects:
                del objects[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Print the string representation of all instances or a specific class.
        Usage: <class_name>.all()
        """
        objects = storage.all()
        commands = shlex.split(arg)

        if len(commands) == 0:
            for value in objects.values():
                print(str(value))
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            for key, value in objects.items():
                if key.split('.')[0] == commands[0]:
                    print(str(value))

    def do_count(self, arg):
        """
        Counts and retrieves the number of instances of a class.
        Usage: <class_name>.count()
        """
        objects = storage.all()
        commands = shlex.split(arg)

        if len(commands) == 0:
            print("** class name missing **")
            return

        class_name = commands[0]
        if class_name in self.valid_classes:
            count = sum(1 for obj in objects.values() if obj.__class__.__name__ == class_name)
            print(count)
        else:
            print("** invalid class name **")

    def do_update(self, arg):
        """
        Update an instance by adding or updating an attribute.
        Usage: update <class_name> <id> <attribute_name> "<attribute_value>"
        """
        commands = shlex.split(arg)

        if len(commands) < 2:
            print("** class name or id missing **")
            return

        class_name = commands[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return

        if len(commands) < 3:
            print("** instance id missing **")
            return

        instance_id = commands[1]
        objects = storage.all()
        key = "{}.{}".format(class_name, instance_id)

        if key not in objects:
            print("** no instance found **")
            return

        if len(commands) < 4:
            print("** attribute name or value missing **")
            return

        attr_name = commands[2]
        attr_value = commands[3]

        try:
            attr_value = eval(attr_value)
        except (SyntaxError, NameError):
            pass

        setattr(objects[key], attr_name, attr_value)
        objects[key].save()

    def default(self, arg):
        """
        Default behavior for cmd module when input is invalid.
        """
        try:
            class_name, method = arg.split('.', 1)
            method, extra_arg = method.split('(', 1)
            extra_arg = extra_arg.rstrip(')')

            method_dict = {
                'all': self.do_all,
                'show': self.do_show,
                'destroy': self.do_destroy,
                'update': self.do_update,
                'count': self.do_count
            }

            if method in method_dict:
                if method != 'update':
                    method_dict[method](f"{class_name} {extra_arg}")
                else:
                    instance_id, arg_dict = split_curly_braces(extra_arg)
                    if instance_id is not None:
                        method_dict[method](f"{class_name} {instance_id} {arg_dict}")
            else:
                print(f"*** Unknown syntax: {arg}")
        except (ValueError, IndexError):
            print(f"*** Unknown syntax: {arg}")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
