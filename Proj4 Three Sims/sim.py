# ECE 366 Fall 2019
# Project 4 - Advanced MIPS Simulator
# Sheng Chen

def chooseDiag():
    print('Choose desired display mode:\n')
    print('1) Display step-by-step diagnostic info')
    print('2) Display final state and statistics only')
    print('#) Return to main menu\n')
    diagMenu = input('Enter 1, 2, or # here: ') # holds mode user selection
    while diagMenu != '#':
        if diagMenu == '1':
            print('\nStarting in diagnostic mode...\n')
            return True
        elif diagMenu == '2':
            print('\nStarting in normal mode, skipping to final results...\n')
            return False
        else:
            print('\nInvalid input.\n')
        diagMenu = input('Enter 1, 2, or # here: ')

def mcycleSim(diagMode):
    if diagMode == True:
        print('I started in diagnostic mode!')
    else:
        print('I started in normal mode!')

def apipeSim(diagMode):
    if diagMode == True:
        print('I started in diagnostic mode!')
    else:
        print('I started in normal mode!')

def dcacheSim(diagMode):
    if diagMode == True:
        print('I started in diagnostic mode!')
    else:
        print('I started in normal mode!')

def main():

    print('\nMIPS CPU and Cache Simulator for Project 4, ECE 366 Fall 2019\n')
    print('Main menu:\n')
    print('1) Multi-cycle MIPS CPU Simulator')
    print('2) Aggressive Pipelined MIPS CPU Simulator')
    print('3) Single-level Data Cache Simulator')
    print('#) Exit\n')
    mainMenu = input('Enter 1, 2, 3, or # here: ') # holds main user selection
    while mainMenu != '#':
        if mainMenu == '1':
            print('\nStarting MC MIPS CPU Sim.\n')
            diagMode = chooseDiag()       # boolean for diagnostic mode
            mcycleSim(diagMode)           # start MC MIPS CPU simulator
        elif mainMenu == '2':
            print('\nStarting AP MIPS CPU Sim.\n')
            diagMode = chooseDiag()
            apipeSim(diagMode)           # start AP MIPS CPU simulator
        elif mainMenu == '3':
            print('\nStarting D-Cache Sim.\n')
            diagMode = chooseDiag()
            dcacheSim(diagMode)           # start data cache simulator
        else:
            print('\nInvalid input.\n')
        print('\nMain menu:\n')
        print('1) Multi-cycle MIPS CPU Simulator')
        print('2) Aggressive Pipelined MIPS CPU Simulator')
        print('3) Single-level Data Cache Simulator')
        print('#) Exit\n')
        mainMenu = input('Enter 1, 2, 3, or # here: ')

    #Instructions = []   # a place to hold all instructions
    #InstructionsHex = [] # raw data of instruction , in hex

    #I_file = open("i_mem_TRUNG.txt", "r")
    #for line in I_file:
    #    if(line == "\n" or line[0] =='#'):
    #        continue    # ignore empty lins, comments
    #    line = line.replace('\n', '')   # delete endline characters in the line
    #    InstructionsHex.append(line)
    #    line = format(int(line,16),"032b")
    #    Instructions.append(line)

    #simulate(Instructions, InstructionsHex, debugMode)


if __name__ == "__main__":
    main()
