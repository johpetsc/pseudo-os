import sys
from queues import Queues as q
from memory import Memory as mem
from file_system import FileSystem as fs
from process import ProcessList as pl
from resources import Resources as rsc

def main(processes, files):
    exec_time = 0 # tempo de execução em segundos
    memory = mem() # módulo de memória
    processes = pl(processes) # módulo de processos
    queues = q() #módulo de filas
    resource = rsc() #módulo de recurso

    init_processes = processes.__len__() # quantidade de processos a serem executados

    # loop principal, executa enquanto ainda existem processos não inicializados ou processos em alguma fila
    while(init_processes or queues.max != 1000):
        prio = 0
        # verifica se o processos já está no tempo de inicialização  
        for process in processes.list:
            if(process[1] == exec_time):
                # se estiver, insere na fila
                queues.create_queues(process)
                init_processes-=1

        # queues.print_queues(exec_time) # usar para debug

        # executa as filas pela ordem de prioridade, os processos são executados enquanto tem tempo de processador > 0
        # processos de tempo real
        if(len(queues.priority0)>0): # prioridade 0
            current = processes.get_process(queues.priority0[0]) # processo no início da fila
            # verifica se o processo já está na memória e executa um quantum
            if(queues.priority0[0] in memory.mem):
                processes.exec_process(queues.priority0[0]) # executa instrução
            # caso não esteja na memória, verifica se é possível alocar o processo
            elif(current[4] > 64):
                current[3] = 0 # seta o tempo de processador igual a 0 para que o processo seja removido da fila
            # se tiver espaço suficiente, aloca espaço e executa um quantum
            else:
                offset = memory.allocate_memory(current) # offset na alocação de memória
                if(offset>=0): # offset é -1 quando não há espaço disponível
                    print("\ndispatcher =>")
                    processes.init_process(queues.priority0[0], offset) # inicia o processo
                    processes.exec_process(queues.priority0[0]) # executa primeira instrução

        # processos de usuário
        if(len(queues.priority1)>0): # prioridade 1
            prio = 1
            current = processes.get_process(queues.priority1[0])
            if(resource.get_resources(current)):
                # verifica se o processo já está na memória e executa um quantum
                if(queues.priority1[0] in memory.mem):
                    processes.exec_process(queues.priority1[0]) # executa instrução
                # caso não esteja na memória, verifica se é possível alocar o processo
                elif(current[4] > 960):
                    current[3] = 0 # seta o tempo de processador igual a 0 para que o processo seja removido da fila
                # se tiver espaço suficiente, aloca espaço e executa um quantum
                else:
                #if(resource.get_resources(current)):
                    offset = memory.allocate_memory(current)
                    if(offset>=0): # offset é -1 quando não há espaço disponível
                        print("\ndispatcher =>")
                        processes.init_process(queues.priority1[0], offset) # inicia o processo
                        processes.exec_process(queues.priority1[0]) # executa primeira instrução
        elif(len(queues.priority2)>0): # prioridade 2
            prio = 2
            current = processes.get_process(queues.priority2[0])
            if(resource.get_resources(current)):
                if(queues.priority2[0] in memory.mem):
                    processes.exec_process(queues.priority2[0])
                    current[1] = exec_time # atualiza o tempo inicial, que é usado para verificar se está ocorrendo starvation
                elif(current[4] > 960):
                    current[3] = 0
                else:
                #if(resource.get_resources(current)):
                    offset = memory.allocate_memory(current)
                    if(offset>=0):
                        print("\ndispatcher =>")
                        processes.init_process(queues.priority2[0], offset)
                        processes.exec_process(queues.priority2[0])
        elif(len(queues.priority3)>0): # prioridade 3
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

        # atualiza a posição dos processos na fila
        queues.update_positions(prio)
        # remove processos que já terminaram a execução
        queues.finish_processes(memory, processes.list)
        #atualiza a prioridade dos processos
        queues.update_priorities(exec_time, processes.list)
        # libera os recursos
        resource.free_resources()
        exec_time+=1
    

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
        system.allocate_file(x, lines[1 + int(lines[1]) + x].split(', '), processes.list)
    # Apresenta o disco contendo os arquivos, sendo que os espaços em 0 não possuem
    system.disk_ocupation()

    files.close()


if __name__ == "__main__":

    if(len(sys.argv) != 3):
        print("Usage: <processes file> <files file>")
        exit()

    processes = sys.argv[1] # entrada de processos
    files = open(sys.argv[2], 'r') # entrada de arquivos
    main(processes, files)
