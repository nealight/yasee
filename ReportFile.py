""" Module for the ReportFile class """
import pandas

class ReportFileError(Exception):
    pass

class NotWCReport(ReportFileError):
    pass


class ReportFile:
    def __init__(self, file_path: str, is_wcreport: bool=True):
        self.is_wcreport = is_wcreport

        inter_file = pandas.ExcelFile(file_path)

        try:
            self.sheets = dict()
            for name in inter_file.sheet_names:
                self.sheets[name] = inter_file.parse(name)

        finally:
            inter_file.close()


    def __getitem__(self, item):
        return self.sheets[item]


    def get_visitNotes(self, quarter: str):
        """Only applicable to UC Irvine Writing Center report files."""

        """Returns a tuple of visit notes, stripped of any other info."""
        if not self.is_wcreport:
            raise NotWCReport

        return tuple(i for i in self.sheets[quarter]["VisitNotes"])




