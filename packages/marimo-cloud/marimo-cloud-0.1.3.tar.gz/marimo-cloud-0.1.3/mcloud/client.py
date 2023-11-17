import json
from typing import IO

from mcloud.auth import get_access_token
from mcloud.constants import API_URL
from mcloud.generated.client import MarimoV1Client
from mcloud.generated.resources.marimo_v_1.types.application import (
    Application,
)
from mcloud.generated.resources.marimo_v_1.types.application_id import ApplicationId
from mcloud.generated.resources.marimo_v_1.types.create_application_request import (
    CreateApplicationRequest,
)
from mcloud.generated.resources.marimo_v_1.types.deployment import (
    Deployment,
)


def create_marimo_client(dryrun: bool = False) -> MarimoV1Client:
    """
    Creates a MarimoV1Client with the default API_URL and access token.
    """
    if dryrun:
        return DryRunMarimoClient(environment=API_URL, token=get_access_token())
    return MarimoV1Client(environment=API_URL, token=get_access_token())


class DryRunMarimoClient(MarimoV1Client):
    def __init__(self, environment: str, token: str):
        super().__init__(environment=environment, token=token)

    def create_deployment(
        self,
        *,
        application_id: ApplicationId,
        code: str,
        requirements_txt: str,
        assets: IO[bytes],
    ) -> Deployment:
        print(
            "create_deployment",
        )
        print(
            json.dumps(
                {
                    "application_id": application_id,
                    "code": code[:100],
                    "requirements_txt": requirements_txt,
                },
                indent=2,
            )
        )
        return Deployment(
            id="dryrun",
            application_id=application_id,
            deployment_id="dryrun-deployment-id",
            started_at="2023-01-01T00:00:00Z",
            status="queued",
        )

    def create_application(self, *, request: CreateApplicationRequest) -> Application:
        print("create_application")
        print(json.dumps(request))
        return Application(
            id="dryrun",
            name=request.name,
        )
