from YaseeWordCloud import YaseeWordCloud


class Console:
    def __call__(self, *args, **kwargs):
        while True:
            user_prompt = input().strip().lower()
            if user_prompt in frozenset(("seeya", "see you")):
                break

            if user_prompt == "generate word cloud":
                print("Where is your file?")
                target_file_path = input().strip()
                print("Which excel sheet to analyze?")
                target_sheet = input().strip()
                print("Which excel column inside that sheet to analyze?")
                target_column = input().strip()

                word_cloud = YaseeWordCloud(path=target_file_path, sheet=target_sheet, column=target_column)

                print("What would be the name of your cloud?")
                output_path = input().strip()
                word_cloud.store_wordcloud(output_path)


if __name__ == "__main__":
    console = Console()
    console()