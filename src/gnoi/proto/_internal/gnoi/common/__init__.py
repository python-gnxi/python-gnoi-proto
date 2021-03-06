# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: github.com/openconfig/gnoi/common/common.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .. import types as _types__


class RemoteDownloadProtocol(betterproto.Enum):
    UNKNOWN = 0
    SFTP = 1
    HTTP = 2
    HTTPS = 3
    SCP = 4


@dataclass
class RemoteDownload(betterproto.Message):
    """
    RemoteDownload defines the details for a device to initiate a file transfer
    from or to a remote location.
    """

    # The path information containing where to download the data from or to. For
    # HTTP(S), this will be the URL (i.e. foo.com/file.tbz2). For SFTP and SCP,
    # this will be the address:/path/to/file (i.e. host.foo.com:/bar/baz).
    path: str = betterproto.string_field(1)
    protocol: "RemoteDownloadProtocol" = betterproto.enum_field(2)
    credentials: _types__.Credentials = betterproto.message_field(3)
