# ECE 366 Fall 2019
# Project 4 - Advanced MIPS Simulator
# Sheng Chen
# Some functions modified from code by Trung le


# This class keeps track of all the statistics needed for
# simulation results.
# Feel free to add any stats 
class Statistic:
    
    def __init__(self,diagMode):
        self.I = []              # Current instr being executed
        self.name = ''           # name of the instruction
        self.cycle = 0           # Total cycles in simulation
        self.DIC = 0             # Total Dynamic Instr Count
        self.threeCycles= 0      # How many instr that took 3 cycles to execute
        self.fourCycles = 0      #                          4 cycles
        self.fiveCycles = 0      #                          5 cycles
        self.diagMode = diagMode

    def log(self,I,name,cycle,pc):
        self.I = I
        self.name = name
        self.cycle = self.cycle + cycle
        self.pc = pc
        self.DIC += 1
        self.threeCycles += 1 if (cycle == 3) else 0
        self.fourCycles += 1 if (cycle == 4) else 0
        self.fiveCycles += 1 if (cycle == 5) else 0

    # Since the self.cycle has the updated cycles, need to substract x cycles for correct printing , i.e (self.cycle - x)
    def prints(self):
        if(self.diagMode):
            print('\n')
            if(self.name == 'addi'):
                print("Cycle: " + str(self.cycle-4) + "|PC: " +str(self.pc*4) + " addi $" + self.I[0] + ",$" + self.I[1] + ","  + self.I[2] + "   Taking 4 cycles")
            elif(self.name == 'beq'):
                print("Cycle: " + str(self.cycle-3) + "|PC: " +str(self.pc*4) + " beq $" + self.I[0] + ",$" + self.I[1] + ","  + self.I[2] + "   Taking 3 cycles")
            elif(self.name == 'bne'):
                print("Cycle: " + str(self.cycle-3) + "|PC: " +str(self.pc*4) + " bne $" + self.I[0] + ",$" + self.I[1] + ","  + self.I[2] + "   Taking 3 cycles")
            elif(self.name == 'ori'):
                print("Cycle: " + str(self.cycle-4) + "|PC: " +str(self.pc*4) + " ori $" + self.I[0] + ",$" + self.I[1] + ","  + self.I[2] + "   Taking 4 cycles")
            elif(self.name == "addu"):
                print("Cycle: " + str(self.cycle-4) + "|PC: " +str(self.pc*4) + " addu $" + self.I[0] + ",$" + self.I[1] + ",$" + self.I[2] + "   Taking 4 cycles")
            elif(self.name == "add"):
                print("Cycle: " + str(self.cycle-4) + "|PC: " +str(self.pc*4) + " add $" + self.I[0] + ",$" + self.I[1] + ",$" + self.I[2] + "   Taking 4 cycles")
            elif(self.name == 'sll'):
                print("Cycle: " + str(self.cycle-4) + "|PC: " +str(self.pc*4) + " sll $" + self.I[0] + ",$" + self.I[1] + ","  + self.I[2] + "   Taking 4 cycles")
            elif(self.name == "sltu"):
                print("Cycle: " + str(self.cycle-4) + "|PC: " +str(self.pc*4) + " sltu $" + self.I[0] + ",$" + self.I[1] + ",$" + self.I[2] + "   Taking 4 cycles")
            elif(self.name == "slt"):
                print("Cycle: " + str(self.cycle-4) + "|PC: " +str(self.pc*4) + " slt $" + self.I[0] + ",$" + self.I[1] + ",$" + self.I[2] + "   Taking 4 cycles")
            elif(self.name == "sub"):
                print("Cycle: " + str(self.cycle-4) + "|PC: " +str(self.pc*4) + " sub $" + self.I[0] + ",$" + self.I[1] + ",$" + self.I[2] + "   Taking 4 cycles")
            elif(self.name == "xor"):
                print("Cycle: " + str(self.cycle-4) + "|PC: " +str(self.pc*4) + " xor $" + self.I[0] + ",$" + self.I[1] + ",$" + self.I[2] + "   Taking 4 cycles")
            elif(self.name == "lw"):
                memAddr = (self.I[1]).split('(')
                immStr = memAddr[0]
                rsStr = memAddr[1]
                rsStr = rsStr.replace(')','') # remove end parentheses
                print("Cycle: " + str(self.cycle-5) + "|PC: " +str(self.pc*4) + " lw $" + self.I[0] + "," + immStr + "($" + rsStr + ")" + "   Taking 5 cycles")
            elif(self.name == "sw"):
                memAddr = (self.I[1]).split('(')
                immStr = memAddr[0]
                rsStr = memAddr[1]
                rsStr = rsStr.replace(')','') # remove end parentheses
                print("Cycle: " + str(self.cycle-4) + "|PC: " +str(self.pc*4) + " sw $" + self.I[0] + "," + immStr + "($" + rsStr + ")" + "   Taking 4 cycles")
            else:
                print("")

    def exitSim(self):
        print("\n***Finished simulation***")
        print("\nTotal # of cycles: " + str(self.cycle))
        print("Dynamic instructions count: " +str(self.DIC) + ". Break down:")
        print("                    " + str(self.threeCycles) + " instructions take 3 cycles" )  
        print("                    " + str(self.fourCycles) + " instructions take 4 cycles" )
        print("                    " + str(self.fiveCycles) + " instructions take 5 cycles" )

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
# getInstructions: formats assembly code for ease of use in simulator
#
def getInstructions():

    I_file = open('Program_A1.txt', 'r')
    Instructions = I_file.readlines()   # holds all instructions
    for j in range(len(Instructions)): # Scrub comment lines ('#blah' -> '\n')
        if Instructions[j].startswith('#'):
            Instructions[j] = '\n'
    for item in range(Instructions.count('\n')): # Remove all empty lines '\n'
        Instructions.remove('\n')
    for k in range(len(Instructions)):           # Remove all extra chars
        Instructions[k] = Instructions[k].replace('\n', '')
        Instructions[k] = Instructions[k].replace('$','')
        Instructions[k] = Instructions[k].replace(' ','')
        Instructions[k] = Instructions[k].replace('zero','0') # zero for 0
    Instructions.append('Deadloop') # add final instruction to stop sim

    return Instructions

