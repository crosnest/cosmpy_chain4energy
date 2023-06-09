# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: c4echain/cfedistributor/query.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from c4echain.cfedistributor import params_pb2 as c4echain_dot_cfedistributor_dot_params__pb2
from c4echain.cfedistributor import sub_distributor_pb2 as c4echain_dot_cfedistributor_dot_sub__distributor__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#c4echain/cfedistributor/query.proto\x12$chain4energy.c4echain.cfedistributor\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a$c4echain/cfedistributor/params.proto\x1a-c4echain/cfedistributor/sub_distributor.proto\"\x14\n\x12QueryParamsRequest\"Y\n\x13QueryParamsResponse\x12\x42\n\x06params\x18\x01 \x01(\x0b\x32,.chain4energy.c4echain.cfedistributor.ParamsB\x04\xc8\xde\x1f\x00\"\x14\n\x12QueryStatesRequest\"\x9f\x01\n\x13QueryStatesResponse\x12\x41\n\x06states\x18\x01 \x03(\x0b\x32+.chain4energy.c4echain.cfedistributor.StateB\x04\xc8\xde\x1f\x00\x12\x45\n\x1c\x63oins_on_distributor_account\x18\x02 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\x32\xd9\x02\n\x05Query\x12\xa6\x01\n\x06Params\x12\x38.chain4energy.c4echain.cfedistributor.QueryParamsRequest\x1a\x39.chain4energy.c4echain.cfedistributor.QueryParamsResponse\"\'\x82\xd3\xe4\x93\x02!\x12\x1f/c4e/distributor/v1beta1/params\x12\xa6\x01\n\x06States\x12\x38.chain4energy.c4echain.cfedistributor.QueryStatesRequest\x1a\x39.chain4energy.c4echain.cfedistributor.QueryStatesResponse\"\'\x82\xd3\xe4\x93\x02!\x12\x1f/c4e/distributor/v1beta1/statesB:Z8github.com/chain4energy/c4e-chain/x/cfedistributor/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'c4echain.cfedistributor.query_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z8github.com/chain4energy/c4e-chain/x/cfedistributor/types'
  _QUERYPARAMSRESPONSE.fields_by_name['params']._options = None
  _QUERYPARAMSRESPONSE.fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _QUERYSTATESRESPONSE.fields_by_name['states']._options = None
  _QUERYSTATESRESPONSE.fields_by_name['states']._serialized_options = b'\310\336\037\000'
  _QUERYSTATESRESPONSE.fields_by_name['coins_on_distributor_account']._options = None
  _QUERYSTATESRESPONSE.fields_by_name['coins_on_distributor_account']._serialized_options = b'\310\336\037\000'
  _QUERY.methods_by_name['Params']._options = None
  _QUERY.methods_by_name['Params']._serialized_options = b'\202\323\344\223\002!\022\037/c4e/distributor/v1beta1/params'
  _QUERY.methods_by_name['States']._options = None
  _QUERY.methods_by_name['States']._serialized_options = b'\202\323\344\223\002!\022\037/c4e/distributor/v1beta1/states'
  _QUERYPARAMSREQUEST._serialized_start=290
  _QUERYPARAMSREQUEST._serialized_end=310
  _QUERYPARAMSRESPONSE._serialized_start=312
  _QUERYPARAMSRESPONSE._serialized_end=401
  _QUERYSTATESREQUEST._serialized_start=403
  _QUERYSTATESREQUEST._serialized_end=423
  _QUERYSTATESRESPONSE._serialized_start=426
  _QUERYSTATESRESPONSE._serialized_end=585
  _QUERY._serialized_start=588
  _QUERY._serialized_end=933
# @@protoc_insertion_point(module_scope)
