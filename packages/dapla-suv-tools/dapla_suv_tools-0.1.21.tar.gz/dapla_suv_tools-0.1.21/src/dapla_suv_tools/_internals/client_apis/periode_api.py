from datetime import date
import json
from typing import Optional

from ssb_altinn3_util.models.skjemadata.skjemadata_request_models import PeriodeRequestModel

from dapla_suv_tools._internals.integration import api_client
from dapla_suv_tools._internals.util.operation_result import OperationResult
from dapla_suv_tools._internals.util.suv_operation_context import SuvOperationContext
from dapla_suv_tools._internals.util.validators import periode_id_validator, skjema_id_validator

PERIODE_PATH = "/skjemadata/periode"


@SuvOperationContext(validator=periode_id_validator)
def get_periode_by_id(*, periode_id: int, context: SuvOperationContext = None) -> OperationResult:
    try:
        content: str = api_client._get(path=f"{PERIODE_PATH}/{periode_id}", context=context)
        content_json = json.loads(content)
        context.log("info", "get_periode_by_id", f"Fetched periode with periode_id '{periode_id}'")

        return OperationResult(value=content_json, log=context.logs())
    except Exception as e:
        context.set_error(f"Failed to fetch for id {periode_id}", e)

        return OperationResult(success=False, value=context.errors(), log=context.logs())


@SuvOperationContext(validator=skjema_id_validator)
def get_perioder_by_skjema_id(*, skjema_id: int, context: SuvOperationContext = None) -> OperationResult:
    try:
        content: str = api_client._get(path=f"{PERIODE_PATH}/skjema/{skjema_id}", context=context)
        content_json = json.loads(content)
        context.log("info", "get_periode_by_skjema_id", f"Fetched perioder for skjema_id '{skjema_id}'")

        return OperationResult(value=content_json, log=context.logs())
    except Exception as e:
        context.set_error(f"Failed to fetch for skjema_id {skjema_id}", e)

        return OperationResult(success=False, value=context.errors(), log=context.logs())


@SuvOperationContext(validator=skjema_id_validator)
def create_periode(
        *,
        skjema_id: int,
        endret_av: str,
        periode_type: Optional[str] = None,
        periode_nr: Optional[int] = None,
        periode_aar: Optional[int] = None,
        periode_dato: Optional[date] = None,
        delreg_nr: Optional[int] = None,
        enhet_type: Optional[str] = None,
        vis_oppgavebyrde: Optional[str] = "N",
        vis_brukeropplevelse: Optional[str] = "N",
        altinn_tilgjengelig: Optional[date] = None,
        altinn_svarfrist: Optional[date] = None,
        context: SuvOperationContext = None
) -> OperationResult:
    model = PeriodeRequestModel(
        skjema_id=skjema_id,
        endret_av=endret_av,
        periode_type=periode_type,
        periode_nr=periode_nr,
        periode_aar=periode_aar,
        periode_dato=periode_dato,
        delreg_nr=delreg_nr,
        enhet_type=enhet_type,
        vis_oppgavebyrde=vis_oppgavebyrde,
        vis_brukeropplevelse=vis_brukeropplevelse,
        altinn_tilgjengelig=altinn_tilgjengelig,
        altinn_svarfrist=altinn_svarfrist
    )

    try:
        body = model.model_dump_json()
        content: str = api_client._post(path=PERIODE_PATH, body_json=body, context=context)
        new_id = json.loads(content)["id"]
        return OperationResult(value={"id": new_id}, log=context.logs())
    except Exception as e:
        context.set_error(
            f"Failed to create for skjema_id '{skjema_id}' - periode {periode_nr} {periode_type} {periode_nr}", e
        )
        return OperationResult(success=False, value=context.errors(), log=context.logs())


def delete_periode(*, periode_id: int, context: SuvOperationContext = None) -> OperationResult:
    try:
        content: str = api_client._delete(path=f"{PERIODE_PATH}/{periode_id}", context=context)
        return OperationResult(value=content, log=context.logs())
    except Exception as e:
        context.set_error(f"Failed to delete Periode with id '{periode_id}'.", e)
        return OperationResult(success=False, value=context.errors(), log=context.logs())
