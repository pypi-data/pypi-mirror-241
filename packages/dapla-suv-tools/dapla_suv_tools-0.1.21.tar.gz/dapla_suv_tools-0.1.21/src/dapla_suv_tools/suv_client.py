from datetime import date
from typing import Optional
import dapla_suv_tools._internals.client_apis.skjema_api as skjema_api
from dapla_suv_tools._internals.client_apis import periode_api
from dapla_suv_tools._internals.util.operation_result import OperationResult
from dapla_suv_tools._internals.util import constants
from dapla_suv_tools.pagination import PaginationInfo


class SuvClient:
    suppress_exceptions: bool
    operations_log: list

    def __init__(self, suppress_exceptions: bool = False):
        self.suppress_exceptions = suppress_exceptions
        self.operations_log = []

    def logs(self) -> list:
        return self.operations_log

    def flush_logs(self):
        self.operations_log = []

    # Skjema

    def get_skjema_by_id(self, *, skjema_id: int) -> dict:
        result = skjema_api.get_skjema_by_id(skjema_id=skjema_id)
        return self._process_result(result=result)

    def get_skjema_by_ra_nummer(
            self,
            *,
            ra_nummer: str,
            latest_only: bool = False,
            paginatipn_info: PaginationInfo = None) -> dict:
        result = skjema_api.get_skjema_by_ra_nummer(ra_nummer=ra_nummer, latest_only=latest_only, paging=paginatipn_info)
        return self._process_result(result=result)

    def create_skjema(
            self,
            *,
            ra_nummer: str,
            versjon: int,
            undersokelse_nr: str,
            gyldig_fra: date,
            endret_av: str,
            datamodell: Optional[str] = None,
            beskrivelse: Optional[str] = None,
            navn_nb: Optional[str] = None,
            navn_nn: Optional[str] = None,
            navn_en: Optional[str] = None,
            infoside: Optional[str] = None,
            eier: Optional[str] = None,
            kun_sky: bool = False,
            gyldig_til: Optional[date] = None,
    ) -> dict:
        fwd_args = {k: v for k,v in locals().items() if k not in {"self", "*"}}

        result = skjema_api.create_skjema(**fwd_args)
        return self._process_result(result=result)

    def delete_skjema(self, skjema_id: int) -> dict:
        result = skjema_api.delete_skjema(skjema_id=skjema_id)
        return self._process_result(result=result)

    # Periode

    def get_periode_by_id(self, *, periode_id: int) -> dict:
        result = periode_api.get_periode_by_id(periode_id=periode_id)
        return self._process_result(result=result)

    def get_perioder_by_skjema_id(self, *, skjema_id: int) -> dict:
        result = periode_api.get_perioder_by_skjema_id(skjema_id=skjema_id)
        return self._process_result(result=result)

    def create_periode(
            self,
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
    ) -> dict:
        fwd_args = {k: v for k, v in locals().items() if k not in {"self", "*"}}
        result = periode_api.create_periode(**fwd_args)
        return self._process_result(result=result)

    def delete_periode(self, *, periode_id: int) -> dict:
        result = periode_api.delete_periode(periode_id=periode_id)
        return self._process_result(result=result)

    def _process_result(self, result: OperationResult) -> dict:
        self.operations_log.append(result.operation_log)
        if result.result == constants.OPERATION_OK:
            return result.result_json

        if result.result == constants.OPERATION_ERROR:
            if self.suppress_exceptions:
                return result.result_json
            errors = result.result_json["errors"]
            raise errors[len(errors) - 1]["exception"]

        return {"result": "Undefined result.  This shouldn't happen."}
