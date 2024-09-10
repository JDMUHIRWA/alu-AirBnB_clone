#1/usr/bin/python
"""
Module documentation
"""

import cmd 


class HBNBCommand(cmd.Cmd):
    """
    This is my module
    """

    prompt = "(hbnb)"

    
    def do_EOF(self, arg):
        print("")
        return True

    def do_quit(self, arg):
        """
        
        """
        return True

    def help_quit(self, arg):
        """

        """
        print("Quit command to exit the program")
    
  


if __name__ == "__main__":
    HBNBCommand().cmdloop()


