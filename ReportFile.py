# Module for the ReportFile class

import pandas

class ReportFileError(Exception):
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


    def __getitem__(self, item) -> pandas.core.frame.DataFrame:
        return self.sheets[item]

    def get_sheet_names(self) -> tuple:
        return tuple(self.sheets.keys())


    def extract_column(self, sheet:str, column:str) -> (str,):
        return tuple(str(i).strip() for i in self.sheets[sheet][column])



