from wiki import *
from option import *

options = {
    "sites": {
        1: "wikipedia",
        2: "wiktionary",
        3: "wikisource"
    },
    "langs": {
        1: "en",
        2: "zh",
        3: "ja",
        4: "fr",
        5: "ko",
        6: "de",
        7: "es",
        8: "it",
        9: "pt"
    },
    "types": {
        1: "html",
        2: "txt",
        3: "pdf"
    }
}

if __name__ == "__main__":
    try:
        print("Select an option:")
        print("1. Get option from input")
        print("2. Get option from txt")
        option_choice = int(input("Enter an option number: "))

        if option_choice == 1:
            # Get user input for site, lang, and type
            site = get_option_from_input(options["sites"], "site")
            lang = get_option_from_input(options["langs"], "language")
            type = get_option_from_input(options["types"], "save type")
            title = input("Enter a title: ")
            get_wiki(title, site, lang, type)
            delink(title, site, lang, type)
        elif option_choice == 2:
            # Get options from txt
            file_path = input("Enter the file path: ")
            options_dict = get_option_from_txt(file_path)
            print(options_dict)
            titles = list(options_dict.keys())
            for title in titles:
                site = options["sites"][int(options_dict[title]["sites"])]
                lang = options["langs"][int(options_dict[title]["langs"])]
                type = options["types"][int(options_dict[title]["types"])]
                get_wiki(title, site, lang, type)
                delink(title, site, lang, type)
        else:
            raise ValueError("Invalid option number.")

    except ValueError as e:
        print(e)
