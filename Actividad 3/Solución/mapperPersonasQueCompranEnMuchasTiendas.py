#!/usr/bin/env python3
import sys

def mapper():
    for linea in sys.stdin:
        linea = linea.strip()
        if linea:
            try:
                cliente, tienda = linea.split("\t", 1)
                print(f"{cliente}\t{tienda}")
            except ValueError:

                continue

if __name__ == "__main__":
    mapper()