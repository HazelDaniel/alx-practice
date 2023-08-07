#!/usr/bin/env python3
import cmd

friends = ["Daniel", "Hazel", "Toughware"]


class Mainloop(cmd.Cmd):
    prompt = "(user@hostname)_:"

    def do_greet(self, line=""):
        """usage: greet [person]\ngreets the name provided"""
        print("welcome {}!".format(line))

    def complete_greet(self, text, line, s_index, l_index):
        if not text:
            completions = friends[:]
        else:
            completions = [f for f in friends if f.startswith(text)]
        return completions

    def do_EOF(self, line=""):
        print(line)
        return True

    def postloop(self, line=""):
        if not line:
            line = "end"
        print("post loop on {}".format(line))

    def help_greet(self, line=""):
        print("usage: greet [name]\nreturns the name of a person")


if __name__ == "__main__":
    Mainloop().cmdloop()
