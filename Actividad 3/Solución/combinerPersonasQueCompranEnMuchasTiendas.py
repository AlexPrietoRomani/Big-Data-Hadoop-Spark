#!/usr/bin/env python3

import sys

def combiner():
    subproblema = None
    tiendas = set()

    for claveValor in sys.stdin:
        cliente, tienda = claveValor.strip().split("\t", 1)

        if subproblema == None:
            subproblema = cliente

        if subproblema == cliente:
            tiendas.add(tienda)    

        else:
            for tiendaVisitada in tiendas:
                print("%s\t%s" % (subproblema, tiendaVisitada))

            subproblema = cliente
            tiendas = set()
            tiendas.add(tienda)

    # Emitir las tiendas del último cliente
    for tiendaVisitada in tiendas:
        print("%s\t%s" % (subproblema, tiendaVisitada))

if __name__ == "__main__":
    combiner()