import concurrent.futures
import typing
from concurrent.futures._base import Future

import requests

from .data import DataFrameFacade
from .models import (
    FabrikReadRequest,
    FabrikReadResponse,
    FabrikWriteRequest,
    FabrikException,
    FabrikRawReadResponse,
    FabrikWriteResponse,
    FabrikRawWriteProfileResponse,
    FabrikRawWriteRequest,
)


def _perform_read(
    endpoint: str,
    req: FabrikReadRequest,
    session: requests.Session,
    df_facade: DataFrameFacade,
) -> FabrikReadResponse:
    try:
        res = session.post(endpoint + "/read", json=req.dict())
        res.raise_for_status()

        fabrik_read_res: FabrikRawReadResponse = FabrikRawReadResponse.parse_obj(
            res.json()
        )

        return FabrikReadResponse(df=df_facade.read_data_frame(fabrik_read_res))

    except Exception as ex:
        raise FabrikException("Failed to execute read request.", ex)
    pass


class FabrikClient(object):
    def __init__(self, endpoint: str, token: str, df_facade: DataFrameFacade):
        self.endpoint = endpoint
        self.token = token
        self.df_facade = df_facade

        self.session = requests.session()
        self.session.headers.update({"authorization": "Bearer " + self.token})

    def read_all(
        self, r: typing.List[FabrikReadRequest]
    ) -> typing.List[FabrikReadResponse]:
        futures: typing.List[Future] = []
        results: typing.List[FabrikReadResponse] = []

        with concurrent.futures.ThreadPoolExecutor() as executor:
            for entry in r:
                futures.append(
                    executor.submit(
                        _perform_read,
                        self.endpoint,
                        entry,
                        self.session,
                        self.df_facade,
                    )
                )

            for f in futures:
                results.append(f.result())

        return results

    def read(self, r: FabrikReadRequest) -> FabrikReadResponse:
        return _perform_read(self.endpoint, r, self.session, self.df_facade)

    def write(self, r: FabrikWriteRequest) -> FabrikWriteResponse:

        res_profile = self.session.post(
            self.endpoint + "/write/profile", json={"reference": "x"}
        )
        res_profile.raise_for_status()

        profile = FabrikRawWriteProfileResponse.parse_obj(res_profile.json())
        self.df_facade.write_data_frame(r.df, profile)

        raw_write_req = FabrikRawWriteRequest(
            path=profile.context["path"] + "results.parquet.snappy",
            warehouse="redshift",
        )

        res_write = self.session.post(
            self.endpoint + "/write", json=raw_write_req.dict()
        )
        res_write.raise_for_status()

        return FabrikWriteResponse(reference="1234")
