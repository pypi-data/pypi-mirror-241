from functools import wraps
from typing import Any, Callable, Optional
import inspect


class SuvOperationContext:

    state: dict[str, Any]
    func_kwargs: dict[str, Any]
    arg_validator: Callable[["SuvOperationContext", dict], None]

    def __init__(self, validator: Callable[["SuvOperationContext", dict], None] = None, func_kwargs: dict[str, Any] = None):
        self.arg_validator = validator
        self.state = {
            "log": [],
            "errors": []
        }
        self.func_kwargs = func_kwargs

    def __enter__(self):
        try:
            if self.func_kwargs and self.arg_validator:
                self.arg_validator(self, **self.func_kwargs)

            return self
        except Exception as e:
            self.__exit__(type(e), e, e.__traceback__)
            raise

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        if exc_type is not None:
            if self.state["errors"]:
                print("Errors flagged during operation:")
                for error in self.state["errors"]:
                    print(error)
            return False
        return True

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            self.log("info", func.__name__, f"Starting function call '{func.__name__}'", result="N/A")
            if self.arg_validator is not None:
                self.arg_validator(self, **kwargs)
            self.func_args = args
            self.func_kwargs = kwargs
            with self._recreate_context_manager():
                sig = inspect.signature(func)
                if "context" in sig.parameters or "kwargs" in sig.parameters:
                    return func(*args, **kwargs, context=self)
                return func(*args, **kwargs)

        return wrapper

    def _recreate_context_manager(self):
        return self

    def log(self, level: str, operation: str, message: str = "", result: str = "OK"):
        self.state["log"].append({
            "level": level,
            "operation": operation,
            "message": message,
            "result": result
        })

    def set_error(self, error_msg: str, exception: Exception):
        self.state["errors"].append({
            "error_type": type(exception).__name__,
            "error_message": error_msg,
            "exception": exception
        })

    def errors(self) -> dict:
        return {"errors": self.state["errors"]}

    def logs(self) -> dict:
        return {"logs": self.state["log"]}
