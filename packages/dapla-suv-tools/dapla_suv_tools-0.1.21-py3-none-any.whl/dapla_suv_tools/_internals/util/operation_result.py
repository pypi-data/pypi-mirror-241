from typing import Union
from dapla_suv_tools._internals.util import constants


class OperationResult:
    result_json: dict
    result: str
    operation_log: dict

    def __init__(self, value: Union[dict | str], success: bool = True,  log: dict = None):
        if success and isinstance(value, str):
            value = {"result": value}
        self.result = constants.OPERATION_OK if success else constants.OPERATION_ERROR
        self.result_json = value
        self.operation_log = {} if log is None else log
