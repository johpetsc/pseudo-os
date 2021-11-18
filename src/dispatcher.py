import sys
from queues import Queues as q
from memory import Memory as mem
from file_system import FileSystem as fs
from processes import ProcessList as pl
from resources import Resources as rsc

def main(processes, files):
    exec_time = 0 # execution time in seconds
    memory = mem() # memory module 
    processes = pl(processes) # processes module
    queues = q() # processes queues module
    resource = rsc() # resources module

    init_processes = processes.__len__() # number of processes to be executed

    # main loop, executes while there are processes not initialized or in a queue
    while(init_processes or queues.max != 1000):
        prio = 0
        # checks if a process has reached its initialization time  
        for process in processes.list:
            if(process[1] == exec_time):
                # case positive, insert into queue
                queues.create_queues(process)
                init_processes-=1

        # queues.print_queues(exec_time) # use for debug

        # executes the queues based on their priority, processes are executed if their processor time is still > 0
        # real time processes
        if(len(queues.priority0)>0): # priority 0
            current = processes.get_process(queues.priority0[0]) # process at the start of the queue
            # checks if the process is already in memory and executes a quantum
            if(queues.priority0[0] in memory.mem):
                processes.exec_process(queues.priority0[0]) # executes an instruction 
            # if not in memory, verifies is its possible to allocate the process in memory
            elif(current[4] > 64):
                current[3] = 0 # sets processor time to 0 so the process can be removed from queue
            # if there is enough space, allocates the process and executes an instruction
            else:
                offset = memory.allocate_memory(current) # memory offset
                if(offset>=0): # offset is -1 when theres not enough free space
                    print("\ndispatcher =>")
                    processes.init_process(queues.priority0[0], offset) # initializes the process
                    processes.exec_process(queues.priority0[0]) # executes the first instruction

        # user processes
        if(len(queues.priority1)>0): # priority 1
            prio = 1
            current = processes.get_process(queues.priority1[0])
            if(resource.get_resources(current)):
                # checks if the process is already in memory and executes a quantum
                if(queues.priority1[0] in memory.mem):
                    processes.exec_process(queues.priority1[0]) # executes an instruction 
                # if not in memory, verifies is its possible to allocate the process in memory
                elif(current[4] > 960):
                    current[3] = 0 # sets processor time to 0 so the process can be removed from queue
                # if there is enough space, allocates the process and executes an instruction
                else:
                #if(resource.get_resources(current)):
                    offset = memory.allocate_memory(current)
                    if(offset>=0): # offset is -1 when theres not enough free space
                        print("\ndispatcher =>")
                        processes.init_process(queues.priority1[0], offset) # initializes the process
                        processes.exec_process(queues.priority1[0]) # executes the first instruction
        elif(len(queues.priority2)>0): # priority 2
            prio = 2
            current = processes.get_process(queues.priority2[0])
            if(resource.get_resources(current)):
                if(queues.priority2[0] in memory.mem):
                    processes.exec_process(queues.priority2[0])
                    current[1] = exec_time # updates the init time, which is used to verify if there is startvation
                elif(current[4] > 960):
                    current[3] = 0
                else:
                #if(resource.get_resources(current)):
                    offset = memory.allocate_memory(current)
                    if(offset>=0):
                        print("\ndispatcher =>")
                        processes.init_process(queues.priority2[0], offset)
                        processes.exec_process(queues.priority2[0])
        elif(len(queues.priority3)>0): # priority 3
            prio = 3
            current = processes.get_process(queues.priority3[0])
            if(resource.get_resources(current)):
                if(queues.priority3[0] in memory.mem):
                    processes.exec_process(queues.priority3[0])
                    current[1] = exec_time
                elif(current[4] > 960):
                    current[3] = 0
                else:
                #if(resource.get_resources(current)):
                    offset = memory.allocate_memory(current)
                    if(offset>=0):
                        print("\ndispatcher =>")
                        processes.init_process(queues.priority3[0], offset)
                        processes.exec_process(queues.priority3[0])

        # updates the processes position in the queues
        queues.update_positions(prio)
        # removes the processes already finished
        queues.finish_processes(memory, processes.list)
        # updates the priority of the processes
        queues.update_priorities(exec_time, processes.list)
        # memory.free_memory()
        # free resources
        resource.free_resources()
        exec_time+=1
    

    lines = files.readlines()
    # initializes the file system
    system = fs()
    # defines the number of blocks in the volume and initializes the bitmap
    system.initialize_volume(int(lines[0]))
    # initial file allocation
    for x in range(int(lines[1])):
        system.pre_allocated_file(lines[2+x].split(', '))
    # creates or deletes files
    for x in range(1, len(lines) - (1 + int(lines[1]))):
        system.allocate_file(x, lines[1 + int(lines[1]) + x].split(', '), processes.list)
    # presents the disk occupation
    system.disk_occupation()

    files.close()


if __name__ == "__main__":

    if(len(sys.argv) != 3):
        print("Usage: <processes file> <files file>")
        exit()

    processes = sys.argv[1] # processes input file
    files = open(sys.argv[2], 'r') # files input file
    main(processes, files)
