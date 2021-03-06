# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: github.com/openconfig/gnoi/factory_reset/reset.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto
import grpclib


@dataclass
class StartRequest(betterproto.Message):
    # Instructs the Target to rollback the OS to the same version as it shipped
    # from factory.
    factory_os: bool = betterproto.bool_field(1)
    # Instructs the Target to zero fill persistent storage state data.
    zero_fill: bool = betterproto.bool_field(2)


@dataclass
class ResetSuccess(betterproto.Message):
    pass


@dataclass
class ResetError(betterproto.Message):
    """Message also used in gRPC status.details field."""

    # Factory OS reset is not supported.
    factory_os_unsupported: bool = betterproto.bool_field(1)
    # Zero fill is not supported.
    zero_fill_unsupported: bool = betterproto.bool_field(2)
    # Unspecified error, must provide detail message.
    other: bool = betterproto.bool_field(3)
    detail: str = betterproto.string_field(4)


@dataclass
class StartResponse(betterproto.Message):
    # Reset will be executed.
    reset_success: "ResetSuccess" = betterproto.message_field(1, group="response")
    # Reset will not be executed.
    reset_error: "ResetError" = betterproto.message_field(2, group="response")


class FactoryResetStub(betterproto.ServiceStub):
    """The FactoryReset service exported by Targets."""

    async def start(
        self, *, factory_os: bool = False, zero_fill: bool = False
    ) -> StartResponse:
        """
        The Start RPC allows the Client to instruct the Target to immediately
        clean all existing state and boot the Target in the same condition as
        it is shipped from factory. State includes storage, configuration,
        logs, certificates and licenses. Optionally allows rolling back the OS
        to the same version shipped from factory. Optionally allows for the
        Target to zero-fill permanent storage where state data is stored. If
        any of the optional flags is set but not supported, a gRPC Status with
        code INVALID_ARGUMENT must be returned with the details value set to a
        properly populated ResetError message.
        """

        request = StartRequest()
        request.factory_os = factory_os
        request.zero_fill = zero_fill

        return await self._unary_unary(
            "/gnoi.factory_reset.FactoryReset/Start", request, StartResponse
        )
