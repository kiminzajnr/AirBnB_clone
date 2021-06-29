#!/usr/bin/python3
"""Command interpreter.
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Command iterpreter public class which inherites from base class cmd.
    """
    prompt = '(hbnb) '

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
