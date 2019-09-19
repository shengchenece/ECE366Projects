# Author: Sheng Chen
# For: UIC ECE 366 Fall 2019 Project 1
# "Multiply and Fold" Hash Function

# Calculate C = H(A, B)for a given B = 0xFA19E366,
# for all the A values ranging from 1 to 100,
# and write these 100 results of C in memory starting at 0x2020.

# initialize B
lui $8, 0xFA19
ori $8, $8, 0xE366
# initialize A
addi $9, $0, 1
# initialize value of A at which main function loop should stop
addi $23, $0, 101
# initialize memory address for storing C
ori $10, $0, 0x2020
# loop for hash function data generation, stop branching when $9 == 100
loop:
# A * B
mult $9, $8
# A1 = hi XOR lo
mfhi $11
mflo $12
xor $13, $11, $12
# A1 * B
mult $13, $8
mfhi $11
mflo $12
# A2 = hi XOR lo
xor $13, $11, $12
# A2 * B
mult $13, $8
mfhi $11
mflo $12
# A3 = hi XOR lo
xor $13, $11, $12
# A3 * B
mult $13, $8
mfhi $11
mflo $12
# A4 = hi XOR lo
xor $13, $11, $12
# A4 * B
mult $13, $8
mfhi $11
mflo $12
# A5 = hi XOR lo
xor $13, $11, $12
# A5[31:16]
srl $14, $13, 16
# A5[15:0]
andi $15, $13, 0x0000FFFF
# C = A5[31:16] XOR A5[15:0]
xor $15, $14, $15
# C[15:8]
srl $16, $15, 8
# C[7:0]
andi $17, $15, 0x000000FF
# C = C[15:8] XOR C[7:0]
xor $17, $16, $17
# store C in memory
sw $17, 0($10)
# increment memory address to next word
addi $10, $10, 4
# increment A by 1
addi $9, $9, 1
# loop again with next value of A
bne $9, $23, loop
