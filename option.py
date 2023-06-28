def get_option_from_input(options_dict, option_name):
    print(f"Select a {option_name}:")
    for key, value in options_dict.items():
        print(f"{key}. {value}")
    choice = int(input("Enter an option number: "))
    if choice not in options_dict:
        raise ValueError("Invalid option number.")
    return options_dict[choice]


def get_option_from_txt(file_path):
    options_dict = {}
    with open(file_path, "r") as file:
        lines = file.readlines()
        headers = lines[0].strip().split()
        for line in lines[1:]:
            data_line = line.strip().split()
            title = data_line[-1]
            options = {}
            for header, value in zip(headers[:-1], data_line[:-1]):
                options[header] = value
            options_dict[title] = options
    return options_dict
