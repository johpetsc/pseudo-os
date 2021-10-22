import sys
from queues import Queues as q
from memory import Memory as mem
from file_system import FileSystem as fs

def main(processes, files):
    exec_time = 0
    memory = mem()
    # lista de processos usada enquanto o modulo de processos não estiver implementado
    # primeiro valor de cada lista representa o PID do processo
    processes = [[0,2,0,10,64,0,0,0,0], [1,8,0,2,64,0,0,0,0], [2,1,1,1,64,0,0,0,0], [3,5,3,3,64,0,0,0,0], [4,10,2,9,64,0,0,0,0], [5,12,1,3,64,0,0,0,0], [6,6,2,1,64,0,0,0,0], [7,11,3,14,64,0,0,0,0]]
    queues = q(processes)
    init_processes = len(queues.processes)
    # loop principal, executa enquanto ainda existem processos não inicializados ou processos em alguma fila
    while(init_processes or queues.max != 1000):
        # verifica se o processos já está no tempo de inicialização
        for process in queues.processes:
            if(process[1] == exec_time):
                # se estiver, insere na fila
                queues.create_queues(process)
                init_processes-=1
        # prints para debug, mostra o estado das listas
        # print("exec_time: {}".format(exec_time))
        # print("p0:")
        # print(queues.priority0)
        # print("p1:")
        # print(queues.priority1)
        # print("p2:")
        # print(queues.priority2)
        # print("p3:")
        # print(queues.priority3)
        # executa as filas pela ordem de prioridade, os processos são executados enquanto tem tempo de processador > 0
        if(len(queues.priority0)>0):
            # verifica se o processo já está na memória e executa um quantum
            if(queues.priority0[0] in memory.mem):
                queues.processes[queues.priority0[0]][3]-=1
            # caso não esteja na memória, verifica se é possível alocar o processo
            elif(queues.processes[queues.priority0[0]][4] > 64):
                queues.processes[queues.priority0[0]][3] = 0 # seta o tempo de processador igual a 0 para que o processo seja removido da fila
            # se tiver espaço suficiente, aloca espaço e executa um quantum
            elif(memory.allocate_memory(queues.processes[queues.priority0[0]])):
                queues.processes[queues.priority0[0]][3]-=1
        if(len(queues.priority1)>0):
            if(queues.priority1[0] in memory.mem):
                queues.processes[queues.priority1[0]][3]-=1
            elif(queues.processes[queues.priority1[0]][4] > 1000):
                queues.processes[queues.priority1[0]][3] = 0
            elif(memory.allocate_memory(queues.processes[queues.priority1[0]])):
                queues.processes[queues.priority1[0]][3]-=1
        elif(len(queues.priority2)>0):
            if(queues.priority2[0] in memory.mem):
                queues.processes[queues.priority2[0]][3]-=1
                queues.processes[queues.priority2[0]][1] = exec_time # atualiza o tempo inicial, que é usado para verificar se está ocorrendo starvation
            elif(queues.processes[queues.priority2[0]][4] > 1000):
                queues.processes[queues.priority2[0]][3] = 0
            elif(memory.allocate_memory(queues.processes[queues.priority2[0]])):
                queues.processes[queues.priority2[0]][3]-=1
        elif(len(queues.priority3)>0):
            if(queues.priority3[0] in memory.mem):
                queues.processes[queues.priority3[0]][3]-=1
                queues.processes[queues.priority3[0]][1] = exec_time
            elif(queues.processes[queues.priority3[0]][4] > 1000):
                queues.processes[queues.priority3[0]][3] = 0
            elif(memory.allocate_memory(queues.processes[queues.priority3[0]])):
                queues.processes[queues.priority3[0]][3]-=1

        # atualiza a posição dos processos na fila
        queues.update_positions()
        # remove processos que já terminaram a execução
        queues.finish_processes(memory)
        #atualiza a prioridade dos processos
        queues.update_priorities(exec_time)
        exec_time+=1

    processes = [[0,2,0,3,64,0,0,0,0], [1,8,0,2,64,0,0,0,0]]

    lines = files.readlines()
    # Inicializa o sistema de arquivos
    system = fs()
    # Define a quantidade de blocos no volume e inicia o mapa de bits
    system.initialize_volume(int(lines[0]))
    # Alocação de arquivos inicial
    for x in range(int(lines[1])):
        system.pre_allocated_file(lines[2+x].split(', '))
    # Cria ou deleta arquivo
    for x in range(1, len(lines) - (1 + int(lines[1]))):
        system.allocate_file(x, lines[1 + int(lines[1]) + x].split(', '), queues.processes)
    # Apresenta o disco contendo os arquivos, sendo que os espaços em 0 não possuem
    system.disk_ocupation()

    files.close()


if __name__ == "__main__":
    processes = sys.argv[1] # entrada de processos
    files = open(sys.argv[2], 'r') # entrada de arquivos
    main(processes, files)