#!/usr/bin/env python3
import sys

def combiner():
    current_cited = None
    citing_patents = []

    for line in sys.stdin:
        line = line.strip()
        cited, citing = line.split('\t')

        if current_cited == cited:
            citing_patents.append(citing)
        else:
            if current_cited:
                # Ordenamos y emitimos los resultados parciales
                citing_patents.sort()
                print(f"{current_cited}\t{','.join(citing_patents)}")
            current_cited = cited
            citing_patents = [citing]

    # No olvidemos el último grupo
    if current_cited:
        citing_patents.sort()
        print(f"{current_cited}\t{','.join(citing_patents)}")

if __name__ == "__main__":
    combiner()