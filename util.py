from functools import wraps
import time

func_dict = {}


def measure_method_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        func_dict.setdefault(func.__qualname__, {"total_call": 0, "avg": 0})

        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__qualname__} elapsed time: {elapsed:.4f}s")

        func_dict[func.__qualname__]["avg"] = (
            func_dict[func.__qualname__]["total_call"]
            * func_dict[func.__qualname__]["avg"]
            + elapsed
        ) / (func_dict[func.__qualname__]["total_call"] + 1)

        func_dict[func.__qualname__]["total_call"] += 1

        print(
            f"avg {func.__qualname__} elapsed time: {func_dict[func.__qualname__]["avg"]:.4f}s"
        )
        return result

    
    return wrapper
