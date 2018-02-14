#!/usr/bin/python

from mrjob.job import MRJob

'''
Create a MapReduce job which counts the total number of words in a file.
'''
class MRWordCount(MRJob):

    def mapper(self, _, line):
        yield "words", len(line.split())

    def reducer(self, key, values):
        yield key, sum(values)


if __name__ == '__main__':
    MRWordCount.run()