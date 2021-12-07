class TaskManager:

    def add_task(self,task):
        self._tasks.append(task)    

    def parse_input(self,input):
        return input.split(" ",1)

