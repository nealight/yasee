import unittest
from YaseeFreqCharts import *
import os

class YaseeFreqChartsTest(unittest.TestCase):
    def setUp(self):
        self.yfc = YaseeFreqCharts("test/report.xlsx")

    def test_NoSearchResultsFound(self):
        self.assertRaises(NoSearchResultsFound, self.yfc.storeRelatedWordFreq, "SQ19", "MajorID1", "VisitNotes", "pre",
                                      "test/RelatedWordFreq 'pre'.png")

    def test_storeWordFreq(self):
        self.yfc.storeWordFreq("FQ18", "VisitNotes", "test/wordfreqchart.png")
        self.assertTrue(os.path.exists("test/wordfreqchart.png"))

    def test_storeWordFreqTop20(self):
        self.yfc.storeWordFreq("FQ18", "VisitNotes", "test/wordfreqchart top20.png", 20)
        self.assertTrue(os.path.exists("test/wordfreqchart top20.png"))

    def test_addStopWords(self):
        self.yfc.addStopWords("word")
        self.yfc.storeWordFreq("FQ18", "VisitNotes", "test/wordfreqcharexcluding'word'.png")
        self.assertTrue(os.path.exists("test/wordfreqcharexcluding'word'.png"))

    def test_storeRelatedWordFreq(self):
        self.yfc.storeRelatedWordFreq("FQ18", "MajorID1", "VisitNotes", "research",
                                      "test/RelatedWordFreq 'research'.png")
        self.assertTrue(os.path.exists("test/RelatedWordFreq 'research'.png"))

    def test_storeRelatedWordRootFreq(self):
        self.yfc.storeRelatedWordFreq("FQ18", "MajorID1", "VisitNotes", "re*",
                                      "test/RelatedWordRootFreq 're'.png")
        self.assertTrue(os.path.exists("test/RelatedWordRootFreq 're'.png"))

    def test_storeRelatedWordSuffix(self):
        self.yfc.storeRelatedWordFreq("FQ18", "MajorID1", "VisitNotes", "*ation",
                                      "test/RelatedWordSuffixtFreq 'ation'.png")
        self.assertTrue(os.path.exists("test/RelatedWordSuffixtFreq 'ation'.png"))

    def test_storeRelatedRECase1(self):
        self.yfc.storeRelatedWordFreq("FQ18", "MajorID1", "VisitNotes", "regex:(\w){3}",
                                      "test/RelatedRE regex:(\w){3}.png")
        self.assertTrue(os.path.exists("test/RelatedRE regex:(\w){3}.png"))

    def test_storeRelatedRECase2(self):
        self.assertRaises(NoSearchResultsFound, self.yfc.storeRelatedWordFreq, "FQ18", "MajorID1",
                          "VisitNotes", "regex:(\w){20}", "test/RelatedRE regex:(\w){20}.png")
