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
# main loop for hash function operations, branch out when $9 == 100
loop:
# A * B
mult $8, $9
# A1 = hi XOR lo
mfhi $11
mflo $12
xor $13, $11, $12
# store A1 (soon to be C) in memory
sw $13, 0($10)
# increment memory address to next word
addi $10, $10, 4
# increment A by 1
addi $9, $9, 1
bne $9, $23, loop
