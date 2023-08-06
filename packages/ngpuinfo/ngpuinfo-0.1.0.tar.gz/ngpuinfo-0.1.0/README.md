# NGPUInfo

## Install
`pip install ngpuinfo`

## Description
This package uses `nvidia-smi` to get gpu information, so it only support nvidia gpus, and the `nvidia-smi` must be in 
system path.

## Get start
```python
from ngpuinfo import NGPUInfo

print(NGPUInfo.NUMBERS)
print(NGPUInfo.CUDA_VERSION)
gpus = NGPUInfo.list_gpus()
for g in gpus:
    print()
    print(g.id)
    print(g.name)
    print(g.mem_info())
```

## Usage
```python
gpu = NGPUInfo.list_gpus()[0]

gpu.mem_total() # total mem of gpu, realtime refresh, the unit is Byte
gpu.mem_used()  # used  mem of gpu, realtime refresh, the unit is Byte
gpu.mem_free()  # free  mem of gpu, realtime refresh, the unit is Byte
```