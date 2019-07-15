import unittest
from YaseeCorrelationAnalyzer import YaseeCorrelationAnalyzer

class YaseeCorrelationAnalyzerTest(unittest.TestCase):
    def setUp(self):
        YaseeCorrelationAnalyzer("test/SampleWCReport.xlsx").storeMIs("test/MI_SCORES RESEARCH", "FQ18", "VisitNotes", "research")
        file = open("test/MI_SCORES RESEARCH.txt", 'r')
        try:
            self.MI_results = file.readlines()
        finally:
            file.close()

    def test_ZEROMISCORECALC(self):
        self.assertAlmostEqual(0, float(self.MI_results[4].split(":")[1].strip()), delta=0.001)

    def test_NONZEROMISCORECALC(self):
        self.assertNotAlmostEqual(0, float(self.MI_results[3].split(":")[1].strip()), delta=0.001)