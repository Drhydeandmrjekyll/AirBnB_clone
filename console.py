import cmd

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Exit program"""
        return True

    def do_EOF(self, arg):
        """Exit program using Ctrl+D (EOF)"""
        return True

    def emptyline(self):
        """Do nothing when empty line is entered"""
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
