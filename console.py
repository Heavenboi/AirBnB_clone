#!/usr/bin/env python3
"""
    a program that contains the entry point of the command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """the class definition initialization"""
    prompt = "(hbnb) "

    def do_quit(self, args):
        """Quit command to exit the program"""
        #print ('Thank you for using the console')
        return True

    def do_EOF(self, args):
        """this will handle end of file"""
        print("")
        return True

    def emptyline(self):
        """
            this make the commandline not to repeate the previous used
        """
        pass



    
if __name__ == '__main__':
    HBNBCommand().cmdloop()
