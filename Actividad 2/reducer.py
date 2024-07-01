#!/usr/bin/env python3
import sys

def reducer():
    current_cited = None
    all_citing_patents = set()

    for line in sys.stdin:
        line = line.strip()
        cited, citing_list = line.split('\t')
        citing_patents = set(citing_list.split(','))

        if current_cited == cited:
            all_citing_patents.update(citing_patents)
        else:
            if current_cited:
                # Ordenamos y emitimos los resultados finales
                sorted_citing = sorted(all_citing_patents)
                print(f"{current_cited}\t{','.join(sorted_citing)}")
            current_cited = cited
            all_citing_patents = citing_patents

    # No olvidemos el último grupo
    if current_cited:
        sorted_citing = sorted(all_citing_patents)
        print(f"{current_cited}\t{','.join(sorted_citing)}")

if __name__ == "__main__":
    reducer()