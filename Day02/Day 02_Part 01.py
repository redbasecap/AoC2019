#!/usr/bin/env python
# coding: utf-8

with open("inputDay02.txt", "r") as f: 
    inputs = []
    #inputs = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,1,19,5,23,2,10,23,27,2,27,13,31,1,10,31,35,1,35,9,39,2,39,13,43,1,43,5,47,1,47,6,51,2,6,51,55,1,5,55,59,2,9,59,63,2,6,63,67,1,13,67,71,1,9,71,75,2,13,75,79,1,79,10,83,2,83,9,87,1,5,87,91,2,91,6,95,2,13,95,99,1,99,5,103,1,103,2,107,1,107,10,0,99,2,0,14,0]
    for number in f.read().split(","):
        inputs.append(int(number))
        
    ##Initalisation to restore the state befor "1202 program alarm"
    # before running the program, replace position 1 with the value 12 
    # and replace position 2 with the value 2.
    # What value is left at position 0 after the program halts?
    
    inputs[1] = 12
    inputs[2] = 2
    
    ##The Main programm
    pos = 0
    while(1):
        if inputs[pos] == 1:
            in1 = inputs[pos+1]
            in2 = inputs[pos+2]
            out = inputs[pos+3]
            inputs[out] = inputs[in1] + inputs[in2]

        elif inputs[pos] == 2:
            in1 = inputs[pos+1]
            in2 = inputs[pos+2]
            out = inputs[pos+3]
            inputs[out] = inputs[in1] * inputs[in2]

        elif inputs[pos] == 99:
            break
        pos += 4

    print(inputs[0])
input()