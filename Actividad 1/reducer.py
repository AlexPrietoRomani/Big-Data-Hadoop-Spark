#!/usr/bin/env python3
import sys

def reducer():
    current_key = None
    sum_gasto = 0
    count = 0

    for line in sys.stdin:
        line = line.strip()
        key, gasto, cnt = line.split('\t')
        
        if current_key == key:
            sum_gasto += float(gasto)
            count += int(cnt)
        else:
            if current_key:
                persona, tienda = current_key.split(';')
                print(f"{persona};{tienda};{sum_gasto/count:.2f}")
            current_key = key
            sum_gasto = float(gasto)
            count = int(cnt)

    if current_key:
        persona, tienda = current_key.split(';')
        print(f"{persona};{tienda};{sum_gasto/count:.2f}")

if __name__ == "__main__":
    reducer()
