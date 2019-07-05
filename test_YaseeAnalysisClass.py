import unittest
from YaseeAnalysisClass import *

class YaseeAnalysisClassTest(unittest.TestCase):
    def setUp(self):
        self.yac = YaseeAnalysisClass("test/report.xlsx")

    def test_addStopWords(self):
        self.yac.addStopWords("word")
        self.assertIn("word", self.yac.getStopWords())

    def test_FrozensetInit(self):
        yac = YaseeAnalysisClass("test/report.xlsx", frozenset(("word", "essay")))
        self.assertIn("word", yac.getStopWords())
        self.assertIn("essay", yac.getStopWords())
        self.assertNotIn("word", self.yac.getStopWords())