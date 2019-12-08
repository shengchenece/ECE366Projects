# ECE 366 Fall 2019
# Project 4 - Advanced MIPS Simulator
# Sheng Chen
# Some functions modified from code by Trung le

#
# chooseDiag: submenu to choose verbose diagnostic or normal end-result modes
#
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

# 
# saveJumpLabel: helper function for getInstructions()
# Remembers where each of the jump labels are, as well as the target location
#
# def saveJumpLabel(asm,labelIndex, labelName):
#    lineCount = 0
#    for line in asm:
#        line = line.replace(" ","")
#        if(line.count(":")):
#            labelName.append(line[0:line.index(":")]) # append the label name
#            labelIndex.append(lineCount) # append the label's index
#            asm[lineCount] = line[line.index(":")+1:]
#        lineCount += 1
#    for item in range(asm.count('\n')): # Remove all empty lines '\n'
#        asm.remove('\n')

#
# getInstructions: formats assembly code for ease of use in simulator
#
def getInstructions():

    I_file = open("Program_A1.asm", "r")
    Instructions = I_file.readlines()   # holds all instructions
    for j in range(len(Instructions)): # Scrub all comment lines ('#' -> '\n')
        if Instructions[j].startswith('#'):
            Instructions[j] = '\n'
    for item in range(Instructions.count('\n')): # Remove all empty lines '\n'
        Instructions.remove('\n')
    for k in range(len(Instructions)):           # Remove all extra chars
        Instructions[k] = Instructions[k].replace('\n', '')
        Instructions[k] = Instructions[k].replace("$","")
        Instructions[k] = Instructions[k].replace(" ","")
        Instructions[k] = Instructions[k].replace("zero","0") # zero for 0

#    labelIndex = []
#    labelName = []
#    f = open("mc.txt","w+")

#    saveJumpLabel(asm,labelIndex,labelName) # Save all jump's destinations

#        if(line[0:4] == "addi"): # ADDI
#            line = line.replace("addi","")
#            line = line.split(",")
#            imm = format(int(line[2]),'016b') if (int(line[2]) > 0) else format(65536 + int(line[2]),'016b')
#            rs = format(int(line[1]),'05b')
#            rt = format(int(line[0]),'05b')
#            f.write(str('001000') + str(rs) + str(rt) + str(imm) + '\n')

#        elif(line[0:3] == "add"): # ADD
#            line = line.replace("add","")
#            line = line.split(",")
#            rd = format(int(line[0]),'05b')
#            rs = format(int(line[1]),'05b')
#            rt = format(int(line[2]),'05b')
#            f.write(str('000000') + str(rs) + str(rt) + str(rd) + str('00000100000') + '\n')
            
#        elif(line[0:1] == "j"): # JUMP
#            line = line.replace("j","")
#            line = line.split(",")

            # Since jump instruction has 2 options:
            # 1) jump to a label
            # 2) jump to a target (integer)
            # We need to save the label destination and its target location

#            if(line[0].isdigit()): # First,test to see if it's a label or a integer
#                f.write(str('000010') + str(format(int(line[0]),'026b')) + '\n')

#            else: # Jumping to label
#                for i in range(len(labelName)):
#                    if(labelName[i] == line[0]):
#                        f.write(str('000010') + str(format(int(labelIndex[i]),'026b')) + '\n')

#    f.close()
    return Instructions

#
# mcycleSim: MC MIPS CPU simulator
#
def mcycleSim(diagMode):

    Instructions = getInstructions()
    print(Instructions)

#
# apipeSim: AP MIPS CPU simulator
#
def apipeSim(diagMode):
    if diagMode == True:
        print('I started in diagnostic mode!')
        print("I'm sorry, I didn't make it to the end of this project...")
    else:
        print('I started in normal mode!')
        print("I'm sorry, I didn't make it to the end of this project...")

#
# dcacheSim: Data cache simulator
#
def dcacheSim(diagMode):
    if diagMode == True:
        print('I started in diagnostic mode!')
        print("I'm sorry, I didn't make it to the end of this project...")
    else:
        print('I started in normal mode!')
        print("I'm sorry, I didn't make it to the end of this project...")



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

if __name__ == "__main__":
    main()
