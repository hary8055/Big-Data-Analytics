#!/usr/bin/env python
import sys

def reducer():
    current_cabin_category = None
    current_sum = 0
    current_count = 0
    header_printed = False

    for line in sys.stdin:
        cabin_category, amount = line.strip().split('\t')

        try:
            amount = float(amount)
        except ValueError:
            continue 

        if current_cabin_category == cabin_category:
            current_sum += amount
            current_count += 1
        else:
            if current_cabin_category:
                if not header_printed:
                    print("CabinCategory\tAveragePrice")
                    header_printed = True

                print(f'{current_cabin_category}\t{current_sum / current_count}')

            current_cabin_category = cabin_category
            current_sum = amount
            current_count = 1

    if current_cabin_category:
        if not header_printed:
            print("CabinCategory\tAveragePrice")
        print(f'{current_cabin_category}\t{current_sum / current_count}')

if __name__ == "__main__":
    reducer()
