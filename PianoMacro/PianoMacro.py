import keyboard
import time

tempoModifier = .85


print("Paste your piano keys into the SheetMusic.txt file.")
#startSignal = input("Press Enter to start the macro...")
print("Keys will be played in 5 seconds.")
time.sleep(5)

file = open("PianoMacro\SheetMusic.txt", "r")

inBrackets = False
brackets = ''

for line in file:
    line = line.strip()

    if line == "":
        time.sleep(0.5 * tempoModifier)
        continue
    for char in line:
        if inBrackets and char != ']':
            brackets += char
            continue

        elif char == ' ':
            time.sleep(0.25 * tempoModifier)
        elif char == '|':
            time.sleep(0.5 * tempoModifier)

        elif char == '[':
            inBrackets = True
            brackets = ''
        elif char == ']':
            inBrackets = False
            keyGrouping = ''

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
                    keyGrouping += brackets[key] + "+"
            time.sleep(0.15 * tempoModifier)
        else:
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