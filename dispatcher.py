import sys
from queues import Queues as q
from memory import Memory as mem

def main(processes, files):
    exec_time = 0
    memory = mem()
    # lista de processos usada enquanto o modulo de processos não estiver implementado
    # primeiro valor de cada lista representa o PID do processo
    processes = [[0,2,0,3,64,0,0,0,0], [1,8,0,2,64,0,0,0,0]]
    queues = q(processes)
    # loop principal, executa enquanto ainda existem processos não inicializados ou processos em alguma fila
    while(processes or queues.max != 1000):
        # verifica se o processos já está no tempo de inicialização
        for process in processes:
            if(process[1] == exec_time):
                # se estiver, aloca os blocos de memória e insere na fila
                memory.allocate_memory(process)
                queues.create_queues(process)
                processes.pop(0)
        # executa as filas pela ordem de prioridade, os processos são executados enquanto tem tempo de processador > 0
        if(len(queues.priority0)>0):
            queues.processes[queues.priority0[0]][3]-=1
            # se o tempo de processador chegar a 0, libera os blocos de mamória e remove da fila
            if(queues.processes[queues.priority0[0]][3] == 0):
                memory.free_memory(process)
                queues.priority0.pop(0)
                queues.max+=1
        elif(len(queues.priority1)>0):
            queues.processes[queues.priority1[0]][3]-=1
            # se o tempo de processador chegar a 0, libera os blocos de mamória e remove da fila
            if(queues.processes[queues.priority1[0]][3] == 0):
                memory.free_memory(process)
                queues.priority1.pop(0)
                queues.max+=1
        elif(len(queues.priority2)>0):
            queues.processes[queues.priority2[0]][3]-=1
            # se o tempo de processador chegar a 0, libera os blocos de mamória e remove da fila
            if(queues.processes[queues.priority2[0]][3] == 0):
                memory.free_memory(process)
                queues.priority2.pop(0)
                queues.max+=1
        elif(len(queues.priority3)>0):
            queues.processes[queues.priority3[0]][3]-=1
            # se o tempo de processador chegar a 0, libera os blocos de mamória e remove da fila
            if(queues.processes[queues.priority3[0]][3] == 0):
                memory.free_memory(process)
                queues.priority3.pop(0)
                queues.max+=1
        #atualiza a prioridade dos processos
        queues.update_priorities(exec_time)
        exec_time+=1


if __name__ == "__main__":
    processes = sys.argv[1] # entrada de processos
    files = sys.argv[2] # entrada de arquivos
    main(processes, files)