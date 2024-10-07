#!/usr/bin/env python
import sys

def mapper():
    for line in sys.stdin:
        # Split the input line 
        fields = line.strip().split(',')

        if len(fields) != 11:
            continue 

        cabin_category = fields[2]  # CabinCategory 
        total_amount = fields[9]    # TotalAmount 

        try:
            print(f'{cabin_category}\t{float(total_amount)}')
        except ValueError:
            continue 

if __name__ == "__main__":
    mapper()
