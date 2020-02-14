#!/usr/bin/python3

#    This file is part of 'ui'.
#
#    ui is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    ui is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with papertrade.  If not, see <http://www.gnu.org/licenses/>.

import os   # For clear_screen()

def menu(items, heading):
    '''Takes list of dictionaries and prints a menu.
        items parameter should be in the form of a list, containing
        dictionaries with the keys: {"key", "text", "function"}.

        Typing the key for a menuitem, followed by return, will run
        "function".
    '''

    heading = "\n"*5 + heading      # A little vertical padding

    while True:
        keydict = {}

        clear_screen()
        print(heading)

        for item in items:
            menustring = "  " + item["key"] + " " + item["text"]
            keydict[item["key"]] = item["function"]
            print(menustring)

        key = input("\nType key and Return (q to quit): ").strip()

        if key.lower() == "q":
            return
        else:
            try:
                ret = keydict[key]()
                if ret:    # If child returns non-false, exit menu.
                    return 1
            except KeyError: # Handle garbage input.
                continue


def yn_prompt(text):
    '''
        Takes the text prompt, and presents it, takes only "y" or "n" for
        answers, and returns True or False. Repeats itself on bad input.
    '''

    text = "\n"+ text + "\n('y' or 'n'): "


    while True:
        answer = input(text).strip()
        if answer != 'y' and answer != 'n':
            continue
        elif answer == 'y':
            return True
        elif answer == 'n':
            return False

def show(text):
    '''Presents text, and returns on any input.'''
    clear_screen()
    print("\n"*5 + text)        # Adding extra newlines to create space.
    input("(Press Return to go back): ")

def underline(text):
    '''Takes a string, and returns it underscored.'''

    text += "\n"
    for i in range(len(text)-1):
        text += "="
    text += "\n"
    return text

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    def test():
        print("Testfunc!")

    def test_two():
        prompt = (
            "Thist is a long line, | Kind of like a table | yeah..."
            " NO MORE OF THIS!!!!! BAHAHA!"
        )
        if yn_prompt(prompt):
            print("Returned True")
        else:
            print("Returned False.")

    testitems = [
        {"key":"p", "text":"Passepå", "function":test},
        {"key":"p", "text":"Passepå", "function":test},
        {"key":"t", "text":"Test", "function":test_two},
    ]

    menu(testitems, "Main Menu!")
