#!/usr/bin/env python3
import sys

def combiner():
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
                # Emitimos la suma parcial y el conteo
                print(f"{current_key}\t{sum_gasto}\t{count}")
            current_key = key
            sum_gasto = float(gasto)
            count = int(cnt)

    if current_key:
        # No olvidemos el último grupo
        print(f"{current_key}\t{sum_gasto}\t{count}")

if __name__ == "__main__":
    combiner()
