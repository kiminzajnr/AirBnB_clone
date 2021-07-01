#!/usr/bin/python3
"""Command interpreter.
"""
import cmd
import models


class HBNBCommand(cmd.Cmd):
    """Command iterpreter public class which inherites from base class cmd.
    """
    prompt = '(hbnb) '

    def do_create(self, line):
        """creates a new instance of BaseModel, saves it
        (to the json file) and prints the id
        """
        if len(line) == 0:
            print("** class name missing **")
        
        new_instance = models.base_model.BaseModel()
        print(new_instance.id)
        new_instance.save()

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """Ctrl+D command to exit the program
        """
        print()
        return True

    def emptyline(self):
        """Called when empty line + Enter. Override the default behaviour,
        execute the previous command, with just do nothing.
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
