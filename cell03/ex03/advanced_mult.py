#!/usr/bin/env python3
num = 0
while num <= 10:
    
    i = 0
    print(f"Table de {num}: ", end="")
    while i <= 10:
        
        print(num * i, end=" ")
        i += 1
    
    print()
    num += 1