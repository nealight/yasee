# Module for the YaseeReportFile class

import pandas

class YaseeReportFileError(Exception):
    pass


class YaseeReportFile:
    def __init__(self, file_path: str):
        inter_file = pandas.ExcelFile(file_path)

        try:
            self.sheets = dict()
            for name in inter_file.sheet_names:
                self.sheets[name] = inter_file.parse(name)

        finally:
            inter_file.close()


    def __getitem__(self, item) -> pandas.DataFrame:
        return self.sheets[item]

    def getSheetNames(self) -> tuple:
        return tuple(self.sheets.keys())

    def extractColumn(self, sheet:str, column:str) -> (str,):
        return tuple(str(i).strip() for i in self.sheets[sheet][column])

    def extractRelatedColumns(self, sheet:str, *columns:str) -> ((str, ...), ...):
        return tuple(zip(*(self.extractColumn(sheet, column) for column in columns)))


