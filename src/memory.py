SIZE = 1024

class Memory:
    def __init__(self):
        self.mem = [None] * SIZE
        self.used_blocks = 0

    # allocates contiguous blocks for a process
    # if not enough space, returns 0
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
                if(contiguous_blocks == process[4]): # allocates as soon as enough space is found
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

    # removes process from memory
    def free_memory(self, process):
        for x in range(0, SIZE):
            if(self.mem[x] == process[0]):
                self.mem[x] = None

