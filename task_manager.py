from task import Task


class TaskManager:

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

    def add_task(self,input):
        task = Task(input[1])
        return task

    def do_action(self,input):
        print(input[0])
        options = {
            "+" : self.add_task(input),
        }
        return options.get(input[0])
        
