# Parallelexec 

#### Parallelexec is a Python module that provides decorators and methods to easily run multiple functions concurrently.

## Installation
#### Use pip
````commandline
pip install parallelexec
````
## Usage 
### Threads:
````python
from parallelexec import ParallelExec

@ParallelExec.thread(join=True)
def fun():
    ...
````
### Processes:
````python
from parallelexec import ParallelExec

def func() -> None: ...
def func2() -> None: ...
def func3() -> None: ...

if __name__ == "__main__":
    ParallelExec.cores_limited_processor([func,func2,func3])
````
#### Better yet, check `examples/`
## License 
#### This is under the [Public Domain](/UNLICENSE)