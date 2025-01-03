# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import recommendation_service_pb2 as recommendation__service__pb2


class RecommendationServiceStub(object):
    """Recommendation Service
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetRecommendations = channel.unary_unary(
                '/recommendation.RecommendationService/GetRecommendations',
                request_serializer=recommendation__service__pb2.RecommendationRequest.SerializeToString,
                response_deserializer=recommendation__service__pb2.RecommendationResponse.FromString,
                )


class RecommendationServiceServicer(object):
    """Recommendation Service
    """

    def GetRecommendations(self, request, context):
        """RPC to get recommendations
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RecommendationServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetRecommendations': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRecommendations,
                    request_deserializer=recommendation__service__pb2.RecommendationRequest.FromString,
                    response_serializer=recommendation__service__pb2.RecommendationResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'recommendation.RecommendationService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RecommendationService(object):
    """Recommendation Service
    """

    @staticmethod
    def GetRecommendations(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/recommendation.RecommendationService/GetRecommendations',
            recommendation__service__pb2.RecommendationRequest.SerializeToString,
            recommendation__service__pb2.RecommendationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
