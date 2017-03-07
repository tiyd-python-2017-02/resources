def get_int_from_user(lower=float("-inf"), upper=float("inf")):
    while True:
        user_input = input("enter an integer ")
        try:
            if lower <= int(user_input) <= upper:
                return int(user_input)
            else:
                print("please enter an integer between {} and {}".format(lower, upper))
        except:
            print("that was not an integer, try again")


class Task:
    def __init__(self, description, priority=0):
        self.description = description
        self.priority = priority
    
    def __repr__(self):
        return self.description
    
class TodoList:
    def __init__(self, filename="task_list.txt"):
        self.task_list = []
        self.filename = filename
        self.is_dirty = False
        self.load()

    def add(self, task):
        self.task_list.append(task)
        self.is_dirty = True
        
    def remove(self):
        for i, task in enumerate(self.task_list):
            print(i, task)
        who = get_int_from_user(0, len(self.task_list))
        self.task_list.pop(who)
        self.task_list[who].complete = True
        self.is_dirty = True
    
    def __repr__(self):
        return str(self.task_list)
    
    def __len__(self):
        return len(self.task_list)
    
    def save(self):
        with open(self.filename, "w") as f:
            for task in self.task_list:
                f.write(str(task))
                f.write("\n")

        self.is_dirty = False
                
    def load(self):
        self.task_list = []
        if self.is_dirty:
            user_input = input("you are about to lose existing data, are you sure? ")
            if user_input.lower()[0] != "y":
                return
        with open(self.filename, "r") as f:
            for line in f:
                self.add(Task(line.strip()))
        self.is_dirty = False
    
    def display(self):
        for id, task in enumerate(self.task_list):
            if not task.complete:
                print(id, task)


if __name__ == "__main__":
    t = TodoList("test.txt")
    user_choice = input("what would you like to do? ")
    while user_choice.lower()[0] != "q":
        t.display()
        if user_choice == "a":
            t.add(Task(input("what is the task? ")))
        elif user_choice == "r":
            t.remove()
        elif user_choice == "s":
            t.save()
        elif user_choice == "l":
            t.load()
        
        user_choice = input("what would you like to do? ")

    if t.is_dirty:
        user_choice = input("would you like to save your changes? ")
        if user_choice == "y":
            t.save()




