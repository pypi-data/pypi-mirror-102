import subprocess

from ngpuinfo.byte_units import ByteUnits


class NGPU(object):

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    def mem_total(self) -> int:
        return int(mem_info(self.id)[0])

    def mem_used(self) -> int:
        return int(mem_info(self.id)[1])

    def mem_free(self) -> int:
        return int(mem_info(self.id)[2])

    def mem_info(self) -> str:
        total, used, free = mem_info(self.id)
        ret = "%-12s: %d MiB\n%-12s: %d MiB\n%-12s: %d MiB" % (
            "Mem Total", ByteUnits.MiB.from_unit(total, ByteUnits.B),
            "Mem Used", ByteUnits.MiB.from_unit(used, ByteUnits.B),
            "Mem Free", ByteUnits.MiB.from_unit(free, ByteUnits.B)
        )
        return ret


def mem_info(id):
    ret = subprocess.run(["nvidia-smi", "--query-gpu=memory.total,memory.used,memory.free", "--format=csv,noheader", "-i", str(id)],
                         stdout=subprocess.PIPE)
    if ret.returncode == 0:
        meminfos = ret.stdout.decode().split(",")
        total = ByteUnits.parse_value(meminfos[0])
        used = ByteUnits.parse_value(meminfos[1])
        free = ByteUnits.parse_value(meminfos[2])
        return total, used, free
    else:
        return 0, 0, 0
