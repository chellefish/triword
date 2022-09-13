'''
get_wordsets.py

This is an algorithm that generates all the word sets to be used in
triword.

Heap's algorithm for permutations is adapted.

'''
'''
Function: getWordSets
Params: fileName
Returns: None
Scope: Takes the name of the file with word bank and returns all permutations
that fit the following requirements:

(1) word 1 and word 2 must begin with the same letter
(2) word 3 must begin with the last letter of word 1
(3) word 3 must end with the last letter of word 2

'''
from typing import List
class GetWordSets:
    def __init__(self, fileName):
        self.fileName = fileName
        #self.tempSets = []
        self.sets = set()
        self.dict = {}

    def getWords(self) -> None:
        try:
            with open(self.fileName, "r") as words:
                print("Grabbing word bank...")
                for w in words:
                    w = w.strip()
                    if w[0] in self.dict:
                        self.dict[w[0]].append(w)
                    else:
                        self.dict[w[0]] = [w]
                print("Converted word bank to a dictionary...")
        except:
            print("File not found. Try again. \n")

    def getFirstTwoWords(self, letterArr, temp, start, end, k):

        if k == 0:
            self.tempSets.append(temp)
            #print(temp)
            return self.tempSets
        for i in range(start, end):
            temp.append(letterArr[i])
            self.tempSets = self.getFirstTwoWords(letterArr, temp, start + 1, end, k - 1)
            temp.pop()


    def getThirdWord(self, set) -> None:
        firstLetter = set[0][0]
        lastLetter = set[1][3]
        for word in self.dict[firstLetter]:
            if word[3] == lastLetter:
                self.sets.add(set + [word])

    def main(self) -> None:
        self.getWords()
        print("Creating sets...")
        for letter in self.dict:
            start, end = 0, len(self.dict[letter])
            temp = []
            self.tempSets = self.getFirstTwoWords(self.dict[letter], temp, start, end, 2)
        print(self.tempSets)
        for set in self.tempSets:
            self.getThirdWord(set)

        #makeSets(len(wordBank) - 1, 0, 3)
        #print(sets)
        wordSetFile = open("word_sets.txt", "a")
        #for set in sets:
        #    print(set)
        #    wordSetFile.write(set + "\n")
test = GetWordSets("word_bank.txt")
test.main()
