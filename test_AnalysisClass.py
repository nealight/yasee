import unittest
from YaseeAnalysisClass import *

class YaseeAnalysisClassTest(unittest.TestCase):
    def setUp(self):
        self.yac = YaseeAnalysisClass("test/report.xlsx")

    def test_addStopWords(self):
        self.yac.addStopWords("word")
        self.assertIn("word", self.yac.getStopWords())