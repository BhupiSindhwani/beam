# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from . import api_pb2 as api__pb2


class PlaygroundServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RunCode = channel.unary_unary(
                '/api.v1.PlaygroundService/RunCode',
                request_serializer=api__pb2.RunCodeRequest.SerializeToString,
                response_deserializer=api__pb2.RunCodeResponse.FromString,
                )
        self.CheckStatus = channel.unary_unary(
                '/api.v1.PlaygroundService/CheckStatus',
                request_serializer=api__pb2.CheckStatusRequest.SerializeToString,
                response_deserializer=api__pb2.CheckStatusResponse.FromString,
                )
        self.GetRunOutput = channel.unary_unary(
                '/api.v1.PlaygroundService/GetRunOutput',
                request_serializer=api__pb2.GetRunOutputRequest.SerializeToString,
                response_deserializer=api__pb2.GetRunOutputResponse.FromString,
                )
        self.GetRunError = channel.unary_unary(
                '/api.v1.PlaygroundService/GetRunError',
                request_serializer=api__pb2.GetRunErrorRequest.SerializeToString,
                response_deserializer=api__pb2.GetRunErrorResponse.FromString,
                )
        self.GetCompileOutput = channel.unary_unary(
                '/api.v1.PlaygroundService/GetCompileOutput',
                request_serializer=api__pb2.GetCompileOutputRequest.SerializeToString,
                response_deserializer=api__pb2.GetCompileOutputResponse.FromString,
                )
        self.GetListOfExamples = channel.unary_unary(
                '/api.v1.PlaygroundService/GetListOfExamples',
                request_serializer=api__pb2.GetListOfExamplesRequest.SerializeToString,
                response_deserializer=api__pb2.GetListOfExamplesResponse.FromString,
                )
        self.GetExample = channel.unary_unary(
                '/api.v1.PlaygroundService/GetExample',
                request_serializer=api__pb2.GetExampleRequest.SerializeToString,
                response_deserializer=api__pb2.GetExampleResponse.FromString,
                )
        self.GetExampleOutput = channel.unary_unary(
                '/api.v1.PlaygroundService/GetExampleOutput',
                request_serializer=api__pb2.GetExampleRequest.SerializeToString,
                response_deserializer=api__pb2.GetRunOutputResponse.FromString,
                )


class PlaygroundServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def RunCode(self, request, context):
        """Submit the job for an execution and get the pipeline uuid.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckStatus(self, request, context):
        """Get the status of pipeline execution.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRunOutput(self, request, context):
        """Get the result of pipeline execution.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRunError(self, request, context):
        """Get the error of pipeline execution.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCompileOutput(self, request, context):
        """Get the result of pipeline compilation.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetListOfExamples(self, request, context):
        """Get the list of precompiled examples.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetExample(self, request, context):
        """Get the code of an example.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetExampleOutput(self, request, context):
        """Get the precompiled details of an example.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PlaygroundServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RunCode': grpc.unary_unary_rpc_method_handler(
                    servicer.RunCode,
                    request_deserializer=api__pb2.RunCodeRequest.FromString,
                    response_serializer=api__pb2.RunCodeResponse.SerializeToString,
            ),
            'CheckStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckStatus,
                    request_deserializer=api__pb2.CheckStatusRequest.FromString,
                    response_serializer=api__pb2.CheckStatusResponse.SerializeToString,
            ),
            'GetRunOutput': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRunOutput,
                    request_deserializer=api__pb2.GetRunOutputRequest.FromString,
                    response_serializer=api__pb2.GetRunOutputResponse.SerializeToString,
            ),
            'GetRunError': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRunError,
                    request_deserializer=api__pb2.GetRunErrorRequest.FromString,
                    response_serializer=api__pb2.GetRunErrorResponse.SerializeToString,
            ),
            'GetCompileOutput': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCompileOutput,
                    request_deserializer=api__pb2.GetCompileOutputRequest.FromString,
                    response_serializer=api__pb2.GetCompileOutputResponse.SerializeToString,
            ),
            'GetListOfExamples': grpc.unary_unary_rpc_method_handler(
                    servicer.GetListOfExamples,
                    request_deserializer=api__pb2.GetListOfExamplesRequest.FromString,
                    response_serializer=api__pb2.GetListOfExamplesResponse.SerializeToString,
            ),
            'GetExample': grpc.unary_unary_rpc_method_handler(
                    servicer.GetExample,
                    request_deserializer=api__pb2.GetExampleRequest.FromString,
                    response_serializer=api__pb2.GetExampleResponse.SerializeToString,
            ),
            'GetExampleOutput': grpc.unary_unary_rpc_method_handler(
                    servicer.GetExampleOutput,
                    request_deserializer=api__pb2.GetExampleRequest.FromString,
                    response_serializer=api__pb2.GetRunOutputResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'api.v1.PlaygroundService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PlaygroundService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def RunCode(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1.PlaygroundService/RunCode',
            api__pb2.RunCodeRequest.SerializeToString,
            api__pb2.RunCodeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CheckStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1.PlaygroundService/CheckStatus',
            api__pb2.CheckStatusRequest.SerializeToString,
            api__pb2.CheckStatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetRunOutput(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1.PlaygroundService/GetRunOutput',
            api__pb2.GetRunOutputRequest.SerializeToString,
            api__pb2.GetRunOutputResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetRunError(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1.PlaygroundService/GetRunError',
            api__pb2.GetRunErrorRequest.SerializeToString,
            api__pb2.GetRunErrorResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetCompileOutput(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1.PlaygroundService/GetCompileOutput',
            api__pb2.GetCompileOutputRequest.SerializeToString,
            api__pb2.GetCompileOutputResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetListOfExamples(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1.PlaygroundService/GetListOfExamples',
            api__pb2.GetListOfExamplesRequest.SerializeToString,
            api__pb2.GetListOfExamplesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetExample(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1.PlaygroundService/GetExample',
            api__pb2.GetExampleRequest.SerializeToString,
            api__pb2.GetExampleResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetExampleOutput(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1.PlaygroundService/GetExampleOutput',
            api__pb2.GetExampleRequest.SerializeToString,
            api__pb2.GetRunOutputResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
