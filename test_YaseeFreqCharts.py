import unittest
from YaseeFreqCharts import YaseeFreqCharts
import os

class YaseeFreqChartsTest(unittest.TestCase):
    def setUp(self):
        self.yfc = YaseeFreqCharts("test/report.xlsx", "FQ18", "VisitNotes")

    def test_storeWordFreq(self):
        self.yfc = YaseeFreqCharts("test/report.xlsx", "FQ18", "VisitNotes")
        self.yfc.storeWordFreq("test/wordfreqchart.png")
        self.assertTrue(os.path.exists("test/wordfreqchart.png"))

    def test_addStopWords(self):
        self.yfc.addStopWords("word")
        self.yfc.storeWordFreq("test/wordfreqcharexcluding'word'.png")
        self.assertTrue(os.path.exists("test/wordfreqcharexcluding'word'.png"))