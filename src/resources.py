class Resources:
    # initializes the resources
    def __init__(self):
        self.scanner = 0
        self.modem = 0
        self.disp_SATA = [0, 0]
        self.printers = [0, 0]

    # allocates resources for a process 
    #-returns 1 if successfully allocated or if nothing was requested
    #-returns 0 if not successfully allocated
    def get_resources(self, process):
        # checks if input is valid
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
        elif(process[5] == 1) and (self.printers[0] != 0):
            return 0
        elif(process[5] == 2) and (self.printers[1] != 0):
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
                self.printers[0] = 1
            if(process[5] == 2):
                self.printers[1] = 1
            return 1

    # free resources
    def free_resources(self):
        self.scanner = 0
        self.modem = 0
        self.disp_SATA = [0, 0]
        self.printers = [0, 0]
    
