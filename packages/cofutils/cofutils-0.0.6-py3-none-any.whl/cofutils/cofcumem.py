from typing import Any
import torch
import torch.distributed as dist
from .coflog import default_logger
from .cofwriter import coftb
def check_rank(rank):
    return not dist.is_initialized() or dist.get_rank()==rank

class Cofmem:
    def __init__(self) -> None:
        self.writer=None
    def set_writer(self, writer=None, name=None, rank=0):
        self.writer=writer
        if self.writer == 'tb' and check_rank(rank=rank):
            coftb.initialize(name)
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        self.report_memory_usage(*args, **kwds)
    def report_memory_usage(self, msg="", rank=0):
        # MC: Memory Allocated in Current
        # MM: Memory Allocated in Max
        # MR: Memory Reserved by PyTorch
        
        GB = 1024*1024*1024
        if check_rank(rank):
            MA = torch.cuda.memory_allocated()/GB
            MM = torch.cuda.max_memory_allocated()/GB
            MR = torch.cuda.memory_reserved()/GB
            default_logger.info(f"{msg} GPU Memory Report (GB): MA = {MA:.2f} | "
                            f"MM = {MM:.2f} | "
                            f"MR = {MR:.2f}")
            if self.writer=='csv':
                pass
            elif self.writer=='tb':
                coftb.write({'MA':MA, 'MM':MM, 'MR':MR}, text=msg)
            else:
                pass
cofmem = Cofmem()