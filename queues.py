class Queues:
    def __init__(self, processes):
        self.priority0 = []
        self.priority1 = []
        self.priority2 = []
        self.priority3 = []
        self.processes = processes.copy()
        self.max = 1000

    def create_queues(self, process):
        if process[2] == 0:
            self.priority0.append(process[0])
            self.max-=1
        elif process[2] == 1:
            self.priority1.append(process[0])
            self.max-=1
        elif process[2] == 2:
            self.priority2.append(process[0])
            self.max-=1
        elif process[2] == 3:
            self.priority3.append(process[0])
            self.max-=1
        
    def update_priorities(self, exec_time):
        for p in self.priority2:
            if(exec_time - self.processes[p][3] > 10):
                self.priority1.append(self.processes[p])
                self.priority2.remove(p)
        for p in self.priority3:
            if(exec_time - self.processes[p][3] > 10):
                self.priority2.append(self.processes[p])
                self.priority3.remove(p)