#
# mcycleSim: MC MIPS CPU simulator
#
def mcycleSim(diagMode):

    branchTargets = {} # dict to hold branch tag key/ instr nubmer value pairs
    Instructions = getInstructions()

    tagsToScrub = -1 # iterator for lines removed after branch tags are scrubbed
    for n in range(len(Instructions)): # Check lines for branch target tags
        if Instructions[n].count(':'):
            tagsToScrub += 1
            temp = Instructions[n]     # n is line number in program
            temp = temp.replace(':','')
            branchTargets[temp] = (n - tagsToScrub) # dict value line-x & tag key
    for p in range(len(Instructions)): # Scrub all tag lines ('blah:' -> '\n')
        if Instructions[p].endswith(':'):
            Instructions[p] = '\n'
    for item in range(Instructions.count('\n')): # Remove all empty lines '\n'
        Instructions.remove('\n')

    print('List of instructions (for debugging):')
    print(Instructions)
    print('\n')

    Register = [0 for i in range(24)]   # initialize regs from $0-$24, but
                               # only utilize $8 - $23 as stated in guideline
    Memory = [0 for i in range(1024)]
    stats = Statistic(diagMode) # init. the statistic class, tracks diagMode

    PC =  0                             # Set PC to 0, beginning of the program

    finished = False
    while(not(finished)):
        fetch = Instructions[PC]        # the instruction at this PC address

        if(fetch == 'Deadloop'):
            finished = True
            print("Deadloop instruction at PC = " + str(PC*4) + ". Exiting simulation..." )

        # I-type instructions

        elif(fetch[0:4] == 'addi'):
            fetch = fetch.replace('addi','') # remove name to expose reg numbr
            fetch = fetch.split(',')         # split regs by comma separation
            if fetch[2].startswith('0x'):
                imm = int(fetch[2],16)       # hex number check
            else:
                imm = int(fetch[2])
            Register[int(fetch[0])] = Register[int(fetch[1])] + imm
            stats.log(fetch,'addi', 4, PC) # ADDI instr, 4 cycles
            PC += 1

        elif(fetch[0:3] == 'beq'):
            fetch = fetch.replace('beq','')
            fetch = fetch.split(',')
            if fetch[2] in branchTargets:
                # get branch target int value from dict
                imm = branchTargets[fetch[2]] - PC - 1
            else:
                imm = int(fetch[2])
            stats.log(fetch,'beq', 3, PC) # BEQ instr, 3 cycles
            PC += 1
            PC = PC + imm if (Register[int(fetch[1])] == Register[int(fetch[0])]) else PC
        
        elif(fetch[0:3] == 'bne'):
            fetch = fetch.replace('bne','')
            fetch = fetch.split(',')
            if fetch[2] in branchTargets:
                # get branch target int value from dict
                imm = branchTargets[fetch[2]] - PC - 1
            else:
                imm = int(fetch[2])
            stats.log(fetch,'bne', 3, PC) # BNE instr, 3 cycles
            PC += 1
            PC = PC + imm if (Register[int(fetch[1])] != Register[int(fetch[0])]) else PC

        elif(fetch[0:3] == 'ori'):
            fetch = fetch.replace('ori','')
            fetch = fetch.split(',')
            imm = int(fetch[2])
            Register[int(fetch[0])] = Register[int(fetch[1])] | imm
            stats.log(fetch,'ori', 4, PC) # ORI instr, 4 cycles
            PC += 1

        # R-type instructions

        elif(fetch[0:4] == 'addu'):
            fetch = fetch.replace('addu','')
            fetch = fetch.split(',')
            Register[int(fetch[0])] = Register[int(fetch[1])] + Register[int(fetch[2])]
            stats.log(fetch,'addu', 4,PC)  # ADDU instr, 4 cycles
            PC += 1

        elif(fetch[0:3] == 'add'):
            fetch = fetch.replace('add','')
            fetch = fetch.split(',')
            Register[int(fetch[0])] = Register[int(fetch[1])] + Register[int(fetch[2])]
            stats.log(fetch,'add', 4,PC)  # ADD instr, 4 cycles
            PC += 1

        elif(fetch[0:3] == 'sll'):
            fetch = fetch.replace('sll','')
            fetch = fetch.split(',')
            sh = int(fetch[2])
            Register[int(fetch[0])] = Register[int(fetch[1])] << sh
            stats.log(fetch,'sll', 4,PC)  # SLL instr, 4 cycles
            PC += 1

        elif(fetch[0:4] == 'sltu'):
            fetch = fetch.replace('sltu','')
            fetch = fetch.split(',')
            Register[int(fetch[0])] = 1 if Register[int(fetch[1])] < Register[int(fetch[2])] else 0
            stats.log(fetch,'sltu', 4, PC) # SLTU instr, 4 cycles
            PC += 1

        elif(fetch[0:3] == 'slt'):
            fetch = fetch.replace('slt','')
            fetch = fetch.split(',')
            Register[int(fetch[0])] = 1 if Register[int(fetch[1])] < Register[int(fetch[2])] else 0
            stats.log(fetch,"slt", 4, PC) # SLT instr, 4 cycles
            PC += 1
        
        elif(fetch[0:3] == 'sub'):
            fetch = fetch.replace('sub','')
            fetch = fetch.split(',')
            Register[int(fetch[0])] = Register[int(fetch[1])] - Register[int(fetch[2])]
            stats.log(fetch,'sub', 4,PC)  # SUB instr, 4 cycles
            PC += 1

        elif(fetch[0:3] == 'xor'):
            fetch = fetch.replace('xor','')
            fetch = fetch.split(',')
            Register[int(fetch[0])] = Register[int(fetch[1])] ^ Register[int(fetch[2])]
            stats.log(fetch,'xor', 4,PC)  # XOR instr, 4 cycles
            PC += 1

        # Memory instructions (special I-type)

        elif(fetch[0:2] == 'lw'):
            fetch = fetch.replace('lw','')
            fetch = fetch.split(',')
            memAddr = fetch[1] # we've got rs and imm stuck together like imm(rs)
            memAddr = memAddr.split('(')
            imm = memAddr[0]
            if imm.startswith('0x'):
                imm = int(imm,16)                      # hex number check
            else:
                imm = int(imm)
            rs = memAddr[1]
            rs = rs.replace(')','')                    # remove end parentheses
            # Sanity check for word-addressing
            if ( (imm%4) != 0 ):
                print("Runtime exception: fetch address not aligned on word boundary. Exiting ")
                print("Instruction causing error:", hex(int(fetch,2)))
                exit()
            Register[int(fetch[0])] = Memory[imm + Register[int(rs)] - 8192] # Load word from memory
            stats.log(fetch,"lw", 5, PC)    # LW instr, 5 cycles
            PC += 1

        elif(fetch[0:2] == 'sw'):
            fetch = fetch.replace('sw','')
            fetch = fetch.split(',')
            memAddr = fetch[1] # we've got rs and imm stuck together like imm(rs)
            memAddr = memAddr.split('(')
            imm = memAddr[0]
            if imm.startswith('0x'):
                imm = int(imm,16)                      # hex number check
            else:
                imm = int(imm)
            rs = memAddr[1]
            rs = rs.replace(')','')                    # remove end parentheses
            # Sanity check for word-addressing
            if ( (imm%4) != 0 ):
                print("Runtime exception: fetch address not aligned on word boundary. Exiting ")
                print("Instruction causing error:", hex(int(fetch,2)))
                exit()
            Memory[imm + Register[int(rs)] - 8192] = Register[int(fetch[0])] # Store word into memory
            stats.log(fetch,"sw", 4, PC)    # SW instr, 4 cycles
            PC += 1

        else:
            print("Instruction " + str(Instructions[PC]) + " not supported. Exiting")
            break

        if(not(finished)):
            stats.prints()

    if(finished):
        stats.exitSim()
        print("\nRegisters: " + str(Register))
        print("\nMemory (beginning at offset 0x2000 and listed by word): " + str(Memory[0::4]))

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
    print('WARNING: ONLY MC CPU SIMULATOR WORKS IS CURRENTLY TESTABLE')
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
