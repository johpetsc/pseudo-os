class FileSystem:
    def __init__(self):
        self.bit_map = []
        self.files = []
        self.volume = 0
        print('Sitema de arquivos =>')

    def initialize_volume(self, blocks):
        # Define a quantidade de blocos no volume e inicia o mapa de bits
        self.volume = blocks
        for x in range(blocks):
            self.bit_map.append(0)

    # Alocação de arquivos inicial
    def pre_allocated_file(self, file):
        # Coloca no map de bits os blocos que estão ocupados por um arquivo
        for block in range(int(file[2][0:-1])):
            self.bit_map[int(file[1]) + block] = 1

        # Registra informações do arquivo como nome, local, tamanho e processo responsável por criá-lo, caso não possua o valor é -1
        self.files.append((file[0], int(file[1]), int(file[2][0:-1]), -1))

    # Cria ou deleta arquivo
    def allocate_file(self, operation, file, processes):
        # Verifica se o processo existe
        current_process = (-1)
        for x in processes:
            if int(file[0]) == x[0]:
                current_process = x

        if  current_process == (-1):
            print('operacao {} => Falha'.format(operation))
            print('O processo {} nao existe.'.format(file[0]))
            return
            
        current_file = ('-1')
        # Operação de deletar arquivo
        if file[1] == '1':
            # Verifica se o arquivo existe
            for x in self.files:
                if file[2][0:-1] == x[0]:
                    current_file = x

            if current_file == ('-1'):
                print('operacao {} => Falha'.format(operation))
                print('O arquivo {} nao existe.'.format(current_file[0]))

            else:
                # Verifica se o processo é de tempo real ou criou o arquivo
                if current_process[2] == current_file[3] or current_process[2] == 0:
                    # Caso sim o mapa de bits é atualizado e o arquivo é removido da lista
                    for x in range(current_file[2]):
                        self.bit_map[x+current_file[1]] = 0
                    self.files.remove((current_file))
                    print('operacao {} => Sucesso'.format(operation))
                    print('O processo {} deletou o arquivo {}.'.format(file[0], current_file[0]))

                else:
                    print('operacao {} => Falha'.format(operation))
                    print('O processo {} nao pode remover o arquivo {} pois nao o criou.'.format(file[0], current_file[0]))

        # Operação de criação do arquivo
        else:
            # Verifica se o arquivo já existe no disco
            for x in self.files:
                if file[2] == x[0]:
                    print('operacao {} => Falha'.format(operation))
                    print('O arquivo {} ja existe no disco.'.format(file[2]))
                    return

            # Verifica se existe espaço contíguo para o arquivo
            for x in range(self.volume - int(file[3]) + 1):
                if 1 not in self.bit_map[x:x+int(file[3])]:
                    # Caso sim o mapa de bits é atualizado e o arquivo adicionado na lista
                    for y in range(int(file[3])):
                        self.bit_map[x+y] = 1
                    self.files.append((file[2], x, int(file[3]), int(file[0])))
                    print('operacao {} => Sucesso'.format(operation))
                    print('O processo {} criou o arquivo {}.'.format(file[0], file[2]))

                    return

            print('operacao {} => Falha'.format(operation))
            print('O processo {} nao pode criar o arquivo {} (falta de espaco).'.format(file[0], file[2]))

    # Apresenta o disco contendo os arquivos, sendo que os espaços em 0 não possuem
    def disk_ocupation(self):
        disk = []
        for x in range(self.volume):
            disk.append(0)

        for file in self.files:
            for x in range(file[1], file[1] + file[2]):
                disk[x] = file[0]

        print(disk)
