from datetime import date

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

    def logs(self, threshold: str | None = None, results: int = 0) -> list:

        if not threshold or threshold not in constants.LOG_LEVELS:
            threshold = constants.LOG_INFO

        log = self._filter_logs(threshold=threshold)

        if results > 0:
            return log[-results:]

        return log

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
            datamodell: str | None = None,
            beskrivelse: str | None = None,
            navn_nb: str | None = None,
            navn_nn: str | None = None,
            navn_en: str | None = None,
            infoside: str | None = None,
            eier: str | None = None,
            kun_sky: bool = False,
            gyldig_til: date | None = None,
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
            periode_type: str | None = None,
            periode_nr: int | None = None,
            periode_aar: int | None = None,
            periode_dato: date | None = None,
            delreg_nr: int | None = None,
            enhet_type: str | None = None,
            vis_oppgavebyrde: str | None = "N",
            vis_brukeropplevelse: str | None = "N",
            altinn_tilgjengelig: date | None = None,
            altinn_svarfrist: date | None = None,
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


    def _filter_logs(self, threshold: str) -> list:
        limit = constants.LOG_LEVELS.index(threshold)

        filtered = []

        for log_entry in self.operations_log:
            logs = log_entry["logs"]
            if len(logs) == 0:
                continue
            for entry in logs:
                if constants.LOG_LEVELS.index(entry["level"]) < limit:
                    continue
                filtered.append(entry)

        return sorted(filtered, key=lambda x: x["time"])
