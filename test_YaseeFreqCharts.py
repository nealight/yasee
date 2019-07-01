import unittest
from YaseeFreqCharts import YaseeFreqCharts
import os

class YaseeFreqChartsTest(unittest.TestCase):
    def setUp(self):
        self.yfc = YaseeFreqCharts("test/report.xlsx")

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