#!/usr/bin/python3
    
import sys

def reducer():
    subproblema = None
    tiendas = set()

    for claveValor in sys.stdin:
        cliente, tienda = claveValor.strip().split("\t", 1)

        if subproblema == None:
            subproblema = cliente

        if subproblema == cliente:
            tiendas.add(tienda)
        else:
            if len(tiendas) >= 3:
                print("%s" % (subproblema))

            subproblema = cliente
            tiendas = set()
            tiendas.add(tienda)

    if len(tiendas) >= 3:
        print("%s" % (subproblema))

if __name__ == "__main__":
    reducer()
