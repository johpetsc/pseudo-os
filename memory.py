SIZE = 1024

class Memory:
    def __init__(self):
        self.mem = [None] * SIZE
        self.free_real = 64
        self.free_user = 960

    def allocate_memory(self, process):
        if(process[2]):
            if(process[4] <= self.free_real):
                for x in range(64, SIZE):
                    if(self.mem[x] == None):
                        process[4] -= 1
                        self.free_real -= 1
                        self.mem[x] = process[0]
                        if(process[4] == 0):
                            break
        else:
            if(process[4] <= self.free_user):
                for x in range(0, 64):
                    if(self.mem[x] == None):
                        process[4] -= 1
                        self.free_user -= 1
                        self.mem[x] = process[0]
                        if(process[4] == 0):
                            break

    def free_memory(self, process):
        for x in range(0, SIZE):
            if(self.mem[x] == process[1]):
                self.mem[x] = None
