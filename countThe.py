#!/usr/bin/python

from mrjob.job import MRJob

'''
Create a MapReduce job which counts the number of times "the" appears in a file.
'''
class MRTheCount(MRJob):

    def mapper(self, _, line):
        words = line.split()
        for word in words:
            yield word.lower(), 1
            
    def reducer(self, key, values):
        if key == "the":
            yield key, sum(values)


if __name__ == '__main__':
    MRTheCount.run()