#!/usr/bin/env python3
"""
    a program that contains the entry point of the command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """the class definition initialization"""
    prompt = "(hbnb)"

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """this will handle end of file"""
        return True

    
if __name__ == '__main__':
    HBNBCommand().cmdloop()
