def change_browser():
    with open("browser/browser.log", "r", encoding="utf8") as number:
        browser = number.readline()

    current_browser = ""

    dict_browser = {1: "Chrome", 2: "Edge", 3: "Firefox"}

    if browser == "1":
        current_browser = dict_browser.get(1)
    elif browser == "2":
        current_browser = dict_browser.get(2)
    elif browser == "3":
        current_browser = dict_browser.get(3)

    options = ["1", "2"]
    choice = ""
    while choice != "exit":
        if choice not in options:
            choice = input(
                "Your current browser is: " + current_browser + ". Do you want to change it?"
                "\n1. Keep current browser choice"
                "\n2. Choose a new browser"
                "\nChoice: "
                )
        if choice == "1":
            break
        elif choice == "2":
            browser = input(
                "Enter number of your browser: "
                "\n1. Chrome"
                "\n2. Edge"
                "\n3. Firefox"
                "\nYour choice: "
            )
            with open("browser/browser.log", "w", encoding="utf8") as number:
                number.write(browser)
            print("*Set " + dict_browser.get(int(browser)) + " as default browser!*")
            break
