from Trie import Trie
import csv


def read_csv(filename):
    theFile = open(filename, "r")
    theReader = csv.reader(theFile, dialect='excel')
    table = []
    for row in theReader:
        if(len(row) > 0):
            table.append(row[0])
    theFile.close()
    return table

content = read_csv("wordsforproblem.txt")
trie = Trie()
for word in content:
    trie.Insert(word)
