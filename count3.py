#!/usr/bin/python

from mrjob.job import MRJob

'''
Create a MapReduce job which counts the number of 3-letter words in a file.
'''
class MR3Count(MRJob):

    def mapper(self, _, line):
        words = line.split()
        for word in words:
            yield len(word), 1

    def reducer(self, key, values):
        if key == 3:
            yield "3-letter", sum(values)


if __name__ == '__main__':
    MR3Count.run()