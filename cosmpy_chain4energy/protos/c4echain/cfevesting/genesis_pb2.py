# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: c4echain/cfevesting/genesis.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from c4echain.cfevesting import params_pb2 as c4echain_dot_cfevesting_dot_params__pb2
from c4echain.cfevesting import account_vesting_pool_pb2 as c4echain_dot_cfevesting_dot_account__vesting__pool__pb2
from c4echain.cfevesting import vesting_account_pb2 as c4echain_dot_cfevesting_dot_vesting__account__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!c4echain/cfevesting/genesis.proto\x12 chain4energy.c4echain.cfevesting\x1a\x14gogoproto/gogo.proto\x1a c4echain/cfevesting/params.proto\x1a.c4echain/cfevesting/account_vesting_pool.proto\x1a)c4echain/cfevesting/vesting_account.proto\"\xb3\x03\n\x0cGenesisState\x12>\n\x06params\x18\x01 \x01(\x0b\x32(.chain4energy.c4echain.cfevesting.ParamsB\x04\xc8\xde\x1f\x00\x12i\n\rvesting_types\x18\x02 \x03(\x0b\x32\x34.chain4energy.c4echain.cfevesting.GenesisVestingTypeB\x1c\xc8\xde\x1f\x00\xf2\xde\x1f\x14yaml:\"vesting_types\"\x12v\n\x15\x61\x63\x63ount_vesting_pools\x18\x03 \x03(\x0b\x32\x35.chain4energy.c4echain.cfevesting.AccountVestingPoolsB \xf2\xde\x1f\x1cyaml:\"account_vesting_pools\"\x12[\n\x16vesting_account_traces\x18\x04 \x03(\x0b\x32\x35.chain4energy.c4echain.cfevesting.VestingAccountTraceB\x04\xc8\xde\x1f\x00\x12#\n\x1bvesting_account_trace_count\x18\x05 \x01(\x04\"\xc8\x01\n\x12GenesisVestingType\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x15\n\rlockup_period\x18\x02 \x01(\x03\x12\x1a\n\x12lockup_period_unit\x18\x03 \x01(\t\x12\x16\n\x0evesting_period\x18\x04 \x01(\x03\x12\x1b\n\x13vesting_period_unit\x18\x05 \x01(\t\x12<\n\x04\x66ree\x18\x06 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x42\x36Z4github.com/chain4energy/c4e-chain/x/cfevesting/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'c4echain.cfevesting.genesis_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z4github.com/chain4energy/c4e-chain/x/cfevesting/types'
  _GENESISSTATE.fields_by_name['params']._options = None
  _GENESISSTATE.fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _GENESISSTATE.fields_by_name['vesting_types']._options = None
  _GENESISSTATE.fields_by_name['vesting_types']._serialized_options = b'\310\336\037\000\362\336\037\024yaml:\"vesting_types\"'
  _GENESISSTATE.fields_by_name['account_vesting_pools']._options = None
  _GENESISSTATE.fields_by_name['account_vesting_pools']._serialized_options = b'\362\336\037\034yaml:\"account_vesting_pools\"'
  _GENESISSTATE.fields_by_name['vesting_account_traces']._options = None
  _GENESISSTATE.fields_by_name['vesting_account_traces']._serialized_options = b'\310\336\037\000'
  _GENESISVESTINGTYPE.fields_by_name['free']._options = None
  _GENESISVESTINGTYPE.fields_by_name['free']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _GENESISSTATE._serialized_start=219
  _GENESISSTATE._serialized_end=654
  _GENESISVESTINGTYPE._serialized_start=657
  _GENESISVESTINGTYPE._serialized_end=857
# @@protoc_insertion_point(module_scope)
