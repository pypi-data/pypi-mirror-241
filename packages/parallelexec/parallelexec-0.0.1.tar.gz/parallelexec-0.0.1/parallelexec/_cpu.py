from multiprocessing import cpu_count as mp_cpu_count
from os import cpu_count as os_cpu_count


def max_cpu_cores() -> int:
    return os_cpu_count() or mp_cpu_count()
