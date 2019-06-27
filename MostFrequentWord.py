from mrjob.job import MRJob
from mrjob.step import MRStep
import re

WORD_RE = re.compile(r"[\w']+")
TOP_LENGTH = 10

class MRMostFrequentWord(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_words,
                   combiner=self.combiner_count_words,
                   reducer=self.reducer_count_words),
            MRStep(reducer=self.reducer_find_max_word)
        ]

    def mapper_get_words(self, _, line):
        # yield each word in the line
        for word in WORD_RE.findall(line):
            yield word.lower(), 1

    def combiner_count_words(self, word, counts):
        # optimization: sum the words we've seen so far
        yield (sum(counts), word)

    def reducer_count_words(self, word, counts):
        # send all (num_occurrences, word) pairs to the same reducer.
        yield None, (sum(counts), word)

    # discard the key; it is just None
    def reducer_find_max_word(self, _, word_count_pairs):
        # top 10 words by number of occurrences
        cnt = 0
        for wp in sorted(word_count_pairs, reverse=True):
            if cnt==TOP_LENGTH:
                break
            else:
                cnt += 1
                yield wp[1], wp[0]

if __name__ == '__main__':
    MRMostFrequentWord.run()
    
    
