import pickle
import sys
import os
import time

VERSION = "0.3b"
DEBUG = True
PDIR = os.getcwd()
"""
If you'll modifying the shell, please consider crediting to the creator which is me, AzizBgBoss.
https://github.com/AzizBgBoss/POWER-Shell
"""

def execution(LINE, COMMAND, ELEMENTS, LINEN):

    global HISTORY

    if COMMAND == 'kill':
        print("Shell stopped.")
        save_history()
        return 'break'

    elif COMMAND == 'help':
        print(
            f"\nPOWER shell created by AzizBgBoss || Version: {VERSION}" +
            "\n\nkill: Quits the shell." +
            "\nhelp: POWER shell manual. (this menu)" +
            "\nprint: Prints a string (use '${VAR}' to append a variable)." +
            "\nvar *variable* = *value*: defines a variable." +
            "\nvar *variable*: prints the value of a variable." +
            "\nhistory: shows you the commands history." +
            "\nhistory clear: Clears the history." +
            "\nfappend *file name* *content*: appends data to a file." +
            "\nfdelete *file name*: deletes a file." +
            "\nfread *file name*: prints the content of a file." +
            "\nwait *milliseconds*: waits :D." +
            "\nscript *file name*: runs the script in a file." +
            f"\ndebug *boolean*: shows Python fatal error when possible (default: {DEBUG.lower()})." +
            "\nread *var* *line*: prints *line* and save user answer in *var*." +
            "\ndir *path*: change the file directory path (enter whole path (c:/.../folder))." +
            "\n\nRemember, spaces matter!\n"
        )

    elif COMMAND == "print":
        PLINE = LINE.replace("print", '', 1).replace(" ", '', 1)
        VARD = PLINE.count('$')
        VARO = PLINE.count('{')
        VARC = PLINE.count('}')
        if VARD != 0 and VARO != 0 and VARC != 0:
            for i in range(VARD):
                try:
                    if PLINE[PLINE.index('$')+1] == '{' and '}' in PLINE:
                        VAR = PLINE[PLINE.index('{')+1:PLINE.index('}')]
                        try:
                            PLINE = PLINE.replace(
                                '${'+VAR+'}', str(globals()[VAR]))
                        except:
                            PLINE = PLINE.replace('${'+VAR+'}', '')
                except:
                    continue
                print(PLINE)
        else:
            print(str(LINE.replace("print", '', 1).replace(" ", '', 1)))
        del PLINE, VARD, VARC, VARO

    elif COMMAND == "var":
        if len(ELEMENTS) == 1:
            print("No variables called or declared. Spaces matter!")
            return 'continue'
        elif len(ELEMENTS) == 2:
            try:
                print(globals()[ELEMENTS[1]])
            except:
                print(f"Error at line {LINEN}: Variable " +
                      ELEMENTS[1] + " is not defined")
        elif len(ELEMENTS) >= 4 and ELEMENTS[2] == '=':
            if ELEMENTS[1] in ["HISTORY", "LINE", "COMMAND", "ELEMENTS", "DEBUG", "VERSION", "SCRIPTMODE", "PDIR"]:
                print(
                    "Illegal variable cannot be changed. Try naming something different."
                )
                return 'continue'
            else:
                globals()[ELEMENTS[1]] = LINE.replace(
                    "var " + ELEMENTS[1] + " = ", '')
        else:
            print(
                f"Error at line {LINEN}: Wrong syntax. Type 'help'. Spaces matter!")

    elif COMMAND == "history":
        if len(ELEMENTS) != 1:
            if ELEMENTS[1] == "clear":
                HISTORY = []
                save_history()
                HISTORY = get_history()
                return 'continue'
        else:
            print("\n".join(HISTORY))

    elif COMMAND == "fappend":
        if len(ELEMENTS) >= 2:
            FILE = open(ELEMENTS[1], 'a')
            FILE.write(
                LINE.replace("fappend " + ELEMENTS[1], '',
                             1).replace(" ", '', 1).replace('\\n', '\n'))
            FILE.close()
            del FILE
        else:
            print(
                f"Error at line {LINEN}: Wrong syntax. Type 'help'. Spaces matter!")

    elif COMMAND == "fdelete":
        if len(ELEMENTS) == 2:
            if os.path.exists(ELEMENTS[1]):
                if input("ARE YOU SURE YOU WANT TO DELETE \'" + ELEMENTS[1] +
                         "\'? (y/n) >>") == 'y':
                    os.remove(ELEMENTS[1])
                    print("\'" + ELEMENTS[1] + "\' removed.")
                else:
                    print("Canceled.")
            else:
                print('\'' + ELEMENTS[1] + "\' does not exist.")
        else:
            print(
                f"Error at line {LINEN}: Wrong syntax. Type 'help'. Spaces matter!")

    elif COMMAND == "fread":
        if len(ELEMENTS) == 2:
            if os.path.exists(ELEMENTS[1]):
                FILE = open(ELEMENTS[1], 'r')
                print(FILE.read())
                FILE.close()
                del FILE
            else:
                print('\'' + ELEMENTS[1] + "\' does not exist.")
        else:
            print(
                f"Error at line {LINEN}: Wrong syntax. Type 'help'. Spaces matter!")

    elif COMMAND == "wait":
        try:
            if len(ELEMENTS) == 2:
                time.sleep(int(ELEMENTS[1])/1000)
            else:
                print(
                    f"Error at line {LINEN}: Wrong syntax. Type 'help'. Spaces matter!")
        except TypeError:
            print(f"Error at line {LINEN}: entered time must be an integer.")
        except:
            print(
                f"Error at line {LINEN}: Wrong syntax. Type 'help'. Spaces matter!")

    elif COMMAND == "read":
        if len(ELEMENTS) >= 2:
            globals()[ELEMENTS[1]] = input(LINE.replace(
                f"read {ELEMENTS[1]}", '', 1).replace(" ", '', 1))
        else:
            print(
                f"Error at line {LINEN}: Wrong syntax. Type 'help'. Spaces matter!")

    else:
        print(
            f"Error at line {LINEN}: Command not recognized. Type 'help' for help.")

    HISTORY.append(LINE)


