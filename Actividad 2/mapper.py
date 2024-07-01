#!/usr/bin/env python3
import sys

def mapper():
    # Saltamos la primera línea (cabecera)
    next(sys.stdin)
    
    for line in sys.stdin:
        line = line.strip()
        if line:
            citing, cited = line.split(',')
            # Invertimos el orden para tener cited como clave
            print(f"{cited}\t{citing}")

if __name__ == "__main__":
    mapper()