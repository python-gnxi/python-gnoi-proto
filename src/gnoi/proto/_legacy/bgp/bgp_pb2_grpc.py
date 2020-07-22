# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from gnoi.proto._legacy.bgp import bgp_pb2 as gnoi_dot_proto_dot___legacy_dot_bgp_dot_bgp__pb2


class BGPStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ClearBGPNeighbor = channel.unary_unary(
                '/gnoi.bgp.BGP/ClearBGPNeighbor',
                request_serializer=gnoi_dot_proto_dot___legacy_dot_bgp_dot_bgp__pb2.ClearBGPNeighborRequest.SerializeToString,
                response_deserializer=gnoi_dot_proto_dot___legacy_dot_bgp_dot_bgp__pb2.ClearBGPNeighborResponse.FromString,
                )


class BGPServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ClearBGPNeighbor(self, request, context):
        """ClearBGPNeighbor clears a BGP session.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BGPServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ClearBGPNeighbor': grpc.unary_unary_rpc_method_handler(
                    servicer.ClearBGPNeighbor,
                    request_deserializer=gnoi_dot_proto_dot___legacy_dot_bgp_dot_bgp__pb2.ClearBGPNeighborRequest.FromString,
                    response_serializer=gnoi_dot_proto_dot___legacy_dot_bgp_dot_bgp__pb2.ClearBGPNeighborResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'gnoi.bgp.BGP', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class BGP(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ClearBGPNeighbor(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gnoi.bgp.BGP/ClearBGPNeighbor',
            gnoi_dot_proto_dot___legacy_dot_bgp_dot_bgp__pb2.ClearBGPNeighborRequest.SerializeToString,
            gnoi_dot_proto_dot___legacy_dot_bgp_dot_bgp__pb2.ClearBGPNeighborResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
