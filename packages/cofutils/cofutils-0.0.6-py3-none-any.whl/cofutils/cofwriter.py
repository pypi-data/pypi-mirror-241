import csv
from abc import ABC, abstractmethod
from typing import Any
from collections import defaultdict
import os
from torch.utils.tensorboard import SummaryWriter
import datetime

class BaseWriter(ABC):
    def __init__(self, file_path) -> None:
        self.file_path = file_path

    @abstractmethod
    def write(self, data):
        pass

class Coftb(BaseWriter):
    def __init__(self, file_path='coftb') -> None:
        super().__init__(file_path)
    def initialize(self, name=None):
        if name:
            formatted_name = name
        else:
            now = datetime.datetime.now()
            formatted_name = now.strftime("%m%d%H%M%S")

        self.writer = SummaryWriter(os.path.join(self.file_path, formatted_name))
        self.iter_dict = defaultdict(int)
    def write(self, data:dict, text:str):
        for k,v in data.items():
            self.iter_dict[k]+=1
            self.writer.add_scalar(k, v, self.iter_dict[k])

class _Cofcsv(BaseWriter):
    def __init__(self, file_path=None) -> None:
        super().__init__(file_path)
        self.table=defaultdict(list)

    def write(self, data_dict:dict):
        for k, v in data_dict.items():
            self.table[k].append(v)
        
    def save(self, file_prefix, reset):
        data=[]
        data.append(self.table.keys())
        for each in zip(*self.table.values()):
            data.append(list(each))
        with open(f'{file_prefix}.csv', 'w', newline='') as fp:
            writer = csv.writer(fp)
            for data_row in data:
                writer.writerow(data_row)
        if reset:
            self.table.clear()

class Cofcsv:
    def __init__(self) -> None:
        self.table=defaultdict(_Cofcsv)

    def __call__(self, name) -> _Cofcsv:
        return self.table[name]
    
    def save(self, root_dir='.', reset=True) -> None:
        if not (os.path.exists(root_dir) and os.path.isdir(root_dir)):
            os.mkdir(root_dir)
        for key, value in self.table.items():
            value.save(os.path.join(root_dir,key), reset)
        

cofcsv = Cofcsv()
coftb = Coftb()