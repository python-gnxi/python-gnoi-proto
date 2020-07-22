# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: github.com/openconfig/gnoi/mpls/mpls.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import AsyncIterator

import betterproto
import grpclib


class ClearLspRequestMode(betterproto.Enum):
    DEFAULT = 0
    NONAGGRESSIVE = 0
    AGGRESSIVE = 1
    RESET = 2
    AUTOBW_AGGRESSIVE = 3
    AUTOBW_NONAGGRESSIVE = 4


class MplsPingRequestReplyMode(betterproto.Enum):
    IPV4 = 0
    ROUTER_ALERT = 1


class MplsPingResponseEchoResponseCode(betterproto.Enum):
    SUCCESS = 0
    NOT_SENT = 1
    TIMEOUT = 2


@dataclass
class ClearLspRequest(betterproto.Message):
    """Request to clear a single tunnel on a target device."""

    name: str = betterproto.string_field(2)
    mode: "ClearLspRequestMode" = betterproto.enum_field(3)


@dataclass
class ClearLspResponse(betterproto.Message):
    pass


@dataclass
class ClearLspCountersRequest(betterproto.Message):
    """Request to clear a single tunnel counters on a target device."""

    name: str = betterproto.string_field(2)


@dataclass
class ClearLspCountersResponse(betterproto.Message):
    pass


@dataclass
class MplsPingPweDestination(betterproto.Message):
    # The address of the egress LER that the MPLS ping should be sent on when
    # destined to a PWE service.
    eler: str = betterproto.string_field(1)
    # The virtual circuit ID for the PWE via which the ping should be sent.
    vcid: int = betterproto.uint32_field(2)


@dataclass
class MplsPingRsvpteDestination(betterproto.Message):
    """
    MPLSPingRSVPTEDestination specifies the destination for an MPLS Ping in
    terms of an absolute specification of an RSVP-TE LSP. It can be used to
    identify an individual RSVP-TE session via which a ping should be sent.
    """

    # The IPv4 or IPv6 address used by the system initiating (acting as the head-
    # end) of the RSVP-TE LSP.
    src: str = betterproto.string_field(1)
    # The IPv4 or IPv6 address used by the system terminating (acting as the
    # tail-end) of the RSVP-TE LSP.
    dst: str = betterproto.string_field(2)
    # The extended tunnel ID of the RSVP-TE LSP, expressed as an unsigned, 32b
    # integer.
    extended_tunnel_id: int = betterproto.uint32_field(3)


@dataclass
class MplsPingRequest(betterproto.Message):
    """
    MPLSPingRequest specifies the parameters that should be used as input from
    the client, to a system that is initiating an RFC4379 MPLS ping request.
    """

    # The LDP forwarding equivalence class that the ping should be sent to
    # expressed as an IPv4 or IPv6 prefix.
    ldp_fec: str = betterproto.string_field(1, group="destination")
    # The FEC129 PWE to which the LSP ping should be sent.
    fec129_pwe: "MplsPingPweDestination" = betterproto.message_field(
        2, group="destination"
    )
    # The name of an RSVP-TE LSP via which the ping should be sent. The system
    # should locally resolve the name to a particular RSVP-TE session.
    rsvpte_lsp_name: str = betterproto.string_field(4, group="destination")
    # An exact specification of an RSVP-TE LSP to which the system should send an
    # MPLS ping message.
    rsvpte_lsp: "MplsPingRsvpteDestination" = betterproto.message_field(
        5, group="destination"
    )
    reply_mode: "MplsPingRequestReplyMode" = betterproto.enum_field(6)
    # The number of MPLS echo request packets to send.
    count: int = betterproto.uint32_field(7)
    # The size (in bytes) of each MPLS echo request packet.
    size: int = betterproto.uint32_field(8)
    # The source IPv4 address that should be used in the request packet.
    source_address: str = betterproto.string_field(9)
    # The MPLS TTL that should be set in the packets sent.
    mpls_ttl: int = betterproto.uint32_field(10)
    # The value of the traffic class (TC, formerly known as EXP) bits that should
    # be set in the MPLS ping packets.
    traffic_class: int = betterproto.uint32_field(11)


@dataclass
class MplsPingResponse(betterproto.Message):
    """
    MPLSPingResponse (MPLSPong?) is sent from the target to the client based on
    each MPLS Echo Response packet it receives associated with an input
    MPLSPing RPC.
    """

    seq: int = betterproto.uint32_field(1)
    # The response that was received from the egress LER.
    response: "MplsPingResponseEchoResponseCode" = betterproto.enum_field(2)
    # The time (in nanoseconds) between transmission of the Echo Response, and
    # the echo reply.
    response_time: int = betterproto.uint64_field(3)


class MplsStub(betterproto.ServiceStub):
    async def clear_lsp(self) -> ClearLspResponse:
        """
        ClearLSP clears a single tunnel (requests for it's route to be
        recalculated).
        """

        request = ClearLspRequest()

        return await self._unary_unary(
            "/gnoi.mpls.MPLS/ClearLSP", request, ClearLspResponse
        )

    async def clear_lsp_counters(self) -> ClearLspCountersResponse:
        """
        ClearLSPCounters will clear the MPLS counters for the provided LSP.
        """

        request = ClearLspCountersRequest()

        return await self._unary_unary(
            "/gnoi.mpls.MPLS/ClearLSPCounters", request, ClearLspCountersResponse
        )

    async def mpls_ping(self) -> AsyncIterator[MplsPingResponse]:
        """An MPLS ping, specified as per RFC4379."""

        request = MplsPingRequest()

        async for response in self._unary_stream(
            "/gnoi.mpls.MPLS/MPLSPing", request, MplsPingResponse,
        ):
            yield response