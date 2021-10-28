class Resources:
    #inicializa os recursos
    def __init__(self):
        self.scanner = 0
        self.modem = 0
        self.disp_SATA = [0, 0]
        self.impressoras = [0, 0]

    #aloca o recurso para o processo 
    #-retorna 1 se foi alocado com sucesso ou se nada foi pedido
    #-retorna 0 se nao foi alocado com sucesso
    def get_resources(self, process):
        # verifica se a entrada é valida
        if((process[6] > 1) or (process[7] > 1) or (process[8] > 2) or (process[5] > 2)):
            process[3] = 0
            return 0

        if(process[6] == 1) and (self.scanner != 0):
            return 0
        elif(process[7] == 1) and (self.modem != 0):
            return 0
        elif(process[8] == 1) and (self.disp_SATA[0] != 0):
            return 0
        elif(process[8] == 2) and (self.disp_SATA[1] != 0):
            return 0
        elif(process[5] == 1) and (self.impressoras[0] != 0):
            return 0
        elif(process[5] == 2) and (self.impressoras[1] != 0):
            return 0
        else:       
            if(process[6] == 1):
                self.scanner = 1
            if(process[7] == 1):
                self.modem = 1
            if(process[8] == 1):
                self.disp_SATA[0] = 1
            if(process[8] == 2):
                self.disp_SATA[1] = 1
            if(process[5] == 1):
                self.impressoras[0] = 1
            if(process[5] == 2):
                self.impressoras[1] = 1
            return 1

    #libera todos os recursos utilizados pelo processo
    def free_resources(self):
        self.scanner = 0
        self.modem = 0
        self.disp_SATA = [0, 0]
        self.impressoras = [0, 0]
####
    
