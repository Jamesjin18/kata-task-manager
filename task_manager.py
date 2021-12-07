from task import Task


class TaskManager:
    def __init__(self):
        self._tasks = []
    def add_task(self,task):
        self._tasks.append(task)  
    def start(self):
        print("No task yet")
        choice = input()
        while choice != "q" :
            input = self.parse_input(choice)
            
            output = ""
            print(output)
            choice = input()

    def parse_input(self,input):
        return input.split(" ",1)

    def add(self,input):
        print('add')
        tasks = self._tasks.copy()
        task = Task(input[1])
        self.add_task(task)
        tasks.append(task)
        return self._tasks == tasks

    def remove_task(self,input):
        print('remove')
        tasks = self._tasks.copy()
        for el in self._tasks:
            print(el.get_number())
            if el.get_number() == input[1] :
                self._tasks.remove(el)
        return  tasks != self._tasks

    def do_action(self,input):
        match input[0]:
            case '+':
                return self.add(input)
            case '-':
                return self.remove_task(input)
        
        
