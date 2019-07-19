from sklearn import metrics
from YaseeFreqCharts import YaseeFreqCharts
from functools import reduce

class YaseeCorrelationAnalyzer(YaseeFreqCharts):

    def storeMIs(self, file_name:str, sheet:str, target_column:str, target_expr:str) -> str:
        MIs = self._calcMIScores(sheet, target_column, target_expr)
        self.storeMIScoresAsTXT(MIs, file_name, target_expr)
        return self.consoleMIScores(MIs)

    def _calcMIScores(self, sheet:str, target_column:str, target_expr:str) -> dict:

        column_names:{str}=set(self.getReportFile().getColumnNames(sheet))
        column_names.remove(target_column)

        MI_dict = dict()
        for current_col in column_names:
            correlation_data = self._report_file.extractRelatedColumns(sheet, current_col, target_column)
            correlation, _, _, _ = self.calcRelatedWordFreq(correlation_data, target_expr)
            if len(correlation) != 0:
                MI_dict[current_col] = metrics.mutual_info_score([x[0] for x in correlation], [x[1] for x in correlation])

        return MI_dict

    @staticmethod
    def consoleMIScores(MI_dict:dict) -> str:
        return "\n========================================\n" \
               "You have the following columns to visualize correlation, ranked by their " \
               "respective Mutual Information Scores.\n" + \
               reduce(YaseeCorrelationAnalyzer.combine_as_lines,
                      (reduce(YaseeCorrelationAnalyzer.combine_as_entry, entry) for entry in sorted(MI_dict.items(), key=lambda x: -x[1]))) + \
               "\n========================================\n"


    @staticmethod
    def storeMIScoresAsTXT(MI_dict:dict, file_name:str, target_expr:str) -> None:
        file = open((file_name + ".txt") if (".txt" not in file_name) else file_name, 'w')

        try:
            file.write(f'"{target_expr.upper()}" Mutual Information Scores with respect to:\n\n\n')
            file.write(reduce(YaseeCorrelationAnalyzer.combine_as_lines, (reduce(YaseeCorrelationAnalyzer.combine_as_entry, entry) for entry in
                                                 sorted(MI_dict.items(), key=lambda x: -x[1]))))

        finally:
            file.close()