import cmd
import requests
import sys
from nubia import Nubia, Options, command, context, argument
from termcolor import cprint
import asyncio
import socket
import lib


# MAPPINGS
# /complete (GET)  -> returns completions for a given phrase
# /sample   (POST) -> creates and fills a sample trie
# /insert   (POST) -> adds a word to the trie
# /delete   (POST) -> removes a word from the trie
# /reset    (POST) -> empties the trie
# /check    (GET)  -> checks if a given key is in the trie
# /view     (GET)  -> returns a list of words from the tree

def main():
    shell = Nubia(
            name="Trie CLI",
            command_pkgs=lib,
            options=Options(persistent_history=False, 
                auto_execute_single_suggestions=True)
            )
    sys.exit(shell.run())

if __name__ == "__main__":
    main()

