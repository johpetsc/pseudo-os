class FileSystem:
    def __init__(self):
        self.bit_map = []
        self.files = []
        self.volume = 0
        print('File System =>')

    def initialize_volume(self, blocks):
        # defines the number of blocks in the volume and initializes the bitmap
        self.volume = blocks
        for x in range(blocks):
            self.bit_map.append(0)

    # initial file allocation
    def pre_allocated_file(self, file):
        # inserts into the bitmap the blocks occupied by a file
        for block in range(int(file[2][0:-1])):
            self.bit_map[int(file[1]) + block] = 1

        # registers file information such as name, location, size and the process that created it 
        self.files.append((file[0], int(file[1]), int(file[2][0:-1]), -1))

    # creates or deletes files
    def allocate_file(self, operation, file, processes):
        # checks if the precess exists
        current_process = (-1)
        for x in processes:
            if int(file[0]) == x[0]:
                current_process = x

        if  current_process == (-1):
            print('operation {} => Fail'.format(operation))
            print('Process {} does not exist.'.format(file[0]))
            return
            
        current_file = ('-1')
        # operation for deleting a file
        if file[1] == '1':
            # checks if the file exists
            for x in self.files:
                if file[2][0:-1] == x[0]:
                    current_file = x

            if current_file == ('-1'):
                print('operation {} => Fail'.format(operation))
                print('File {} does not exist.'.format(current_file[0]))

            else:
                # checks if a process is real time or if it created the file
                if current_process[2] == current_file[3] or current_process[2] == 0:
                    # case positive, the bitmap is updated and the file is removed from queue
                    for x in range(current_file[2]):
                        self.bit_map[x+current_file[1]] = 0
                    self.files.remove((current_file))
                    print('operation {} => Success'.format(operation))
                    print('Process {} deleted the file {}.'.format(file[0], current_file[0]))

                else:
                    print('operation {} => Fail'.format(operation))
                    print('Process {} could not remove file {} because it is not the file creator.'.format(file[0], current_file[0]))

        # operation for creating a file
        else:
            # checks if the file is already in disk
            for x in self.files:
                if file[2] == x[0]:
                    print('operation {} => Fail'.format(operation))
                    print('Process {} is already in disk.'.format(file[2]))
                    return

            # checks if there is enough contiguous space for the file
            for x in range(self.volume - int(file[3]) + 1):
                if 1 not in self.bit_map[x:x+int(file[3])]:
                    # case positive, the bitmap is updated and the file inserted into the queue
                    for y in range(int(file[3])):
                        self.bit_map[x+y] = 1
                    self.files.append((file[2], x, int(file[3]), int(file[0])))
                    print('operation {} => Success'.format(operation))
                    print('Process {} created file {}.'.format(file[0], file[2]))

                    return

            print('operation {} => Fail'.format(operation))
            print('Process {} could not create file {} (not enough space).'.format(file[0], file[2]))

    # presents the disk occupation
    def disk_occupation(self):
        disk = []
        for x in range(self.volume):
            disk.append(0)

        for file in self.files:
            for x in range(file[1], file[1] + file[2]):
                disk[x] = file[0]

        print(disk)
