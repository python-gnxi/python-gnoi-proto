# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: github.com/openconfig/gnoi/bgp/bgp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto
import grpclib


class ClearBgpNeighborRequestMode(betterproto.Enum):
    SOFT = 0
    SOFTIN = 1
    HARD = 2


@dataclass
class ClearBgpNeighborRequest(betterproto.Message):
    address: str = betterproto.string_field(1)
    # Routing instance containing the neighbor. Defaults to the global routing
    # table.
    routing_instance: str = betterproto.string_field(2)
    mode: "ClearBgpNeighborRequestMode" = betterproto.enum_field(3)


@dataclass
class ClearBgpNeighborResponse(betterproto.Message):
    pass


class BgpStub(betterproto.ServiceStub):
    async def clear_bgp_neighbor(self) -> ClearBgpNeighborResponse:
        """ClearBGPNeighbor clears a BGP session."""

        request = ClearBgpNeighborRequest()

        return await self._unary_unary(
            "/gnoi.bgp.BGP/ClearBGPNeighbor", request, ClearBgpNeighborResponse
        )
