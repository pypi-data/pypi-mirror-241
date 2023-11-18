import concurrent.futures
import multiprocessing
import threading
from functools import wraps

from typing import Any, Callable, List, Dict, Tuple
from typing_extensions import Annotated, Doc

from parallelexec._cpu import max_cpu_cores


class ParallelExec:
    def __init__(self):
        ...

    @staticmethod
    def processor(
        funcs: Annotated[
            List[Callable],
            Doc(
                """
                List of callable functions
                """
            ),
        ],
        join: Annotated[
            bool,
            Doc(
                """
                If True, the main process will wait until other processes or funcs have finished executing.
                Else the main process continues regardless.
                """
            ),
        ] = False,
    ) -> Any:
        """
        Used as a decorator for a function that groups all the tasks above.

        example:
            @ParallelExec.processor([func1, func2, func3], join=True)
            def run_all(): ...
            some_tasks()
            run_all()
            other_tasks()
        """

        def decorator(func: Any):
            @wraps(func)
            def wrapper(*args: Tuple[Any, ...], **kwargs: Dict[str, Any]) -> Any:
                processes = [multiprocessing.Process(target=f) for f in funcs]
                if join:
                    for process in processes:
                        process.start()
                        process.join()
                else:
                    for process in processes:
                        process.start()
                return func(*args, **kwargs)

            return wrapper

        return decorator

    @staticmethod
    def cores_limited_processor(
        callables: Annotated[
            List[Callable],
            Doc(
                """
                List of callable functions
                """
            ),
        ],
        max_workers: Annotated[
            int,
            Doc(
                """
                The number of current CPU cores to override this set the number u want
                """
            ),
        ] = max_cpu_cores(),
    ) -> None:
        """
        This will run the tasks using as many processes as the current machine's CPU allows.
        If a CPU has 16 cores, it will run 16 processes; if 4, then 4, and so on.
        To override the max value and run as many processes as needed, set max_workers
        to the desired number.
        """
        with concurrent.futures.ProcessPoolExecutor(
            max_workers=max_workers
        ) as executor:
            futures = [executor.submit(callable_func) for callable_func in callables]
            concurrent.futures.wait(futures)

    @staticmethod
    def thread(
        join: Annotated[
            bool,
            Doc(
                """
                If True, the main process will wait until all threaded funcs have finished executing.
                Else, the main process continues regardless.
                """
            ),
        ] = False
    ) -> Any:
        """Use this as a wrapper for each function you want to run in parallel."""

        def decorator(fn: Callable):
            @wraps(fn)
            def execute(*k: Tuple[Any, ...], **kw: Dict[str, Any]) -> Any:
                f = threading.Thread(target=fn, args=k, kwargs=kw)
                f.start()
                if join:
                    f.join()
                return f

            return execute

        return decorator
