#!/usr/bin/python

from mrjob.job import MRJob

'''
Create a MapReduce job which counts the number of words that begin with each letter.
That is, how many words start with 'a'? How many words start with 'b'? ...
'''
class MRStartLetterCount(MRJob):

    def mapper(self, _, line):
        words = line.split()
        for word in words:
            start_letter = word[0].lower()
            if start_letter.isalpha():
                yield start_letter, 1

    def reducer(self, key, values):
        yield key, sum(values)


if __name__ == '__main__':
    MRStartLetterCount.run()