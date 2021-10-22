SIZE = 1024

class Memory:
    def __init__(self):
        self.mem = [None] * SIZE

    # aloca os blocos de memória contiguos de um processo
    # se não houver espaço suficiente, retorna 0
    def allocate_memory(self, process):
        contiguous_blocks = 0
        allocated = 0
        if(process[2]):
            start_block = 64
            for x in range(64, SIZE):
                if(self.mem[x] == None):
                    contiguous_blocks += 1
                else:
                    contiguous_blocks = 0
                    start_block = x+1
                if(contiguous_blocks == process[4]): # assim que encontra espaço suficiente, faz a alocação
                    allocated = 1
                    for x in range(start_block, start_block+contiguous_blocks):
                        self.mem[x] = process[0]
                    return 1
            if(not allocated):
                return 0
        else:
            start_block = 0
            for x in range(0, 64):
                if(self.mem[x] == None):
                    contiguous_blocks += 1
                else:
                    contiguous_blocks = 0
                    start_block = x+1
                if(contiguous_blocks == process[4]):
                    allocated = 1
                    for x in range(start_block, start_block+contiguous_blocks):
                        self.mem[x] = process[0]
                    return 1
            if(not allocated):
                return 0

    # remove processo da memória
    def free_memory(self, process):
        for x in range(0, SIZE):
            if(self.mem[x] == process[0]):
                self.mem[x] = None

