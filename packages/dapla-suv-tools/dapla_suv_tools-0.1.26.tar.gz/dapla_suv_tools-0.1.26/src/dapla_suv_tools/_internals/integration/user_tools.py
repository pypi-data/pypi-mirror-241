from dapla.auth import AuthClient

from dapla_suv_tools._internals.util.suv_operation_context import SuvOperationContext
from dapla_suv_tools._internals.util import constants


def get_access_token(context: SuvOperationContext) -> str:
    context.log(
        level=constants.LOG_DIAGNOSTIC,
        # operation="get_access_token",
        message="Fetching user access_token"
    )
    return AuthClient.fetch_personal_token()


def get_current_user(context: SuvOperationContext) -> str:
    context.log(
        level=constants.LOG_DIAGNOSTIC,
        # operation="get_current_user",
        message="Fetching username"
    )
    local_user = AuthClient.fetch_local_user()
    return local_user["username"]