class Queues:
    def __init__(self, processes):
        self.priority0 = []
        self.priority1 = []
        self.priority2 = []
        self.priority3 = []
        self.processes = processes.copy()
        self.max = 1000 # variável usada para verificar a quantidade de processos nas filas

    # insere o processo na fila correspondente à prioridade
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

    # remove os processos que tem o tempo de processador igual a 0
    def finish_processes(self, memory):
        for p in self.priority0:
            if(self.processes[p][3] == 0):
                memory.free_memory(self.processes[p])
                self.priority0.remove(p)
                self.max+=1
        for p in self.priority1:    
            if(self.processes[p][3] == 0):
                memory.free_memory(self.processes[p])
                self.priority1.remove(p)
                self.max+=1
        for p in self.priority2:    
            if(self.processes[p][3] == 0):
                memory.free_memory(self.processes[p])
                self.priority2.remove(p)
                self.max+=1
        for p in self.priority3:    
            if(self.processes[p][3] == 0):
                memory.free_memory(self.processes[p])
                self.priority3.remove(p)
                self.max+=1

    # remove o primeiro processo da fila e envia para o final
    # não se aplica para prioridade 0 por ser uma fila FIFO
    def update_positions(self):
        if(len(self.priority1)>1):
            process = self.priority1.pop(0)
            self.priority1.append(process)
        if(len(self.priority2)>1):
            process = self.priority2.pop(0)
            self.priority2.append(process)
        if(len(self.priority3)>1):
            process = self.priority3.pop(0)
            self.priority3.append(process)

    # processos que estão a 10 quantum sem serem executados sobem de prioridade
    # não se aplica para processos com prioridade 0 e 1
    def update_priorities(self, exec_time):
        for p in self.priority2:
            if(exec_time - self.processes[p][1] > 10):
                self.processes[p][1] = exec_time
                self.priority1.append(p)
                self.priority2.remove(p)
        for p in self.priority3:
            if(exec_time - self.processes[p][1] > 10):
                self.processes[p][1] = exec_time
                self.priority2.append(p)
                self.priority3.remove(p)