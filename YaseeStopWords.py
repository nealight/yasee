# This class provides a layer of conversion between Frozenset and Set.
#
# You can also specify whether to use the standard UC Irvine Writing
# Center stop words.


STOPWORDS = {'a',
 'about',
 'above',
 'after',
 'again',
 'against',
 'all',
 'also',
 'am',
 'an',
 'and',
 'any',
 'are',
 "aren't",
 'as',
 'at',
 'be',
 'because',
 'been',
 'before',
 'being',
 'below',
 'between',
 'both',
 'but',
 'by',
 'can',
 "can't",
 'cannot',
 'com',
 'could',
 "couldn't",
 'did',
 "didn't",
 'do',
 'does',
 "doesn't",
 'doing',
 "don't",
 'down',
 'during',
 'each',
 'else',
 'ever',
 'few',
 'for',
 'from',
 'further',
 'get',
 'had',
 "hadn't",
 'has',
 "hasn't",
 'have',
 "haven't",
 'having',
 'he',
 "he'd",
 "he'll",
 "he's",
 'her',
 'here',
 "here's",
 'hers',
 'herself',
 'him',
 'himself',
 'his',
 'how',
 "how's",
 'however',
 'http',
 'i',
 "i'd",
 "i'll",
 "i'm",
 "i've",
 'if',
 'in',
 'into',
 'is',
 "isn't",
 'it',
 "it's",
 'its',
 'itself',
 'just',
 'k',
 "let's",
 'like',
 'me',
 'more',
 'most',
 "mustn't",
 'my',
 'myself',
 'no',
 'nor',
 'not',
 'of',
 'off',
 'on',
 'once',
 'only',
 'or',
 'other',
 'otherwise',
 'ought',
 'our',
 'ours',
 'ourselves',
 'out',
 'over',
 'own',
 'r',
 'same',
 'shall',
 "shan't",
 'she',
 "she'd",
 "she'll",
 "she's",
 'should',
 "shouldn't",
 'since',
 'so',
 'some',
 'such',
 'than',
 'that',
 "that's",
 'the',
 'their',
 'theirs',
 'them',
 'themselves',
 'then',
 'there',
 "there's",
 'these',
 'they',
 "they'd",
 "they'll",
 "they're",
 "they've",
 'this',
 'those',
 'through',
 'to',
 'too',
 'under',
 'until',
 'up',
 'very',
 'was',
 "wasn't",
 'we',
 "we'd",
 "we'll",
 "we're",
 "we've",
 'were',
 "weren't",
 'what',
 "what's",
 'when',
 "when's",
 'where',
 "where's",
 'which',
 'while',
 'who',
 "who's",
 'whom',
 'why',
 "why's",
 'with',
 "won't",
 'would',
 "wouldn't",
 'www',
 'you',
 "you'd",
 "you'll",
 "you're",
 "you've",
 'your',
 'yours',
 'yourself',
 'yourselves'}


from UCIWC_DEFAULTSTOPWORDS import UCIWC_DEFAULTSTOPWORDS


class YaseeStopWords():
    DEFAULT_STOPWORDS = STOPWORDS.union(UCIWC_DEFAULTSTOPWORDS)

    def __init__(self, stopwords:frozenset=None, replace:bool=False):
        if (stopwords == None):
            self.stopwords = set(YaseeStopWords.DEFAULT_STOPWORDS)
        else:
            if replace:
                self.stopwords = set(stopwords.__iter__())
            else:

                self.stopwords = set(YaseeStopWords.DEFAULT_STOPWORDS)
                for x in stopwords:
                    self.stopwords.add(x)

    def getStopwords(self) -> frozenset:
        return frozenset(self.stopwords.__iter__())

    def addStopwords(self, item: str or iter=None):
        if item == None:
            return
        elif type(item) == str:
            self.stopwords.add(item)
        else:
            for x in item:
                self.stopwords.add(x)

    def __contains__(self, item):
        return item in self.stopwords

    def __iter__(self):
        return self.stopwords.__iter__()


