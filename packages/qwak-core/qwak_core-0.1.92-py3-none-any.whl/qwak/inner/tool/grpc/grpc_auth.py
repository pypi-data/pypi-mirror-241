from typing import Optional, Sequence, Tuple, Union

import grpc
from grpc._interceptor import _ClientCallDetails
from qwak.inner.tool.auth import Auth0ClientBase

_SIGNATURE_HEADER_KEY = "authorization"


class Auth0Client(grpc.AuthMetadataPlugin, Auth0ClientBase):
    def __init__(self):
        from qwak.inner.di_configuration import UserAccountConfiguration

        user_account = UserAccountConfiguration().get_user_config()
        api_key = user_account.api_key

        Auth0ClientBase.__init__(self, api_key=api_key)

    def __call__(self, context, callback):
        callback(((_SIGNATURE_HEADER_KEY, "Bearer {}".format(self.get_token())),), None)


class ForceTokenInterceptor(grpc.UnaryUnaryClientInterceptor):
    def __init__(self):
        from qwak.inner.di_configuration import UserAccountConfiguration

        user_account = UserAccountConfiguration().get_user_config()
        api_key = user_account.api_key

        self.auth_client = Auth0ClientBase(api_key=api_key)

    def concat_metadata(
        self, call_details_metadata: Optional[Sequence[Tuple[str, Union[str, bytes]]]]
    ):
        token_header: Tuple = (
            (_SIGNATURE_HEADER_KEY, "Bearer {}".format(self.auth_client.get_token())),
        )
        return token_header + (call_details_metadata if call_details_metadata else ())

    def intercept_unary_unary(self, continuation, client_call_details, request):
        intercepted_metadata = self.concat_metadata(client_call_details.metadata)
        new_call_details = _ClientCallDetails(
            **{**client_call_details._asdict(), **{"metadata": intercepted_metadata}}
        )
        return continuation(new_call_details, request)
