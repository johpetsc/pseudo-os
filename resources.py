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
        free_resources = 1
        if (process.scanner == 1) and (self.scanner != 0):
            free_resources = 0
        if (process.modem == 1) and (self.modem != 0):
            free_resources = 0
        if (process.disp_SATA == 1) and (self.disp_SATA[0] != 0):
            free_resources = 0
        if (process.disp_SATA == 2) and (self.disp_SATA[1] != 0):
            free_resources = 0
        if (process.impressoras == 1) and (self.impressoras[0] != 0):
            free_resources = 0
        if (process.impressoras == 2) and (self.impressoras[1] != 0):
            free_resources = 0
        
        
        if free_resources == 1:
            if(process.scanner == 1):
                self.scanner = 1
            if(process.modem == 1):
                self.modem = 1
            if(process.disp_SATA == 1):
                self.disp_SATA[0] = 1
            if(process.disp_SATA == 2):
                self.disp_SATA[1] = 1
            if(process.impressora == 1):
                self.impressora[0] = 1
            if(process.impressora == 2):
                self.impressora[1] = 1
        return free_resources

    #libera todos os recursos utilizados pelo processo
    def free_resources(self):
        self.scanner = 0
        self.modem = 0
        self.disp_SATA = [0, 0]
        self.impressoras = [0, 0]
    
