from collections.abc import Sequence

class ProcessList(Sequence):
    def __init__(self, filepath) -> None:
        self.list = []
        self.PID = 0

        with open(filepath, 'r') as f:
            for line in f:
                self.list.append(list(map(int, line.split(','))))
        
        # inserts the process PID at the start and number of executed instruction at the end
        for process in self.list:
            process.insert(0, self.PID)
            process.append(1)
            self.PID+=1
        
        super().__init__()
    
    def get_process(self, index) -> list:
        return self.list[index]

    # initializes the process
    def init_process(self, index, offset):
        print("    PID: {}".format(self.list[index][0]))
        print("    offset: {}".format(offset))
        print("    blocks: {}".format(self.list[index][4]))
        print("    priority: {}".format(self.list[index][2]))
        print("    time: {}".format(self.list[index][3]))
        if(self.list[index][5] > 1):
            self.list[index][5] = 1
        print("    printers: {}".format(self.list[index][5]))
        print("    scanners: {}".format(self.list[index][6]))
        print("    modems: {}".format(self.list[index][7]))
        if(self.list[index][8] > 1):
            self.list[index][8] = 1
        print("    drivers: {}\n".format(self.list[index][8]))

    # executes a process instruction
    def exec_process(self, index):
        if(self.list[index][9] == 1): # checks if first instruction
            print("process {}".format(self.list[index][0]))
        print("P{} instruction {}".format(self.list[index][0], self.list[index][9]))
        self.list[index][9]+=1
        self.list[index][3]-=1
        if(self.list[index][3] == 0): # checks if last instruction
            print("P{} return SIGINT\n".format(self.list[index][0]))

    def __getitem__(self, index) -> list:
        return self.list[index]
    
    def __len__(self) -> int:
        return len(self.list)
