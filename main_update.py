from function.package import *
from function.miscellaneous import *
from function.scrap import retrieval
from function.changebrowser import change_browser
from function.dataframe import create_data_frame
from function.map import map_function
from function.displaymap import display

# main program
value = ""

while value != "exit":
    value = input(
        "------Choose operation------"
        "\n0. Retrieve website data"
        "\n1. Create dataframe"
        "\n2. Generate map"
        "\n3. Display map"
        '\n4. Change browser'
        "\n5. Quit."
        "\nChoice: "
    )
    if value == "0":
        choices = ""
        while choices != "exit":
            file_valid = os.path.isfile(raw_output)
            if file_valid:
                choices = input(
                    "Your file is already existed. Replace it?"
                    "\n1. Replace"
                    "\n2. Keep"
                    "\nChoices: "
                )
                if choices == "1":
                    retrieval()
                    break
                elif choices == "2":
                    break
            else:
                retrieval()
                break
    elif value == "1":
        choices = ""
        while choices != "exit":
            file_valid = os.path.isfile(dataframe_output)
            if file_valid:
                choices = input(
                    "Your dataframe is already created. Create a new one?"
                    "\n1. Replace"
                    "\n2. Keep"
                    "\nChoices: "
                )
                if choices == "1":
                    create_data_frame()
                    break
                elif choices == "2":
                    break
            else:
                create_data_frame()
                break
    elif value == "2":
        choices = ""
        while choices != "exit":
            file_valid = os.path.isfile(covid_map)
            if file_valid:
                choices = input(
                    "Your map is already generated. Generate a new one?"
                    "\n1. Replace"
                    "\n2. Keep"
                    "\nChoices: "
                )
                if choices == "1":
                    map_function()
                    break
                elif choices == "2":
                    break
            else:
                map_function()
                break
    elif value == "3":
        choices = ""
        while choices != "exit":
            choices = input(
                "You will be redirected to web-based map. Continue?"
                "\n1. Continue"
                "\n2. Back"
                "\nChoices: ")
            if choices == "1":
                display()
                break
            elif choices == "2":
                break
    elif value == "4":
        change_browser()
    elif value == "5":
        break
    else:
        print("Input value is valid in range [0-->4] only!")
