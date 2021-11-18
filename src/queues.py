class Queues:
    def __init__(self):
        self.priority0 = []
        self.priority1 = []
        self.priority2 = []
        self.priority3 = []
        self.max = 1000 # variable used to check the total number of processes in queues

    # inserts procees into the corresponding priority queue
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

    # print queues, use for debug
    def print_queues(self, exec_time):
        print("exec_time: {}".format(exec_time))
        print("p0:")
        print(self.priority0)
        print("p1:")
        print(self.priority1)
        print("p2:")
        print(self.priority2)
        print("p3:")
        print(self.priority3)

    # removes the processes with processor time equal to 0
    def finish_processes(self, memory, processes):
        for p in self.priority0:
            if(processes[p][3] == 0):
                memory.free_memory(processes[p])
                self.priority0.remove(p)
                self.max+=1
        for p in self.priority1:    
            if(processes[p][3] == 0):
                memory.free_memory(processes[p])
                self.priority1.remove(p)
                self.max+=1
        for p in self.priority2:    
            if(processes[p][3] == 0):
                memory.free_memory(processes[p])
                self.priority2.remove(p)
                self.max+=1
        for p in self.priority3:    
            if(processes[p][3] == 0):
                memory.free_memory(processes[p])
                self.priority3.remove(p)
                self.max+=1

    # removes the process at the start of the queues and moves it to the end
    # does not apply to priority 0, which ia FIFO queue
    def update_positions(self, prio):
        if(len(self.priority1)>1 and prio == 1):
            process = self.priority1.pop(0)
            self.priority1.append(process)
        if(len(self.priority2)>1 and prio == 2):
            process = self.priority2.pop(0)
            self.priority2.append(process)
        if(len(self.priority3)>1 and prio == 3):
            process = self.priority3.pop(0)
            self.priority3.append(process)

    # processes that have not been executed for 10 quantum have their priority increased
    # does not apply for processes with priority 0 or 1
    def update_priorities(self, exec_time, processes):
        for p in self.priority2:
            if(exec_time - processes[p][1] > 10):
                processes[p][1] = exec_time
                self.priority1.append(p)
                self.priority2.remove(p)
        for p in self.priority3:
            if(exec_time - processes[p][1] > 10):
                processes[p][1] = exec_time
                self.priority2.append(p)
                self.priority3.remove(p)