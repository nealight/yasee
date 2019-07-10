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
        self.yfc.storeWordFreq("FQ18", "VisitNotes", "test/WordFreqChart")
        self.assertTrue(os.path.exists("test/WordFreqChart.png"))

    def test_storeWordFreqTop20(self):
        self.yfc.storeWordFreq("FQ18", "VisitNotes", "test/WordFreqChart Top20", 20)
        self.assertTrue(os.path.exists("test/WordFreqChart Top20.png"))

    def test_addStopWords(self):
        self.yfc.addStopWords("word")
        self.yfc.storeWordFreq("FQ18", "VisitNotes", "test/WordFreqChartExcluding'word'")
        self.assertTrue(os.path.exists("test/WordFreqChartExcluding'word'.png"))

    def test_storeRelatedWordFreq(self):
        self.yfc.storeRelatedWordFreq("FQ18", "MajorID1", "VisitNotes", "research",
                                      "test/RelatedWordFreq 'research'")
        self.assertTrue(os.path.exists("test/RelatedWordFreq 'research' RELATIVE.png"))
        self.assertTrue(os.path.exists("test/RelatedWordFreq 'research' ABSOLUTE.png"))
        self.assertTrue(os.path.exists("test/RelatedWordFreq 'research'.txt"))


    def test_storeRelatedWordRootFreq(self):
        self.yfc.storeRelatedWordFreq("FQ18", "MajorID1", "VisitNotes", "re*",
                                      "test/RelatedWordRootFreq 're'")
        self.assertTrue(os.path.exists("test/RelatedWordRootFreq 're' ABSOLUTE.png"))
        self.assertTrue(os.path.exists("test/RelatedWordRootFreq 're' RELATIVE.png"))
        self.assertTrue(os.path.exists("test/RelatedWordRootFreq 're'.txt"))

    def test_storeRelatedWordSuffix(self):
        self.yfc.storeRelatedWordFreq("FQ18", "MajorID1", "VisitNotes", "*ation",
                                      "test/RelatedWordSuffixtFreq 'ation'")
        self.assertTrue(os.path.exists("test/RelatedWordSuffixtFreq 'ation' ABSOLUTE.png"))
        self.assertTrue(os.path.exists("test/RelatedWordSuffixtFreq 'ation' RELATIVE.png"))
        self.assertTrue(os.path.exists("test/RelatedWordSuffixtFreq 'ation'.txt"))

    def test_storeRelatedRECase1(self):
        self.yfc.storeRelatedWordFreq("FQ18", "MajorID1", "VisitNotes", "regex:(\w){5}",
                                      "test/RelatedRE 5-letter-word")
        self.assertTrue(os.path.exists("test/RelatedRE 5-letter-word ABSOLUTE.png"))
        self.assertTrue(os.path.exists("test/RelatedRE 5-letter-word RELATIVE.png"))
        self.assertTrue(os.path.exists("test/RelatedRE 5-letter-word.txt"))

    def test_storeRelatedRECase2(self):
        self.assertRaises(NoSearchResultsFound, self.yfc.storeRelatedWordFreq, "FQ18", "MajorID1",
                          "VisitNotes", "regex:(\w){20}", "test/RelatedRE regex:(\w){20}.png")
