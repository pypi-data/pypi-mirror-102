from typing import List

from ngpuinfo.ngpu import NGPU
from ngpuinfo.ngpu_detect import detect


class NGPUInfo(object):

    NUMBERS = 0
    CUDA_VERSION = "-"
    __GPUS = []

    @classmethod
    def list_gpus(cls) -> List[NGPU]:
        return cls.__GPUS

    @classmethod
    def refresh(cls):
        res = detect()
        if res is not None:
            cls.NUMBERS = res["numbers"]
            cls.CUDA_VERSION = res["cuda_version"]
            cls.__GPUS = res["gpus"]
        else:
            cls.NUMBERS = 0
            cls.CUDA_VERSION = "-"
            cls.__GPUS = []


NGPUInfo.refresh()
