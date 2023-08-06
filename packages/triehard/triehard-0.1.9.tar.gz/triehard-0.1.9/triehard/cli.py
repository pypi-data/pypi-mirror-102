import cmd
import requests
import sys
from nubia import Nubia, Options, command, context, argument, PluginInterface
from nubia.internal.cmdbase import AutoCommand
from termcolor import cprint
import asyncio
import socket

# MAPPINGS
# /complete (GET)  -> returns completions for a given phrase
# /sample   (POST) -> creates and fills a sample trie
# /insert   (POST) -> adds a word to the trie
# /delete   (POST) -> removes a word from the trie
# /reset    (POST) -> empties the trie
# /check    (GET)  -> checks if a given key is in the trie
# /view     (GET)  -> returns a list of words from the tree

API = "https://flask-service.e6k717ksimpmo.us-east-2.cs.amazonlightsail.com/api/"

cli = cmd.Cmd()

@command("sample")
def sample():
    "Generate a sample tree with 100 random words"
    r = requests.post(API + "sample")
    if r.ok:
        cprint("Example trie generated", "green")
    else:
        cprint("Trie generation failed", "red")
    view()

@command("reset")
def reset():
    "Reset the trie, eliminating all keys"
    cprint("Are you sure? (y/n) ", "yellow")
    confirmation = input()
    if confirmation.upper().startswith("Y"):
        r = requests.post(API + "reset")
        if r.ok:
            cprint("Trie reset", "green")
        else:
            cprint("Reset failed", "red")

@command("view")
def view():
    "View the keys in the trie, alphabetized"
    r = requests.get(API + "view")
    if r.ok:
        keys = list(r.json())
        if keys:
            cprint("Keys:", "blue")
            cli.columnize(keys, displaywidth=80)
        else:
            cprint("(empty)", "grey")
    else:
        cprint(f"Failed to get keys", "red")

@command("complete")
@argument("prefix", description="the substring completions will be based on", positional=True)
def complete(prefix: str):
    "Provides completions for a given prefix"
    json = {'prefix': prefix}
    r = requests.get(API + "complete", json=json)
    if r.ok:
        completions = list(r.json())
        if completions:
            cprint("Keys:", "blue")
            cli.columnize(completions, displaywidth=80)
        else:
            cprint("No completions available", "white")
    else:
        cprint(f"Failed to get completions", "red")

@command("check")
@argument("key", description="the key the tree is being searched for", positional=True)
def check(key: str):
    "Determines whether or not a given key is in the tree"
    json = {'key': key}
    r = requests.get(API + "check", json=json)
    if r.ok:
        cprint(r.text, "cyan")
    else:
        cprint("check for {key} failed", "red")

@command("insert")
@argument("key", description="the key to insert into the tree", positional=True)
def insert(key: str):
    "Adds a given key to the trie"
    json = {'key':key}
    r = requests.post(API + "insert", json=json)
    if r.ok:
        cprint(f"Succesfully inserted {key}", "green")
    else:
        cprint(f"Failed to insert {key}", "red")
    view()

@command("delete")
@argument("key", description="the key to remove from the tree", positional=True)
def delete(key: str):
    "Removes a given key from the trie"
    json = {'key':key}
    r = requests.post(API + "delete", json=json)
    if r.ok:
        cprint(f"{r.text}")
    else:
        cprint(f"Failed to delete {key}", "red")
    view()

class Plugin(PluginInterface):
    def get_commands(self):
        return [
            AutoCommand(sample),
            AutoCommand(reset),
            AutoCommand(view),
            AutoCommand(complete),
            AutoCommand(check),
            AutoCommand(insert),
            AutoCommand(delete),

        ]

def main():
    plugin = Plugin()
    shell = Nubia(
            name="Trie CLI",
            #command_pkgs=commands,
            plugin=plugin,
            options=Options(persistent_history=False, 
                auto_execute_single_suggestions=True)
            )
    sys.exit(shell.run())

if __name__ == "__main__":
    main()

