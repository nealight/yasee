from YaseeWordCloud import YaseeWordCloud
from YaseeFreqCharts import YaseeFreqCharts


def init_analysis_class(analysis_class:type) -> "type()":
    print("Where is your file?")
    target_file_path = input().strip()
    return analysis_class(path=target_file_path)


class Console():
    def __call__(self, *args, **kwargs):
        while True:
            print("Hi! You have the following options\n"
                  "a) word cloud\n"
                  "b) word freq chart\n"
                  "q) quit\n", end="")
            user_prompt = input().strip().lower()
            if (user_prompt in ("seeya", "see you", "quit", "q")):
                break

            if (user_prompt in ("a", "word cloud")):
                word_cloud:YaseeWordCloud = init_analysis_class(YaseeWordCloud)

                print("Which excel sheet to analyze?")
                target_sheet = input().strip()
                print("Which excel column inside that sheet to analyze?")
                target_column = input().strip()

                print("What would be the name of your analysis file?")
                output_path = input().strip()
                word_cloud.store(target_sheet, target_column, output_path)

            if (user_prompt in ("b", "word freq chart")):
                word_freq_chart:YaseeFreqCharts = init_analysis_class(YaseeFreqCharts)

                print("Which excel sheet to analyze?")
                target_sheet = input().strip()
                print("Which excel column inside that sheet to analyze?")
                target_column = input().strip()

                print("What would be the name of your analysis file?")
                output_path = input().strip()
                print("How many results do you want to see?")
                result_num = int(input().strip())

                word_freq_chart.storeWordFreq(target_sheet, target_column, output_path, result_num)




if __name__ == "__main__":
    Console()()
