# Write-up



## Introduction

The goal of the challenge is to understand how the program encrypted the file "enc.txt" and to decrypt it.

`Flag: dvCTF{7dae459ccb4a436757f486be2e9d69730451b6e4eeae1fe8e118a53269ac5847}`

## Solution

The program is very simple. It takes one input that will be xored with a key and the output is stored in a file. The key is generated with rand() and the starting seed value is set to the current timestamp. To decrypt the file, you just need to get the "Modified Date" of the file "enc.txt" and understand how the input is xored.