from dapla.auth import AuthClient


def get_access_token() -> str:
    return AuthClient.fetch_personal_token()


def get_current_user() -> str:
    local_user = AuthClient.fetch_local_user()
    return local_user["username"]