class Task :
    count = 0
    def __init__(self,desc):
        self._description = desc
        self._number = Task.count + 1
        self._status = "to do"
        Task.count = Task.count + 1
    
    def get_description(self):
        return self._description
    def set_description(self, x):
        self._description = x

    def get_number(self):
        return self._number
    def set_number(self, x):
        self._number = x
    
    def get_status(self):
        return self._status
    def set_status(self, x):
        self._status = x