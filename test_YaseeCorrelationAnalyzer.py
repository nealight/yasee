import unittest
from YaseeCorrelationAnalyzer import YaseeCorrelationAnalyzer

class YaseeCorrelationAnalyzerTest(unittest.TestCase):
    def setUp(self):
        file_path = "test/MI_SCORES 'RESEARCH'.txt"
        YaseeCorrelationAnalyzer("test/SampleWCReport.xlsx").storeMIs(file_path, "FQ18", "VisitNotes", "research")
        file = open(file_path, 'r')
        try:
            self.MI_results = file.readlines()
        finally:
            file.close()

    def test_ZEROMISCORECALC(self):
        self.assertAlmostEqual(0, float(self.MI_results[4].split(":")[1].strip()), delta=0.001)

    def test_NONZEROMISCORECALC(self):
        self.assertNotAlmostEqual(0, float(self.MI_results[3].split(":")[1].strip()), delta=0.001)