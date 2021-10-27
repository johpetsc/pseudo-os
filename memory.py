SIZE = 1024

class Memory:
    def __init__(self):
        self.mem = [None] * SIZE
        self.used_blocks = 0

    # aloca os blocos de memória contiguos de um processo
    # se não houver espaço suficiente, retorna 0
    def allocate_memory(self, process):
        contiguous_blocks = 0
        allocated = 0
        self.used_blocks+=process[4]
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
                    return start_block
                    # return self.used_blocks
            if(not allocated):
                return -1
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
                    return start_block
                    # return self.used_blocks
            if(not allocated):
                return -1

    # remove processo da memória
    def free_memory(self, process):
        for x in range(0, SIZE):
            if(self.mem[x] == process[0]):
                self.mem[x] = None
        # caso seja necessário limpar a memória depois de cada quantum
        # for x in range(0, SIZE):
        #     self.mem[x] = None

