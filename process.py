from collections.abc import Sequence
from copy import deepcopy

class ProcessList(Sequence):
    def __init__(self, filepath) -> None:
        self.processes = []

        with open(filepath, 'r') as f:
            for line in f:
                self.processes.append(list(map(int, line.split(','))))

        super().__init__()
    
    def get_process(self, index) -> list:
        return self.processes[index]

    def copy(self) -> 'ProcessList':
        return deepcopy(self)

    def __getitem__(self, index) -> list:
        return self.processes[index]
    
    def __len__(self) -> int:
        return len(self.processes)