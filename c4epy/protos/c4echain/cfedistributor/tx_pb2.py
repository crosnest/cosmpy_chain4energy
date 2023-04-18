# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: c4echain/cfedistributor/tx.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from c4echain.cfedistributor import sub_distributor_pb2 as c4echain_dot_cfedistributor_dot_sub__distributor__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n c4echain/cfedistributor/tx.proto\x12$chain4energy.c4echain.cfedistributor\x1a\x17\x63osmos/msg/v1/msg.proto\x1a\x14gogoproto/gogo.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a-c4echain/cfedistributor/sub_distributor.proto\"z\n\x0fMsgUpdateParams\x12\x11\n\tauthority\x18\x01 \x01(\t\x12T\n\x10sub_distributors\x18\x02 \x03(\x0b\x32\x34.chain4energy.c4echain.cfedistributor.SubDistributorB\x04\xc8\xde\x1f\x00\"\x19\n\x17MsgUpdateParamsResponse\"\x80\x01\n\x1cMsgUpdateSubDistributorParam\x12\x11\n\tauthority\x18\x01 \x01(\t\x12M\n\x0fsub_distributor\x18\x02 \x01(\x0b\x32\x34.chain4energy.c4echain.cfedistributor.SubDistributor\"&\n$MsgUpdateSubDistributorParamResponse\"\xc8\x01\n,MsgUpdateSubDistributorDestinationShareParam\x12\x11\n\tauthority\x18\x01 \x01(\t\x12\x1c\n\x14sub_distributor_name\x18\x02 \x01(\t\x12\x18\n\x10\x64\x65stination_name\x18\x03 \x01(\t\x12M\n\x05share\x18\x04 \x01(\tB>\xf2\xde\x1f\x0cyaml:\"share\"\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\"6\n4MsgUpdateSubDistributorDestinationShareParamResponse\"\xb1\x01\n%MsgUpdateSubDistributorBurnShareParam\x12\x11\n\tauthority\x18\x01 \x01(\t\x12\x1c\n\x14sub_distributor_name\x18\x02 \x01(\t\x12W\n\nburn_share\x18\x03 \x01(\tBC\xf2\xde\x1f\x11yaml:\"burn_share\"\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\"/\n-MsgUpdateSubDistributorBurnShareParamResponse2\xe1\x05\n\x03Msg\x12\x84\x01\n\x0cUpdateParams\x12\x35.chain4energy.c4echain.cfedistributor.MsgUpdateParams\x1a=.chain4energy.c4echain.cfedistributor.MsgUpdateParamsResponse\x12\xab\x01\n\x19UpdateSubDistributorParam\x12\x42.chain4energy.c4echain.cfedistributor.MsgUpdateSubDistributorParam\x1aJ.chain4energy.c4echain.cfedistributor.MsgUpdateSubDistributorParamResponse\x12\xdb\x01\n)UpdateSubDistributorDestinationShareParam\x12R.chain4energy.c4echain.cfedistributor.MsgUpdateSubDistributorDestinationShareParam\x1aZ.chain4energy.c4echain.cfedistributor.MsgUpdateSubDistributorDestinationShareParamResponse\x12\xc6\x01\n\"UpdateSubDistributorBurnShareParam\x12K.chain4energy.c4echain.cfedistributor.MsgUpdateSubDistributorBurnShareParam\x1aS.chain4energy.c4echain.cfedistributor.MsgUpdateSubDistributorBurnShareParamResponseB:Z8github.com/chain4energy/c4e-chain/x/cfedistributor/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'c4echain.cfedistributor.tx_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z8github.com/chain4energy/c4e-chain/x/cfedistributor/types'
  _MSGUPDATEPARAMS.fields_by_name['sub_distributors']._options = None
  _MSGUPDATEPARAMS.fields_by_name['sub_distributors']._serialized_options = b'\310\336\037\000'
  _MSGUPDATESUBDISTRIBUTORDESTINATIONSHAREPARAM.fields_by_name['share']._options = None
  _MSGUPDATESUBDISTRIBUTORDESTINATIONSHAREPARAM.fields_by_name['share']._serialized_options = b'\362\336\037\014yaml:\"share\"\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _MSGUPDATESUBDISTRIBUTORBURNSHAREPARAM.fields_by_name['burn_share']._options = None
  _MSGUPDATESUBDISTRIBUTORBURNSHAREPARAM.fields_by_name['burn_share']._serialized_options = b'\362\336\037\021yaml:\"burn_share\"\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _MSGUPDATEPARAMS._serialized_start=195
  _MSGUPDATEPARAMS._serialized_end=317
  _MSGUPDATEPARAMSRESPONSE._serialized_start=319
  _MSGUPDATEPARAMSRESPONSE._serialized_end=344
  _MSGUPDATESUBDISTRIBUTORPARAM._serialized_start=347
  _MSGUPDATESUBDISTRIBUTORPARAM._serialized_end=475
  _MSGUPDATESUBDISTRIBUTORPARAMRESPONSE._serialized_start=477
  _MSGUPDATESUBDISTRIBUTORPARAMRESPONSE._serialized_end=515
  _MSGUPDATESUBDISTRIBUTORDESTINATIONSHAREPARAM._serialized_start=518
  _MSGUPDATESUBDISTRIBUTORDESTINATIONSHAREPARAM._serialized_end=718
  _MSGUPDATESUBDISTRIBUTORDESTINATIONSHAREPARAMRESPONSE._serialized_start=720
  _MSGUPDATESUBDISTRIBUTORDESTINATIONSHAREPARAMRESPONSE._serialized_end=774
  _MSGUPDATESUBDISTRIBUTORBURNSHAREPARAM._serialized_start=777
  _MSGUPDATESUBDISTRIBUTORBURNSHAREPARAM._serialized_end=954
  _MSGUPDATESUBDISTRIBUTORBURNSHAREPARAMRESPONSE._serialized_start=956
  _MSGUPDATESUBDISTRIBUTORBURNSHAREPARAMRESPONSE._serialized_end=1003
  _MSG._serialized_start=1006
  _MSG._serialized_end=1743
# @@protoc_insertion_point(module_scope)
