# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: c4echain/cfevesting/event.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1f\x63\x34\x65\x63hain/cfevesting/event.proto\x12 chain4energy.c4echain.cfevesting\"$\n\x11NewVestingAccount\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\"d\n\x0eNewVestingPool\x12\r\n\x05owner\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06\x61mount\x18\x03 \x01(\t\x12\x10\n\x08\x64uration\x18\x04 \x01(\t\x12\x13\n\x0bvestingType\x18\x05 \x01(\t\"\x86\x01\n NewVestingAccountFromVestingPool\x12\r\n\x05owner\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\x12\x19\n\x11vesting_pool_name\x18\x03 \x01(\t\x12\x0e\n\x06\x61mount\x18\x04 \x01(\t\x12\x17\n\x0frestart_vesting\x18\x05 \x01(\t\"M\n\x11WithdrawAvailable\x12\r\n\x05owner\x18\x01 \x01(\t\x12\x19\n\x11vesting_pool_name\x18\x02 \x01(\t\x12\x0e\n\x06\x61mount\x18\x03 \x01(\t\"3\n\x0cVestingSplit\x12\x0e\n\x06source\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65stination\x18\x02 \x01(\tB6Z4github.com/chain4energy/c4e-chain/x/cfevesting/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'c4echain.cfevesting.event_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z4github.com/chain4energy/c4e-chain/x/cfevesting/types'
  _NEWVESTINGACCOUNT._serialized_start=69
  _NEWVESTINGACCOUNT._serialized_end=105
  _NEWVESTINGPOOL._serialized_start=107
  _NEWVESTINGPOOL._serialized_end=207
  _NEWVESTINGACCOUNTFROMVESTINGPOOL._serialized_start=210
  _NEWVESTINGACCOUNTFROMVESTINGPOOL._serialized_end=344
  _WITHDRAWAVAILABLE._serialized_start=346
  _WITHDRAWAVAILABLE._serialized_end=423
  _VESTINGSPLIT._serialized_start=425
  _VESTINGSPLIT._serialized_end=476
# @@protoc_insertion_point(module_scope)
