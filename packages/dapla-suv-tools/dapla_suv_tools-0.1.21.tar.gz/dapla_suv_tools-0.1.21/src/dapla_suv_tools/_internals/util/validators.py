import re
from dapla_suv_tools._internals.util.suv_operation_context import SuvOperationContext


ra_pattern = re.compile("^[rR][aA]-[0-9]{4}$")


def skjema_id_validator(ctx: SuvOperationContext, **kwargs):
    skjema_id = kwargs.get("skjema_id", -1)

    if not isinstance(skjema_id, int) or skjema_id == -1:
        raise _set_error(ctx, "Parameter 'skjema_id' must be a valid positive integer.")


def ra_nummer_validator(ctx: SuvOperationContext, **kwargs):
    ra_nummer = kwargs.get("ra_nummer", None)

    if not isinstance(ra_nummer, str):
        raise _set_error(ctx, "Parameter 'ra_nummer' must be a valid positive integer.")

    if not re.match(ra_pattern, ra_nummer):
        raise _set_error(ctx, "Parameter 'ra_nummer' must match pattern 'ra-XXXX' or 'RA-XXXX' (X = digit 0-9)")


def periode_id_validator(ctx: SuvOperationContext, **kwargs):
    periode_id = kwargs.get("periode_id", -1)

    if not isinstance(periode_id, int) or periode_id == -1:
        raise _set_error(ctx, "Parameter 'periode_id' must be a valid positive integer.")


def _set_error(ctx: SuvOperationContext, message: str) -> Exception:
    ex = ValueError("Parameter 'skjema_id' must be a valid positive integer.")
    ctx.set_error(
        error_msg=message,
        exception=ex
    )

    return ex
