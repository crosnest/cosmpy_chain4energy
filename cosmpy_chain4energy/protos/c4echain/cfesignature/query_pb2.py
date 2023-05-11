# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: c4echain/cfesignature/query.proto
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
from c4echain.cfesignature import params_pb2 as c4echain_dot_cfesignature_dot_params__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!c4echain/cfesignature/query.proto\x12\"chain4energy.c4echain.cfesignature\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\"c4echain/cfesignature/params.proto\"\x14\n\x12QueryParamsRequest\"W\n\x13QueryParamsResponse\x12@\n\x06params\x18\x01 \x01(\x0b\x32*.chain4energy.c4echain.cfesignature.ParamsB\x04\xc8\xde\x1f\x00\"0\n\x1dQueryCreateReferenceIdRequest\x12\x0f\n\x07\x63reator\x18\x01 \x01(\t\"5\n\x1eQueryCreateReferenceIdResponse\x12\x13\n\x0breferenceId\x18\x01 \x01(\t\"M\n\x1cQueryCreateStorageKeyRequest\x12\x18\n\x10targetAccAddress\x18\x01 \x01(\t\x12\x13\n\x0breferenceId\x18\x02 \x01(\t\"3\n\x1dQueryCreateStorageKeyResponse\x12\x12\n\nstorageKey\x18\x01 \x01(\t\"R\n&QueryCreateReferencePayloadLinkRequest\x12\x13\n\x0breferenceId\x18\x01 \x01(\t\x12\x13\n\x0bpayloadHash\x18\x02 \x01(\t\"W\n\'QueryCreateReferencePayloadLinkResponse\x12\x14\n\x0creferenceKey\x18\x01 \x01(\t\x12\x16\n\x0ereferenceValue\x18\x02 \x01(\t\"L\n\x1bQueryVerifySignatureRequest\x12\x13\n\x0breferenceId\x18\x01 \x01(\t\x12\x18\n\x10targetAccAddress\x18\x02 \x01(\t\"{\n\x1cQueryVerifySignatureResponse\x12\x11\n\tsignature\x18\x01 \x01(\t\x12\x11\n\talgorithm\x18\x02 \x01(\t\x12\x13\n\x0b\x63\x65rtificate\x18\x03 \x01(\t\x12\x11\n\ttimestamp\x18\x04 \x01(\t\x12\r\n\x05valid\x18\x05 \x01(\t\"6\n\x1aQueryGetAccountInfoRequest\x12\x18\n\x10\x61\x63\x63\x41\x64\x64ressString\x18\x01 \x01(\t\"A\n\x1bQueryGetAccountInfoResponse\x12\x12\n\naccAddress\x18\x01 \x01(\t\x12\x0e\n\x06pubKey\x18\x02 \x01(\t\"R\n&QueryVerifyReferencePayloadLinkRequest\x12\x13\n\x0breferenceId\x18\x01 \x01(\t\x12\x13\n\x0bpayloadHash\x18\x02 \x01(\t\":\n\'QueryVerifyReferencePayloadLinkResponse\x12\x0f\n\x07isValid\x18\x01 \x01(\x08\":\n#QueryGetReferencePayloadLinkRequest\x12\x13\n\x0breferenceId\x18\x01 \x01(\t\"I\n$QueryGetReferencePayloadLinkResponse\x12!\n\x19referencePayloadLinkValue\x18\x01 \x01(\t2\xd0\x0e\n\x05Query\x12\xa0\x01\n\x06Params\x12\x36.chain4energy.c4echain.cfesignature.QueryParamsRequest\x1a\x37.chain4energy.c4echain.cfesignature.QueryParamsResponse\"%\x82\xd3\xe4\x93\x02\x1f\x12\x1d/c4e/signature/v1beta1/params\x12\xd8\x01\n\x11\x43reateReferenceId\x12\x41.chain4energy.c4echain.cfesignature.QueryCreateReferenceIdRequest\x1a\x42.chain4energy.c4echain.cfesignature.QueryCreateReferenceIdResponse\"<\x82\xd3\xe4\x93\x02\x36\x12\x34/c4e/signature/v1beta1/create_reference_id/{creator}\x12\xeb\x01\n\x10\x43reateStorageKey\x12@.chain4energy.c4echain.cfesignature.QueryCreateStorageKeyRequest\x1a\x41.chain4energy.c4echain.cfesignature.QueryCreateStorageKeyResponse\"R\x82\xd3\xe4\x93\x02L\x12J/c4e/signature/v1beta1/create_storage_key/{targetAccAddress}/{referenceId}\x12\x8f\x02\n\x1a\x43reateReferencePayloadLink\x12J.chain4energy.c4echain.cfesignature.QueryCreateReferencePayloadLinkRequest\x1aK.chain4energy.c4echain.cfesignature.QueryCreateReferencePayloadLinkResponse\"X\x82\xd3\xe4\x93\x02R\x12P/c4e/signature/v1beta1/create_reference_payload_link/{referenceId}/{payloadHash}\x12\xe6\x01\n\x0fVerifySignature\x12?.chain4energy.c4echain.cfesignature.QueryVerifySignatureRequest\x1a@.chain4energy.c4echain.cfesignature.QueryVerifySignatureResponse\"P\x82\xd3\xe4\x93\x02J\x12H/c4e/signature/v1beta1/verify_signature/{referenceId}/{targetAccAddress}\x12\xd5\x01\n\x0eGetAccountInfo\x12>.chain4energy.c4echain.cfesignature.QueryGetAccountInfoRequest\x1a?.chain4energy.c4echain.cfesignature.QueryGetAccountInfoResponse\"B\x82\xd3\xe4\x93\x02<\x12:/c4e/signature/v1beta1/get_account_info/{accAddressString}\x12\x8f\x02\n\x1aVerifyReferencePayloadLink\x12J.chain4energy.c4echain.cfesignature.QueryVerifyReferencePayloadLinkRequest\x1aK.chain4energy.c4echain.cfesignature.QueryVerifyReferencePayloadLinkResponse\"X\x82\xd3\xe4\x93\x02R\x12P/c4e/signature/v1beta1/verify_reference_payload_link/{referenceId}/{payloadHash}\x12\xf5\x01\n\x17GetReferencePayloadLink\x12G.chain4energy.c4echain.cfesignature.QueryGetReferencePayloadLinkRequest\x1aH.chain4energy.c4echain.cfesignature.QueryGetReferencePayloadLinkResponse\"G\x82\xd3\xe4\x93\x02\x41\x12?/c4e/signature/v1beta1/get_reference_payload_link/{referenceId}B8Z6github.com/chain4energy/c4e-chain/x/cfesignature/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'c4echain.cfesignature.query_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z6github.com/chain4energy/c4e-chain/x/cfesignature/types'
  _QUERYPARAMSRESPONSE.fields_by_name['params']._options = None
  _QUERYPARAMSRESPONSE.fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _QUERY.methods_by_name['Params']._options = None
  _QUERY.methods_by_name['Params']._serialized_options = b'\202\323\344\223\002\037\022\035/c4e/signature/v1beta1/params'
  _QUERY.methods_by_name['CreateReferenceId']._options = None
  _QUERY.methods_by_name['CreateReferenceId']._serialized_options = b'\202\323\344\223\0026\0224/c4e/signature/v1beta1/create_reference_id/{creator}'
  _QUERY.methods_by_name['CreateStorageKey']._options = None
  _QUERY.methods_by_name['CreateStorageKey']._serialized_options = b'\202\323\344\223\002L\022J/c4e/signature/v1beta1/create_storage_key/{targetAccAddress}/{referenceId}'
  _QUERY.methods_by_name['CreateReferencePayloadLink']._options = None
  _QUERY.methods_by_name['CreateReferencePayloadLink']._serialized_options = b'\202\323\344\223\002R\022P/c4e/signature/v1beta1/create_reference_payload_link/{referenceId}/{payloadHash}'
  _QUERY.methods_by_name['VerifySignature']._options = None
  _QUERY.methods_by_name['VerifySignature']._serialized_options = b'\202\323\344\223\002J\022H/c4e/signature/v1beta1/verify_signature/{referenceId}/{targetAccAddress}'
  _QUERY.methods_by_name['GetAccountInfo']._options = None
  _QUERY.methods_by_name['GetAccountInfo']._serialized_options = b'\202\323\344\223\002<\022:/c4e/signature/v1beta1/get_account_info/{accAddressString}'
  _QUERY.methods_by_name['VerifyReferencePayloadLink']._options = None
  _QUERY.methods_by_name['VerifyReferencePayloadLink']._serialized_options = b'\202\323\344\223\002R\022P/c4e/signature/v1beta1/verify_reference_payload_link/{referenceId}/{payloadHash}'
  _QUERY.methods_by_name['GetReferencePayloadLink']._options = None
  _QUERY.methods_by_name['GetReferencePayloadLink']._serialized_options = b'\202\323\344\223\002A\022?/c4e/signature/v1beta1/get_reference_payload_link/{referenceId}'
  _QUERYPARAMSREQUEST._serialized_start=205
  _QUERYPARAMSREQUEST._serialized_end=225
  _QUERYPARAMSRESPONSE._serialized_start=227
  _QUERYPARAMSRESPONSE._serialized_end=314
  _QUERYCREATEREFERENCEIDREQUEST._serialized_start=316
  _QUERYCREATEREFERENCEIDREQUEST._serialized_end=364
  _QUERYCREATEREFERENCEIDRESPONSE._serialized_start=366
  _QUERYCREATEREFERENCEIDRESPONSE._serialized_end=419
  _QUERYCREATESTORAGEKEYREQUEST._serialized_start=421
  _QUERYCREATESTORAGEKEYREQUEST._serialized_end=498
  _QUERYCREATESTORAGEKEYRESPONSE._serialized_start=500
  _QUERYCREATESTORAGEKEYRESPONSE._serialized_end=551
  _QUERYCREATEREFERENCEPAYLOADLINKREQUEST._serialized_start=553
  _QUERYCREATEREFERENCEPAYLOADLINKREQUEST._serialized_end=635
  _QUERYCREATEREFERENCEPAYLOADLINKRESPONSE._serialized_start=637
  _QUERYCREATEREFERENCEPAYLOADLINKRESPONSE._serialized_end=724
  _QUERYVERIFYSIGNATUREREQUEST._serialized_start=726
  _QUERYVERIFYSIGNATUREREQUEST._serialized_end=802
  _QUERYVERIFYSIGNATURERESPONSE._serialized_start=804
  _QUERYVERIFYSIGNATURERESPONSE._serialized_end=927
  _QUERYGETACCOUNTINFOREQUEST._serialized_start=929
  _QUERYGETACCOUNTINFOREQUEST._serialized_end=983
  _QUERYGETACCOUNTINFORESPONSE._serialized_start=985
  _QUERYGETACCOUNTINFORESPONSE._serialized_end=1050
  _QUERYVERIFYREFERENCEPAYLOADLINKREQUEST._serialized_start=1052
  _QUERYVERIFYREFERENCEPAYLOADLINKREQUEST._serialized_end=1134
  _QUERYVERIFYREFERENCEPAYLOADLINKRESPONSE._serialized_start=1136
  _QUERYVERIFYREFERENCEPAYLOADLINKRESPONSE._serialized_end=1194
  _QUERYGETREFERENCEPAYLOADLINKREQUEST._serialized_start=1196
  _QUERYGETREFERENCEPAYLOADLINKREQUEST._serialized_end=1254
  _QUERYGETREFERENCEPAYLOADLINKRESPONSE._serialized_start=1256
  _QUERYGETREFERENCEPAYLOADLINKRESPONSE._serialized_end=1329
  _QUERY._serialized_start=1332
  _QUERY._serialized_end=3204
# @@protoc_insertion_point(module_scope)