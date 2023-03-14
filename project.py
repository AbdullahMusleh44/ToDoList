from tabulate import tabulate

def main():
    print("Welcome to the To Do List!")
    bool = True
    db = []
    counter = 0

    while bool:
        process = inputting()

        if process == "Create":
            db, counter = creating(db, counter)
        elif process == "View":
            viewing(db)
        elif process == "Update":
            db = updating(db)
        elif process == "Delete":
            db = deleting(db)
        else:
            bool = False

def inputting():
    actions = [{"Keyword": "Create", "Process": "Create a Task"},
                {"Keyword": "View", "Process": "View Tasks"},
                {"Keyword": "Update", "Process": "Update a Task"},
                {"Keyword": "Delete", "Process": "Delete a Task"},
                {"Keyword": "Exit", "Process": "Exit To Do List"}]

    while True:
        print(tabulate(actions, headers="keys", tablefmt="fancy_grid"))
        action = input("Select a process by typing a Keyword: ")

        if action in ["Create", "View", "Update", "Delete", "Exit"]:
            return action
        else:
            print("Invalid choice, please try again.")

def creating(table, c):
    task, c = input("Enter Task: "), c + 1
    table.append({"Task ID": c, "Task": task})
    return table, c

def viewing(table):
    print(tabulate(table, headers="keys", tablefmt="fancy_grid"))

def updating(table):
    numbers = list(task["Task ID"] for task in table)

    while True:
        viewing(table)
        try:
            c = int(input("Choose a task to update (enter Task ID): "))
            if c in numbers:
                break
            else:
                print("Invalid task choice, please try again: ")
        except ValueError:
            print("Invalid input")

    updated = input("Enter an updated version of the task: ")
    for task in table:
        if task["Task ID"] == c:
            task["Task"] = updated
    return table

def deleting(table):
    numbers = list(task["Task ID"] for task in table)

    while True:
        viewing(table)
        try:
            c = int(input("Choose a task to delete (enter Task ID): "))
            if c in numbers:
                break
            else:
                print("Invalid task choice, please try again:.")
        except ValueError:
            print("Invalid input, try again.")

    for i in range(len(table)):
        if table[i]["Task ID"] == c:
            del table[i]
            break

    return table


if __name__ == "__main__":
    main()



