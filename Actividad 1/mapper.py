#!/usr/bin/env python3
import sys

def mapper():
    for line in sys.stdin:
        line = line.strip()
        persona, tienda, gasto = line.split(';')
        print(f"{persona};{tienda}\t{gasto}\t1")

if __name__ == "__main__":
    mapper()
