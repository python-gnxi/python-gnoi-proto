PROJECT_ROOT                    ?= gnoi/proto
PROTO_PACKAGE                   ?= github.com/openconfig/gnoi
PROTOS                          ?= types/types common/common layer2/layer2 mpls/mpls \
                                   os/os bgp/bgp otdr/otdr file/file factory_reset/reset \
                                   wavelength_router/wavelength_router cert/cert diag/diag \
                                   system/system

include Makefile.in