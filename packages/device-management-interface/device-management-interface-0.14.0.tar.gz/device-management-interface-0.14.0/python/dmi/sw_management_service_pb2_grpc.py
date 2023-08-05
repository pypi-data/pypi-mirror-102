# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from dmi import hw_pb2 as dmi_dot_hw__pb2
from dmi import sw_image_pb2 as dmi_dot_sw__image__pb2
from dmi import sw_management_service_pb2 as dmi_dot_sw__management__service__pb2


class NativeSoftwareManagementServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetSoftwareVersion = channel.unary_unary(
                '/dmi.NativeSoftwareManagementService/GetSoftwareVersion',
                request_serializer=dmi_dot_hw__pb2.HardwareID.SerializeToString,
                response_deserializer=dmi_dot_sw__management__service__pb2.GetSoftwareVersionInformationResponse.FromString,
                )
        self.DownloadImage = channel.unary_stream(
                '/dmi.NativeSoftwareManagementService/DownloadImage',
                request_serializer=dmi_dot_sw__management__service__pb2.DownloadImageRequest.SerializeToString,
                response_deserializer=dmi_dot_sw__image__pb2.ImageStatus.FromString,
                )
        self.ActivateImage = channel.unary_stream(
                '/dmi.NativeSoftwareManagementService/ActivateImage',
                request_serializer=dmi_dot_hw__pb2.HardwareID.SerializeToString,
                response_deserializer=dmi_dot_sw__image__pb2.ImageStatus.FromString,
                )
        self.RevertToStandbyImage = channel.unary_stream(
                '/dmi.NativeSoftwareManagementService/RevertToStandbyImage',
                request_serializer=dmi_dot_hw__pb2.HardwareID.SerializeToString,
                response_deserializer=dmi_dot_sw__image__pb2.ImageStatus.FromString,
                )
        self.UpdateStartupConfiguration = channel.unary_stream(
                '/dmi.NativeSoftwareManagementService/UpdateStartupConfiguration',
                request_serializer=dmi_dot_sw__management__service__pb2.ConfigRequest.SerializeToString,
                response_deserializer=dmi_dot_sw__management__service__pb2.ConfigResponse.FromString,
                )
        self.GetStartupConfigurationInfo = channel.unary_unary(
                '/dmi.NativeSoftwareManagementService/GetStartupConfigurationInfo',
                request_serializer=dmi_dot_sw__management__service__pb2.StartupConfigInfoRequest.SerializeToString,
                response_deserializer=dmi_dot_sw__management__service__pb2.StartupConfigInfoResponse.FromString,
                )


class NativeSoftwareManagementServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetSoftwareVersion(self, request, context):
        """Get the software version information of the Active and Standby images
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DownloadImage(self, request, context):
        """Downloads and installs the image in the standby partition, returns the status/progress of the Install
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ActivateImage(self, request, context):
        """Activates and runs the OLT with the image in the standby partition. If things are fine this image will
        henceforth be marked as the Active Partition. The old working image would remain on the Standby partition.
        Any possibly required (sub-)steps like "commit" are left to the "Device Manager"
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RevertToStandbyImage(self, request, context):
        """Marks the image in the Standby as Active and reboots the device, so that it boots from that image which was in the standby.
        This API is to be used if operator wants to go back to the previous software
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateStartupConfiguration(self, request, context):
        """This API can be used to let the devices pickup their properitary configuration which they need at startup.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetStartupConfigurationInfo(self, request, context):
        """This API can be used to retrieve information about the current startup configuration that a device is using
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NativeSoftwareManagementServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetSoftwareVersion': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSoftwareVersion,
                    request_deserializer=dmi_dot_hw__pb2.HardwareID.FromString,
                    response_serializer=dmi_dot_sw__management__service__pb2.GetSoftwareVersionInformationResponse.SerializeToString,
            ),
            'DownloadImage': grpc.unary_stream_rpc_method_handler(
                    servicer.DownloadImage,
                    request_deserializer=dmi_dot_sw__management__service__pb2.DownloadImageRequest.FromString,
                    response_serializer=dmi_dot_sw__image__pb2.ImageStatus.SerializeToString,
            ),
            'ActivateImage': grpc.unary_stream_rpc_method_handler(
                    servicer.ActivateImage,
                    request_deserializer=dmi_dot_hw__pb2.HardwareID.FromString,
                    response_serializer=dmi_dot_sw__image__pb2.ImageStatus.SerializeToString,
            ),
            'RevertToStandbyImage': grpc.unary_stream_rpc_method_handler(
                    servicer.RevertToStandbyImage,
                    request_deserializer=dmi_dot_hw__pb2.HardwareID.FromString,
                    response_serializer=dmi_dot_sw__image__pb2.ImageStatus.SerializeToString,
            ),
            'UpdateStartupConfiguration': grpc.unary_stream_rpc_method_handler(
                    servicer.UpdateStartupConfiguration,
                    request_deserializer=dmi_dot_sw__management__service__pb2.ConfigRequest.FromString,
                    response_serializer=dmi_dot_sw__management__service__pb2.ConfigResponse.SerializeToString,
            ),
            'GetStartupConfigurationInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStartupConfigurationInfo,
                    request_deserializer=dmi_dot_sw__management__service__pb2.StartupConfigInfoRequest.FromString,
                    response_serializer=dmi_dot_sw__management__service__pb2.StartupConfigInfoResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'dmi.NativeSoftwareManagementService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class NativeSoftwareManagementService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetSoftwareVersion(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dmi.NativeSoftwareManagementService/GetSoftwareVersion',
            dmi_dot_hw__pb2.HardwareID.SerializeToString,
            dmi_dot_sw__management__service__pb2.GetSoftwareVersionInformationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DownloadImage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/dmi.NativeSoftwareManagementService/DownloadImage',
            dmi_dot_sw__management__service__pb2.DownloadImageRequest.SerializeToString,
            dmi_dot_sw__image__pb2.ImageStatus.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ActivateImage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/dmi.NativeSoftwareManagementService/ActivateImage',
            dmi_dot_hw__pb2.HardwareID.SerializeToString,
            dmi_dot_sw__image__pb2.ImageStatus.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RevertToStandbyImage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/dmi.NativeSoftwareManagementService/RevertToStandbyImage',
            dmi_dot_hw__pb2.HardwareID.SerializeToString,
            dmi_dot_sw__image__pb2.ImageStatus.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateStartupConfiguration(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/dmi.NativeSoftwareManagementService/UpdateStartupConfiguration',
            dmi_dot_sw__management__service__pb2.ConfigRequest.SerializeToString,
            dmi_dot_sw__management__service__pb2.ConfigResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetStartupConfigurationInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dmi.NativeSoftwareManagementService/GetStartupConfigurationInfo',
            dmi_dot_sw__management__service__pb2.StartupConfigInfoRequest.SerializeToString,
            dmi_dot_sw__management__service__pb2.StartupConfigInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
