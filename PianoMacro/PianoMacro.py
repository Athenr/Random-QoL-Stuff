import keyboard
import time

tempoModifier = .85


print("Paste your piano keys into the SheetMusic.txt file.")
#startSignal = input("Press Enter to start the macro...")
print("Keys will be played in 5 seconds.")
time.sleep(5)

def PianoMacro():
    file = open("PianoMacro\SheetMusic.txt", "r")

    inBrackets = False
    brackets = ''

    for line in file:
        line = line.strip()

        if line == "":
            time.sleep(0.5 * tempoModifier)
            continue

        for char in line:
            # Adds any key grouping notes to a string to be played together
            if inBrackets and char != ']':
                brackets += char
                continue

            # Various levels of spacing (rests) between notes
            elif char == ' ':
                time.sleep(0.25 * tempoModifier)
            elif char == '|':
                time.sleep(0.5 * tempoModifier)

            #  Bracket open - Start of a key grouping
            elif char == '[':
                inBrackets = True
                brackets = ''
            # Bracket close - End of a key grouping
            elif char == ']':
                inBrackets = False
                keyGrouping = ''

                # Handles any key groupings (notes in brackets)
                for key in range(len(brackets)):
                    if  key == len(brackets) - 1 or (key <= len(brackets) - 2 and brackets[key + 1] == ' '):
                        keyGrouping += brackets[key]
                        #print(keyGrouping)
                        keyboard.press(keyGrouping)
                        time.sleep(0.1 * tempoModifier)
                        keyboard.release(keyGrouping)
                        keyGrouping = ''
                    elif brackets[key] == ' ':
                        time.sleep(0.15 * tempoModifier)
                    else:
                        # Adds notes delimited by  a '+' to play simultaneously
                        keyGrouping += brackets[key] + "+"
                time.sleep(0.15 * tempoModifier)
            else:
                # Sharp/flat notes (capital letters) - requires shift key to be held
                if char.isupper():
                    keyboard.press("shift" + "+" + char)
                    time.sleep(0.1 * tempoModifier)
                    keyboard.release("shift" + "+" + char)
                else:
                    keyboard.press(char)
                    time.sleep(0.1 * tempoModifier)
                    keyboard.release(char)
                time.sleep(0.15 * tempoModifier)
        time.sleep(0.15 * tempoModifier)
