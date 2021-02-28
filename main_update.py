from function.packages import *
from function.config import *
from function.retrieval import retrieval
from function.changebrowser import change_browser

# main program
value = ""

while value != "exit":
    value = input(
        "Choose operation"
        "\n0. Retrieve website data"
        "\n1. Create dataframe"
        '\n2. Generate map'
        '\n3. Change browser'
        "\n4. Quit."
        "\nChoice: "
    )
    if value == "0":
        choices = ""
        while choices != "exit":
            file_valid = os.path.isfile(output)
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
    elif value == "1":
        break
    elif value == "2":
        change_browser()
    elif value == "3":
        break
    else:
        print("Input value is valid in range [0-->3] only!")