def get_history():
    global PDIR
    if ".his" in os.listdir():
        with open(PDIR+'\\.his', 'rb') as fd:
            return pickle.load(fd)
    else:
        return list()


def save_history():
    global PDIR
    with open(PDIR+'\\.his', 'wb') as fd:
        pickle.dump(HISTORY, fd)


print(f"POWER shell by AzizBgBoss || Version: {VERSION}\n")

try:

    HISTORY = get_history()
    LINEN = ''

    while True:
        LINE = input(f'{os.getcwd()} >> ')

        if LINE == '':
            print("No command entered. Type 'kill' to quit.")
            continue

        try:
            ELEMENTS = LINE.split()
            COMMAND = ELEMENTS[0]

        except IndexError:
            print("No command entered. Type 'kill' to quit.")
            continue
        if COMMAND == 'script':
            if len(ELEMENTS) == 2:
                if os.path.exists(ELEMENTS[1]):
                    FILE = open(ELEMENTS[1], 'r')
                    LINEN = 0
                    for LINE in (FILE.readlines()):
                        LINEN += 1
                        try:
                            ELEMENTS = LINE.split()
                            COMMAND = ELEMENTS[0]
                        except:
                            break
                        RETURN = execution(LINE.replace(
                            '\n', '', 1), COMMAND, ELEMENTS, LINEN)
                        if RETURN == 'break':
                            break
                        elif RETURN == 'continue':
                            continue
                        del RETURN
                    FILE.close()
                    del FILE
                    LINEN = ''
                else:
                    print('\'' + ELEMENTS[1] + "\' does not exist.")
            else:
                print(
                    f"Error at line {LINEN}: Wrong syntax. Type 'help'. Spaces matter!")

        elif COMMAND == "debug":
            if len(ELEMENTS) == 1:
                print(str(DEBUG).lower())
            elif len(ELEMENTS) == 2:
                if ELEMENTS[1] == 'true':
                    DEBUG = True
                elif ELEMENTS[1] == 'false':
                    DEBUG = False
                else:
                    print(
                        f"Error at line {LINEN}: Wrong syntax. Type 'help'. Spaces matter!")
            else:
                print(
                    f"Error at line {LINEN}: Wrong syntax. Type 'help'. Spaces matter!")

        elif COMMAND == 'dir':
            if len(ELEMENTS) != 1:
                os.chdir(LINE.replace("dir ", '', 1))
            else:
                print(
                    f"Error at line {LINEN}: Wrong syntax. Type 'help'. Spaces matter!")

        else:
            RETURN = execution(LINE, COMMAND, ELEMENTS, '')
            if RETURN == 'break':
                break
            elif RETURN == 'continue':
                continue
            del RETURN

except KeyboardInterrupt:
    print("Shell stopped (User CTRL+C).")
    save_history()
    sys.exit()


except Exception as EXCEPTION:
    if DEBUG == False:
        print(
            "QUITTING! FATAL ERROR.\nIF PERSISTENT PLEASE WAIT FOR UPDATES AND REPORT AT https://github.com/AzizBgBoss/POWER-Shell."
        )
    else:
        print(str(EXCEPTION))
        del EXCEPTION
    try:
        save_history()
    except:
        time.sleep(3)
        sys.exit()
    time.sleep(3)
    sys.exit()
