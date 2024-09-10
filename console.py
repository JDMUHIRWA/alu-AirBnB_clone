#!/usr/bin/python3
"""
Module documentation
"""

import cmd 


class HBNBCommand(cmd.Cmd):
    """
    
    """
    prompt = "(hbnb)"

    
    def do_EOF(self, arg):
        """
        
        """
        print()
        return True

    def do_quit(self, arg):
        """
        """
        return True

    def help_quit(self, arg):
        """
        """
        print("Quit command to exit the program")
    
    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass
    
  

if __name__ == "__main__":
    HBNBCommand().cmdloop()


