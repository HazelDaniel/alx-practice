#!/usr/bin/env python3
import cmd

friends = ["Daniel", "Hazel", "Toughware"]


class Mainloop(cmd.Cmd):
    prompt = "prompt:\n"

    def do_greet(self, line=""):
        """usage: greet [person]\ngreets the name provided"""
        print("welcome {}!".format(line))


    def complete_greet(self, text, line, s_index, l_index):
        if not text:
            completions = friends[:]
        else:
            completions = [f for f in friends if f.startswith(text)]
        return completions

    def do_makebutter(self, line):
        """works"""
        pass

    def do_makecheese(self, line):
        """works"""
        pass

    def do_EOF(self, line=""):
        """this handles what happens when ^D key is pressed"""
        print(line)
        return True

    def postloop(self, line=""):
        """this handles what happens after the repl phase"""
        if not line:
            line = "end"
        print("post loop on {}".format(line))

    def do_help(self, line):
        super().do_help(line)

    def help_greet(self, line=""):
        print("usage: greet [name]\nreturns the name of a person")

    def do_quit(self, line=""):
        """this handles the quit command"""
        return True


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        Mainloop().onecmd(' '.join(sys.argv[1:]))
    else:
        Mainloop().cmdloop()
