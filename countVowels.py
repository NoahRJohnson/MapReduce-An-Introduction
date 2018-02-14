#!/usr/bin/python

from mrjob.job import MRJob

'''
Create a MapReduce job which, for each possible word length, computes the average
number of vowels in the word. That is, words with 4 letters typically have how many
vowels? Words with 5 letters typically have how many vowels?
'''
class MR3Count(MRJob):

    def mapper(self, _, line):
        words = line.split()
        for word in words:
            numVowels = sum(map(word.lower().count, "aeiou"))
            yield len(word), numVowels

    def reducer(self, key, values):
        totalVowels = 0
        n = 0
        
        for numVowels in values:
            totalVowels += numVowels
            n += 1
            
        yield key, round(float(totalVowels) / n, 2) # 2 decimal places


if __name__ == '__main__':
    MR3Count.run()