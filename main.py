import pickle
import sys
import os

VERSION = "0.2b"

"""
If you'll modifying the shell, please consider crediting to the creator which is me AzizBgBoss.
https://github.com/AzizBgBoss/POWER-Shell
"""


def get_history():
    if ".his" in os.listdir():
        with open('.his', 'rb') as fd:
            return pickle.load(fd)
    else:
        return list()


def save_history():
    with open('.his', 'wb') as fd:
        pickle.dump(HISTORY, fd)


print(f"POWER shell by AzizBgBoss || Version: {VERSION}\n")

try:

    HISTORY = get_history()

    while True:
        LINE = input('>> ')

        if LINE == '':
            print("No command entered. Type 'kill' to quit.")
            continue

        try:
            ELEMENTS = LINE.split()
            COMMAND = ELEMENTS[0]

        except IndexError:
            print("No command entered. Type 'kill' to quit.")
            continue

        if COMMAND == 'kill':
            print("Shell stopped.")
            save_history()
            break

        elif COMMAND == 'help':
            print(
                f"\nPOWER shell created by AzizBgBoss || Version: {VERSION}\n\nkill: Quits the shell.\nhelp: POWER shell manual. (This menu)\nprint: Prints a string.\nvar *variable* = *value*: defines a variable.\nvar *variable*: prints the value of a variable.\nhistory: shows you the commands history.\nhistory clear: Clears the history.\nfappend *file name* *content*: appends data to a file.\nfdelete *file name*: deletes a file.\nfread *file name*: prints the content of a file.\n\nRemember, spaces matter!\n"
            )

        elif COMMAND == "print":
            print(LINE.replace("print", '', 1).replace(" ", '', 1))

        elif COMMAND == "var":
            if len(ELEMENTS) == 1:
                print("No variables called or declared. Spaces matter!")
                continue
            elif len(ELEMENTS) == 2:
                try:
                    print(globals()[ELEMENTS[1]])
                except:
                    print("Error: Variable " + ELEMENTS[1] + " is not defined")
            elif len(ELEMENTS) >= 4 and ELEMENTS[2] == '=':
                if ELEMENTS[1] == "HISTORY" or ELEMENTS[
                        1] == "LINE" or ELEMENTS[1] == "COMMAND" or ELEMENTS[
                            1] == "ELEMENTS":
                    print(
                        "Illegal variable cannot be changed. Try naming something different."
                    )
                    continue
                else:
                    globals()[ELEMENTS[1]] = LINE.replace(
                        "var " + ELEMENTS[1] + " = ", '')
            else:
                print("Error: Wrong syntax. Type 'help'. Spaces matter!")

        elif COMMAND == "history":
            if len(ELEMENTS) != 1:
                if ELEMENTS[1] == "clear":
                    HISTORY = []
                    continue
            else:
                print("\n".join(HISTORY))

        elif COMMAND == "fappend":
            if len(ELEMENTS) >= 2:
                FILE = open(ELEMENTS[1],'a')
                FILE.write(LINE.replace("fappend "+ELEMENTS[1],'',1).replace(" ",'',2).replace('\\n','\n'))
                FILE.close()
                del FILE
            else:
                print("Error: Wrong syntax. Type 'help'. Spaces matter!")

        elif COMMAND == "fdelete":
            if len(ELEMENTS)==2:
                if os.path.exists(ELEMENTS[1]):
                    if input("ARE YOU SURE YOU WANT TO DELETE \'"+ELEMENTS[1]+"\'? (y/n) >>")=='y':
                        os.remove(ELEMENTS[1])
                        print("\'"+ELEMENTS[1]+"\' removed.")
                    else:
                        print("Canceled.")
                else:
                    print('\''+ELEMENTS[1]+"\' does not exist.")
            else:
                print("Error: Wrong syntax. Type 'help'. Spaces matter!")

        elif COMMAND == "fread":
            if len(ELEMENTS)==2:
                if os.path.exists(ELEMENTS[1]):
                    FILE = open(ELEMENTS[1],'r')
                    print(FILE.read())
                    FILE.close()
                    del FILE
                else:
                    print('\''+ELEMENTS[1]+"\' does not exist.")
            else:
                print("Error: Wrong syntax. Type 'help'. Spaces matter!")
        
        else:
            print("Error: Command not recognized. Type 'help' for help.")

        HISTORY.append(LINE)

except KeyboardInterrupt:
    print("Shell stopped (User CTRL+C).")
    save_history()
    sys.exit()

except:
    print("QUITTING! FATAL ERROR.\nIF PERSISTENT PLEASE WAIT FOR UPDATES AND REPORT AT https://github.com/AzizBgBoss/POWER-Shell.")
    try:
        save_history()
    except:
        sys.exit()
    sys.exit()
