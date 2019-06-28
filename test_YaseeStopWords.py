import unittest
from YaseeStopWords import YaseeStopWords

class YaseeStopWordsTest(unittest.TestCase):
    def test_default_init(self):
        ysw = YaseeStopWords()
        self.assertTrue("a" in ysw)

    def test_replace_init(self):
        ysw = YaseeStopWords(stopwords=frozenset(("UCI",)), replace=True)
        self.assertFalse("a" in ysw)
        self.assertTrue("UCI" in ysw)

    def test_addon_init(self):
        ysw = YaseeStopWords(stopwords=frozenset(("UCI",)))
        self.assertTrue("a" in ysw)
        self.assertTrue("UCI" in ysw)

    def test_getStopWords(self):
        ysw = YaseeStopWords(stopwords=frozenset(("UCI",)), replace=True)
        self.assertTrue(ysw.get_stopwords() == frozenset(("UCI",)))

    def test_addStopWords(self):
        ysw = YaseeStopWords(stopwords=frozenset(("UCI",)), replace=True)
        ysw.add_stopwords(("UCLA", "UCSD"))
        self.assertTrue(ysw.get_stopwords() == frozenset(("UCI", "UCLA", "UCSD")))

        ysw.add_stopwords("UCSB")
        self.assertTrue(ysw.get_stopwords() == frozenset(("UCI", "UCLA", "UCSD", "UCSB")))