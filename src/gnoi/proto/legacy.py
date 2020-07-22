from gnoi.proto._legacy.bgp.bgp_pb2 import (  # noqa
    ClearBGPNeighborRequest,
    ClearBGPNeighborResponse,
)
from gnoi.proto._legacy.bgp.bgp_pb2_grpc import BGP, BGPServicer, BGPStub  # noqa
from gnoi.proto._legacy.cert.cert_pb2 import (  # noqa
    CSR,
    CSRParams,
    CanGenerateCSRRequest,
    CanGenerateCSRResponse,
    Certificate,
    CertificateInfo,
    CertificateRevocationError,
    CertificateType,
    Endpoint,
    FinalizeRequest,
    GenerateCSRRequest,
    GenerateCSRResponse,
    GetCertificatesRequest,
    GetCertificatesResponse,
    InstallCertificateRequest,
    InstallCertificateResponse,
    KeyPair,
    KeyType,
    LoadCertificateRequest,
    LoadCertificateResponse,
    RevokeCertificatesRequest,
    RevokeCertificatesResponse,
    RotateCertificateRequest,
    RotateCertificateResponse,
)
from gnoi.proto._legacy.cert.cert_pb2_grpc import (  # noqa
    CertificateManagement,
    CertificateManagementServicer,
    CertificateManagementStub,
)
from gnoi.proto._legacy.common.common_pb2 import RemoteDownload  # noqa
from gnoi.proto._legacy.diag.diag_pb2 import (  # noqa
    BertStatus,
    GetBERTResultRequest,
    GetBERTResultResponse,
    PrbsPolynomial,
    StartBERTRequest,
    StartBERTResponse,
    StopBERTRequest,
    StopBERTResponse,
)
from gnoi.proto._legacy.diag.diag_pb2_grpc import Diag, DiagServicer, DiagStub  # noqa
from gnoi.proto._legacy.factory_reset.reset_pb2 import (  # noqa
    ResetError,
    ResetSuccess,
    StartRequest,
    StartResponse,
)
from gnoi.proto._legacy.factory_reset.reset_pb2_grpc import (  # noqa
    FactoryReset,
    FactoryResetServicer,
    FactoryResetStub,
)
from gnoi.proto._legacy.file.file_pb2 import (  # noqa
    GetRequest,
    GetResponse,
    PutRequest,
    PutResponse,
    RemoveRequest,
    RemoveResponse,
    StatInfo,
    StatRequest,
    StatResponse,
    TransferToRemoteRequest,
    TransferToRemoteResponse,
)
from gnoi.proto._legacy.file.file_pb2_grpc import File, FileServicer, FileStub  # noqa
from gnoi.proto._legacy.layer2.layer2_pb2 import (  # noqa
    ClearLLDPInterfaceRequest,
    ClearLLDPInterfaceResponse,
    ClearNeighborDiscoveryRequest,
    ClearNeighborDiscoveryResponse,
    ClearSpanningTreeRequest,
    ClearSpanningTreeResponse,
    PerformBERTRequest,
    PerformBERTResponse,
    SendWakeOnLANRequest,
    SendWakeOnLANResponse,
)
from gnoi.proto._legacy.layer2.layer2_pb2_grpc import (  # noqa
    Layer2,
    Layer2Servicer,
    Layer2Stub,
)
from gnoi.proto._legacy.mpls.mpls_pb2 import (  # noqa
    ClearLSPCountersRequest,
    ClearLSPCountersResponse,
    ClearLSPRequest,
    ClearLSPResponse,
    MPLSPingPWEDestination,
    MPLSPingRSVPTEDestination,
    MPLSPingRequest,
    MPLSPingResponse,
)
from gnoi.proto._legacy.mpls.mpls_pb2_grpc import MPLS, MPLSServicer, MPLSStub  # noqa
from gnoi.proto._legacy.os.os_pb2 import (  # noqa
    ActivateError,
    ActivateOK,
    ActivateRequest,
    ActivateResponse,
    InstallError,
    InstallRequest,
    InstallResponse,
    StandbyResponse,
    StandbyState,
    SyncProgress,
    TransferEnd,
    TransferProgress,
    TransferReady,
    TransferRequest,
    Validated,
    VerifyRequest,
    VerifyResponse,
    VerifyStandby,
)
from gnoi.proto._legacy.os.os_pb2_grpc import OS, OSServicer, OSStub  # noqa
from gnoi.proto._legacy.otdr.otdr_pb2 import (  # noqa
    Event,
    FiberTypeProfile,
    InitiateError,
    InitiateProgress,
    InitiateRequest,
    InitiateResponse,
    InitiateResults,
    OTDRConfiguration,
    OTDRTrace,
)
from gnoi.proto._legacy.otdr.otdr_pb2_grpc import OTDR, OTDRServicer, OTDRStub  # noqa
from gnoi.proto._legacy.system.system_pb2 import (  # noqa
    COLD,
    CancelRebootRequest,
    CancelRebootResponse,
    HALT,
    NSF,
    POWERDOWN,
    POWERUP,
    Package,
    PingRequest,
    PingResponse,
    RebootMethod,
    RebootRequest,
    RebootResponse,
    RebootStatusRequest,
    RebootStatusResponse,
    SetPackageRequest,
    SetPackageResponse,
    SwitchControlProcessorRequest,
    SwitchControlProcessorResponse,
    TimeRequest,
    TimeResponse,
    TracerouteRequest,
    TracerouteResponse,
    UNKNOWN,
    WARM,
)
from gnoi.proto._legacy.system.system_pb2_grpc import (  # noqa
    System,
    SystemServicer,
    SystemStub,
)
from gnoi.proto._legacy.types.types_pb2 import (  # noqa
    Credentials,
    HashType,
    Path,
    PathElem,
    UNSPECIFIED,
)
from gnoi.proto._legacy.wavelength_router.wavelength_router_pb2 import (  # noqa
    AdjustPSDError,
    AdjustPSDProgress,
    AdjustPSDRequest,
    AdjustPSDResponse,
    AdjustSpectrumError,
    AdjustSpectrumProgress,
    AdjustSpectrumRequest,
    AdjustSpectrumResponse,
    CancelAdjustPSDResponse,
    CancelAdjustSpectrumResponse,
)
from gnoi.proto._legacy.wavelength_router.wavelength_router_pb2_grpc import (  # noqa
    WavelengthRouter,
    WavelengthRouterServicer,
    WavelengthRouterStub,
)
