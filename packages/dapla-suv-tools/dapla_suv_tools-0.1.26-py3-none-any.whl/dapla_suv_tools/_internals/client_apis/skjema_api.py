from datetime import date
import json

from ssb_altinn3_util.models.skjemadata.skjemadata_request_models import SkjemaRequestModel

from dapla_suv_tools._internals.integration import api_client
from dapla_suv_tools._internals.integration import user_tools
from dapla_suv_tools._internals.util.operation_result import OperationResult
from dapla_suv_tools._internals.util.suv_operation_context import SuvOperationContext
from dapla_suv_tools._internals.util.validators import skjema_id_validator, ra_nummer_validator
from dapla_suv_tools.pagination import PaginationInfo


SKJEMA_PATH = "/skjemadata/skjema"


@SuvOperationContext(validator=skjema_id_validator)
def get_skjema_by_id(*, skjema_id: int, context: SuvOperationContext = None) -> OperationResult:
    try:
        content: str = api_client._get(path=f"{SKJEMA_PATH}/{skjema_id}", context=context)
        content_json = json.loads(content)
        # context.log(constants.LOG_INFO, "get_skjema_by_id", f"Fetched 'skjema' with id '{skjema_id}'")
        context.log(message="Fetched 'skjema' with id '{skjema_id}'")
        return OperationResult(value=content_json, log=context.logs())

    except Exception as e:
        context.set_error(f"Failed to fetch for id {skjema_id}", e)
        return OperationResult(success=False, value=context.errors(), log=context.logs())


def _get_non_paged_result(path: str, max_results: int, filters: str, context: SuvOperationContext) -> str:
    if max_results > 0:
        return api_client._post(
            path=f"{path}?size={max_results}&order_by=versjon&asc=false", body_json=filters, context=context
        )

    items = []
    total = 1
    page = 1

    while len(items) < total:
        response = api_client._post(
            path=f"{path}?page={page}&size=100&order_by=versjon&asc=false", body_json=filters, context=context
        )

        response_json = json.loads(response)
        total = int(response_json["total"])
        items.extend(response_json["results"])
        page += 1

    return json.dumps({"results": items})


def _get_paged_result(path: str, paging: PaginationInfo, filters: str, context: SuvOperationContext) -> str:
    return api_client._post(
        path=f"{path}?page={paging.page}&size={paging.size}&order_by=versjon&asc=false",
        body_json=filters,
        context=context
    )


@SuvOperationContext(validator=ra_nummer_validator)
def get_skjema_by_ra_nummer(
        *,
        ra_nummer: str,
        max_results: int = 0,
        latest_only: bool = False,
        paging: PaginationInfo = None,
        context: SuvOperationContext = None
) -> OperationResult:
    try:
        filters = json.dumps({"ra_nummer": ra_nummer})
        content: str
        if paging is None:
            content = _get_non_paged_result(
                path="/skjemadata/skjema_paged", max_results=max_results, filters=filters, context=context
            )
        else:
            content = _get_paged_result(path="/skjemadata/skjema_paged", paging=paging, filters=filters, context=context)

        result: dict = json.loads(content)

        if latest_only:
            # context.log(constants.LOG_INFO, "get_skjema_by_ra_number", f"Fetched latest version of 'skjema' with RA-number '{ra_nummer}'")
            context.log(message=f"Fetched latest version of 'skjema' with RA-number '{ra_nummer}'")
            return OperationResult(value=result["results"][0], log=context.logs())

        # context.log(constants.LOG_INFO, "get_skjema_by_ra_number", f"Fetched all 'skjema' with RA-number '{ra_nummer}'")
        context.log(message="Fetched all 'skjema' with RA-number '{ra_nummer}'")
        return OperationResult(value=result["results"], log=context.logs())

    except Exception as e:
        context.set_error(f"Failed to fetch for ra_nummer '{ra_nummer}'.", e)
        return OperationResult(success=False, value=context.errors(), log=context.logs())


@SuvOperationContext(validator=ra_nummer_validator)
def create_skjema(
        *,
        ra_nummer: str,
        versjon: int,
        undersokelse_nr: str,
        gyldig_fra: date,
        datamodell: str | None = None,
        beskrivelse: str | None = None,
        navn_nb: str | None = None,
        navn_nn: str | None = None,
        navn_en: str | None = None,
        infoside: str | None = None,
        eier: str | None = None,
        kun_sky: bool = False,
        gyldig_til: date |None = None,
        context: SuvOperationContext = None
) -> OperationResult:

    user: str = user_tools.get_current_user(context)

    model = SkjemaRequestModel(
        ra_nummer=ra_nummer,
        versjon=versjon,
        undersokelse_nr=undersokelse_nr,
        gyldig_fra=gyldig_fra,
        gyldig_til=gyldig_til,
        endret_av=user,
        datamodell=datamodell,
        beskrivelse=beskrivelse,
        navn_nb=navn_nb,
        navn_nn=navn_nn,
        navn_en=navn_en,
        infoside=infoside,
        eier=eier,
        kun_sky="J" if kun_sky else "N"
    )

    try:
        body = model.model_dump_json()
        content: str = api_client._post(path=SKJEMA_PATH, body_json=body, context=context)
        new_id = json.loads(content)["id"]
        # context.log(constants.LOG_INFO, "create_skjema", f"Created 'skjema' with id '{new_id}'")
        context.log(message="Created 'skjema' with id '{new_id}'")
        return OperationResult(value={"id": new_id}, log=context.logs())
    except Exception as e:
        context.set_error(f"Failed to create for ra_number '{ra_nummer}' - version '{versjon}'", e)
        return OperationResult(success=False, value=context.errors(), log=context.logs())


@SuvOperationContext(validator=skjema_id_validator)
def delete_skjema(*, skjema_id: int, context: SuvOperationContext = None) -> OperationResult:
    try:
        content: str = api_client._delete(path=f"{SKJEMA_PATH}/{skjema_id}", context=context)
        # context.log(constants.LOG_INFO, "delete_skjema", f"Deleted 'skjema' with id '{skjema_id}'")
        context.log(message="Deleted 'skjema' with id '{skjema_id}'")
        return OperationResult(value=content, log=context.logs())
    except Exception as e:
        context.set_error(f"Failed to delete skjema with id '{skjema_id}'.", e)
        return OperationResult(success=False, value=context.errors(), log=context.logs())
