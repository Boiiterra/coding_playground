print("Now I am gonna create some dictionaries")


def stop():
    global process
    process = False
    print("stopped")


def add():
    while True:
        print("creating new element:")
        key = input("key -> ")
        value = input("value -> ")
        dictionary[f"{key}"] = f"{value}"
        yn = input("Do you want to add more elements?")
        if yn[0].lower() == "y":
            print("\n")
        elif yn[0].lower() == "n":
            break
        else:
            print("Something went wrong. Process stopped.\n")
            break


def remove():
    while True:
        print("Deleting element:")
        key = input("key -> ")
        del dictionary[f"{key}"]
        yn = input("Do you want to delete more elements? (y/n) ")
        if yn[0].lower() == "y":
            print("\n")
        elif yn[0].lower() == "n":
            break
        else:
            print("Something went wrong. Process stopped.\n")
            break


def show():
    print(dictionary)


dictionary = {}

process = True
print("started")

while process:
    _input = input("Command -> ")

    if _input == "add_el":
        add()
    elif _input == "help":
        print("Stop script: stop")
        print("Add new element to dictionary: add_el")
        print("Remove element from dictionary: remove_el")
        print("Show dictionary: show_dict")
    elif _input == "remove_el":
        remove()
    elif _input == "stop":
        stop()
    elif _input == "show_dict":
        show()
