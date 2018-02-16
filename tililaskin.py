# -*- coding: utf-8 -*-
import sys

def main():
    if (len(sys.argv) < 2):
        print("No file name specified!")
        return -1

    filename = sys.argv[1]

    try:
        infile = open(filename, "r")
    except IOError:
        print("ERROR: Unable to read the file.")
        return -1

    # Lista riveist
    lines = infile.read().splitlines()
    infile.close()

    # Remove the first line
    lines.pop(0)
    filtered = list(filter(None, lines))

    firstline = filtered[0].lower().split("\t")
    amountindex = 3
    nameindex = firstline.index("saaja/maksaja")
    # Toinen indeksin loytamistapa on for i,j in enumerate(list)

    # Remove title line
    filtered.pop(0)

    # Get amounts and names
    amounts = []
    names = []

    for l in filtered:
        l = l.split("\t")
        amounts.append(l[amountindex])
        names.append(l[nameindex])

    # Remove commas, replace with dots
    for i, a in enumerate(amounts):
        if "," in a:
            amounts[i] = a.replace(",", ".")
    sumvalue = sum(list(map(float, amounts)))
    inputname = input("Enter search term: ")

    finalsum = 0
    print("\nMäärä:\tNimi:")
    for l in filtered:
        l = l.split("\t")
        if inputname in l[nameindex].lower():
            finalsum += float(l[amountindex].replace(",", "."))
            print(l[amountindex], "\t", l[nameindex])

    print("\nYhteensä", str(finalsum), "/", str(sumvalue), "total")

main()
