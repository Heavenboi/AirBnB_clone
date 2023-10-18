#!/usr/bin/python3
"""
a program that contains the entry point of the command interpreter
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review

""" Create a dictionary mapping class names to class objects """
class_names = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "Amenity": Amenity,
    "City": City,
    "Place": Place,
    "Review": Review,
}


class HBNBCommand(cmd.Cmd):
    """the class definition initialization"""

    prompt = "(hbnb) "

    def do_quit(self, args):
        """Quit command to exit the program"""
        """print("Thank you for using the console")"""
        return True

    def do_EOF(self, args):
        """this will handle the end of file"""
        print("")
        return True

    def emptyline(self):
        """
        this makes the command line not repeat the previously used command
        """
        pass

    def do_create(self, args):
        """
        Creates a new instance of BaseModel, saves it to the JSON file,
        and prints the id.
        """
        if not args:
            print("** class name missing **")
            return
        if args not in class_names:
            print("** class does not exist **")
            return
        try:
            new_instance = class_names[args]()
            new_instance.save()
            print(new_instance.id)
        except Exception as e:
            print(e)

    def do_show(self, args):
        """
        Prints the string representation of an instance
        based on the class name and id.
        """
        if not args:
            print("** class name missing **")
            return
        arg_list = args.split()
        if arg_list[0] not in class_names:
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:
            print("** instance id missing **")
            return
        obj_key = "{}.{}".format(arg_list[0], arg_list[1])
        all_objs = storage.all()
        if obj_key in all_objs:
            print(all_objs[obj_key])
        else:
            print("** no instance found **")

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id
        (saves the change into the JSON file)
        """
        if not args:
            print("** class name missing **")
            return
        arg_list = args.split()
        if arg_list[0] not in class_names:
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:
            print("** instance id missing **")
            return
        obj_key = "{}.{}".format(arg_list[0], arg_list[1])
        all_objs = storage.all()
        if obj_key in all_objs:
            del all_objs[obj_key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, args):
        """
        Prints all string representations of all instances
        based or not on the class name.
        """
        arg_list = args.split()
        if len(arg_list) == 0 or arg_list[0] == "":
            all_objs = storage.all()
            print([str(obj) for obj in all_objs.values()])
        elif arg_list[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        else:
            all_objs = storage.all()
            filtered_objs = [
                str(obj)
                for obj in all_objs.values()
                if obj.__class__.__name__ == arg_list[0]
            ]
            print(filtered_objs)

    def do_update(self, args):
        """
        Updates an instance based on the class name and
        id by adding or updating an attribute.
        """
        if not args:
            print("** class name missing **")
            return
        arg_list = args.split()
        if arg_list[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:
            print("** instance id missing **")
            return
        obj_key = "{}.{}".format(arg_list[0], arg_list[1])
        all_objs = storage.all()
        if obj_key not in all_objs:
            print("** no instance found **")
            return
        if len(arg_list) < 3:
            print("** attribute name missing **")
            return
        if len(arg_list) < 4:
            print("** value missing **")
            return
        attribute_name = arg_list[2]
        attribute_value = arg_list[3]

        """
            Check if the attribute_name is a valid attribute for the model
        """
        if hasattr(all_objs[obj_key], attribute_name):
            """
            Cast the attribute value to the appropriate type
            """
            if hasattr(all_objs[obj_key], attribute_name):
                attr_type = type(getattr(all_objs[obj_key], attribute_name))
                if attr_type == int:
                    attribute_value = int(attribute_value)
                elif attr_type == float:
                    attribute_value = float(attribute_value)
            setattr(all_objs[obj_key], attribute_name, attribute_value)
            storage.save()
        else:
            print("** attribute name doesn't exist **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
