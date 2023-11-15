"""
Type annotations for sso-oidc service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sso_oidc/type_defs/)

Usage::

    ```python
    from mypy_boto3_sso_oidc.type_defs import CreateTokenRequestRequestTypeDef

    data: CreateTokenRequestRequestTypeDef = ...
    ```
"""

import sys
from typing import Dict, Sequence

if sys.version_info >= (3, 12):
    from typing import NotRequired
else:
    from typing_extensions import NotRequired
if sys.version_info >= (3, 12):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CreateTokenRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "RegisterClientRequestRequestTypeDef",
    "StartDeviceAuthorizationRequestRequestTypeDef",
    "CreateTokenResponseTypeDef",
    "RegisterClientResponseTypeDef",
    "StartDeviceAuthorizationResponseTypeDef",
)

CreateTokenRequestRequestTypeDef = TypedDict(
    "CreateTokenRequestRequestTypeDef",
    {
        "clientId": str,
        "clientSecret": str,
        "grantType": str,
        "deviceCode": NotRequired[str],
        "code": NotRequired[str],
        "refreshToken": NotRequired[str],
        "scope": NotRequired[Sequence[str]],
        "redirectUri": NotRequired[str],
    },
)
ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, str],
        "RetryAttempts": int,
    },
)
RegisterClientRequestRequestTypeDef = TypedDict(
    "RegisterClientRequestRequestTypeDef",
    {
        "clientName": str,
        "clientType": str,
        "scopes": NotRequired[Sequence[str]],
    },
)
StartDeviceAuthorizationRequestRequestTypeDef = TypedDict(
    "StartDeviceAuthorizationRequestRequestTypeDef",
    {
        "clientId": str,
        "clientSecret": str,
        "startUrl": str,
    },
)
CreateTokenResponseTypeDef = TypedDict(
    "CreateTokenResponseTypeDef",
    {
        "accessToken": str,
        "tokenType": str,
        "expiresIn": int,
        "refreshToken": str,
        "idToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RegisterClientResponseTypeDef = TypedDict(
    "RegisterClientResponseTypeDef",
    {
        "clientId": str,
        "clientSecret": str,
        "clientIdIssuedAt": int,
        "clientSecretExpiresAt": int,
        "authorizationEndpoint": str,
        "tokenEndpoint": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartDeviceAuthorizationResponseTypeDef = TypedDict(
    "StartDeviceAuthorizationResponseTypeDef",
    {
        "deviceCode": str,
        "userCode": str,
        "verificationUri": str,
        "verificationUriComplete": str,
        "expiresIn": int,
        "interval": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
