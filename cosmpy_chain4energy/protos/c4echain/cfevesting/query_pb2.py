# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: c4echain/cfevesting/query.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from c4echain.cfevesting import genesis_pb2 as c4echain_dot_cfevesting_dot_genesis__pb2
from c4echain.cfevesting import params_pb2 as c4echain_dot_cfevesting_dot_params__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1f\x63\x34\x65\x63hain/cfevesting/query.proto\x12 chain4energy.c4echain.cfevesting\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a!c4echain/cfevesting/genesis.proto\x1a c4echain/cfevesting/params.proto\"\x14\n\x12QueryParamsRequest\"U\n\x13QueryParamsResponse\x12>\n\x06params\x18\x01 \x01(\x0b\x32(.chain4energy.c4echain.cfevesting.ParamsB\x04\xc8\xde\x1f\x00\"\x19\n\x17QueryVestingTypeRequest\"\x85\x01\n\x18QueryVestingTypeResponse\x12i\n\rvesting_types\x18\x02 \x03(\x0b\x32\x34.chain4energy.c4echain.cfevesting.GenesisVestingTypeB\x1c\xc8\xde\x1f\x00\xf2\xde\x1f\x14yaml:\"vesting_types\"\")\n\x18QueryVestingPoolsRequest\x12\r\n\x05owner\x18\x01 \x01(\t\"e\n\x19QueryVestingPoolsResponse\x12H\n\rvesting_pools\x18\x02 \x03(\x0b\x32\x31.chain4energy.c4echain.cfevesting.VestingPoolInfo\"\xa1\x02\n\x0fVestingPoolInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0cvesting_type\x18\x02 \x01(\t\x12\x38\n\nlock_start\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01\x12\x36\n\x08lock_end\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01\x12\x14\n\x0cwithdrawable\x18\x05 \x01(\t\x12\x33\n\x10initially_locked\x18\x06 \x01(\x0b\x32\x19.cosmos.base.v1beta1.Coin\x12\x18\n\x10\x63urrently_locked\x18\x07 \x01(\t\x12\x13\n\x0bsent_amount\x18\x08 \x01(\t\"\x1d\n\x1bQueryVestingsSummaryRequest\"\xe1\x02\n\x1cQueryVestingsSummaryResponse\x12J\n\x12vesting_all_amount\x18\x01 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00\x12O\n\x17vesting_in_pools_amount\x18\x02 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00\x12R\n\x1avesting_in_accounts_amount\x18\x03 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00\x12P\n\x18\x64\x65legated_vesting_amount\x18\x04 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00\"$\n\"QueryGenesisVestingsSummaryRequest\"\xe8\x02\n#QueryGenesisVestingsSummaryResponse\x12J\n\x12vesting_all_amount\x18\x01 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00\x12O\n\x17vesting_in_pools_amount\x18\x02 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00\x12R\n\x1avesting_in_accounts_amount\x18\x03 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00\x12P\n\x18\x64\x65legated_vesting_amount\x18\x04 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00\x32\xa3\x07\n\x05Query\x12\x9a\x01\n\x06Params\x12\x34.chain4energy.c4echain.cfevesting.QueryParamsRequest\x1a\x35.chain4energy.c4echain.cfevesting.QueryParamsResponse\"#\x82\xd3\xe4\x93\x02\x1d\x12\x1b/c4e/vesting/v1beta1/params\x12\xaf\x01\n\x0bVestingType\x12\x39.chain4energy.c4echain.cfevesting.QueryVestingTypeRequest\x1a:.chain4energy.c4echain.cfevesting.QueryVestingTypeResponse\")\x82\xd3\xe4\x93\x02#\x12!/c4e/vesting/v1beta1/vesting_type\x12\xbb\x01\n\x0cVestingPools\x12:.chain4energy.c4echain.cfevesting.QueryVestingPoolsRequest\x1a;.chain4energy.c4echain.cfevesting.QueryVestingPoolsResponse\"2\x82\xd3\xe4\x93\x02,\x12*/c4e/vesting/v1beta1/vesting_pools/{owner}\x12\xb6\x01\n\x0fVestingsSummary\x12=.chain4energy.c4echain.cfevesting.QueryVestingsSummaryRequest\x1a>.chain4energy.c4echain.cfevesting.QueryVestingsSummaryResponse\"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/c4e/vesting/v1beta1/summary\x12\xd3\x01\n\x16GenesisVestingsSummary\x12\x44.chain4energy.c4echain.cfevesting.QueryGenesisVestingsSummaryRequest\x1a\x45.chain4energy.c4echain.cfevesting.QueryGenesisVestingsSummaryResponse\",\x82\xd3\xe4\x93\x02&\x12$/c4e/vesting/v1beta1/genesis_summaryB6Z4github.com/chain4energy/c4e-chain/x/cfevesting/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'c4echain.cfevesting.query_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z4github.com/chain4energy/c4e-chain/x/cfevesting/types'
  _QUERYPARAMSRESPONSE.fields_by_name['params']._options = None
  _QUERYPARAMSRESPONSE.fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _QUERYVESTINGTYPERESPONSE.fields_by_name['vesting_types']._options = None
  _QUERYVESTINGTYPERESPONSE.fields_by_name['vesting_types']._serialized_options = b'\310\336\037\000\362\336\037\024yaml:\"vesting_types\"'
  _VESTINGPOOLINFO.fields_by_name['lock_start']._options = None
  _VESTINGPOOLINFO.fields_by_name['lock_start']._serialized_options = b'\310\336\037\000\220\337\037\001'
  _VESTINGPOOLINFO.fields_by_name['lock_end']._options = None
  _VESTINGPOOLINFO.fields_by_name['lock_end']._serialized_options = b'\310\336\037\000\220\337\037\001'
  _QUERYVESTINGSSUMMARYRESPONSE.fields_by_name['vesting_all_amount']._options = None
  _QUERYVESTINGSSUMMARYRESPONSE.fields_by_name['vesting_all_amount']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\310\336\037\000'
  _QUERYVESTINGSSUMMARYRESPONSE.fields_by_name['vesting_in_pools_amount']._options = None
  _QUERYVESTINGSSUMMARYRESPONSE.fields_by_name['vesting_in_pools_amount']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\310\336\037\000'
  _QUERYVESTINGSSUMMARYRESPONSE.fields_by_name['vesting_in_accounts_amount']._options = None
  _QUERYVESTINGSSUMMARYRESPONSE.fields_by_name['vesting_in_accounts_amount']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\310\336\037\000'
  _QUERYVESTINGSSUMMARYRESPONSE.fields_by_name['delegated_vesting_amount']._options = None
  _QUERYVESTINGSSUMMARYRESPONSE.fields_by_name['delegated_vesting_amount']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\310\336\037\000'
  _QUERYGENESISVESTINGSSUMMARYRESPONSE.fields_by_name['vesting_all_amount']._options = None
  _QUERYGENESISVESTINGSSUMMARYRESPONSE.fields_by_name['vesting_all_amount']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\310\336\037\000'
  _QUERYGENESISVESTINGSSUMMARYRESPONSE.fields_by_name['vesting_in_pools_amount']._options = None
  _QUERYGENESISVESTINGSSUMMARYRESPONSE.fields_by_name['vesting_in_pools_amount']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\310\336\037\000'
  _QUERYGENESISVESTINGSSUMMARYRESPONSE.fields_by_name['vesting_in_accounts_amount']._options = None
  _QUERYGENESISVESTINGSSUMMARYRESPONSE.fields_by_name['vesting_in_accounts_amount']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\310\336\037\000'
  _QUERYGENESISVESTINGSSUMMARYRESPONSE.fields_by_name['delegated_vesting_amount']._options = None
  _QUERYGENESISVESTINGSSUMMARYRESPONSE.fields_by_name['delegated_vesting_amount']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\310\336\037\000'
  _QUERY.methods_by_name['Params']._options = None
  _QUERY.methods_by_name['Params']._serialized_options = b'\202\323\344\223\002\035\022\033/c4e/vesting/v1beta1/params'
  _QUERY.methods_by_name['VestingType']._options = None
  _QUERY.methods_by_name['VestingType']._serialized_options = b'\202\323\344\223\002#\022!/c4e/vesting/v1beta1/vesting_type'
  _QUERY.methods_by_name['VestingPools']._options = None
  _QUERY.methods_by_name['VestingPools']._serialized_options = b'\202\323\344\223\002,\022*/c4e/vesting/v1beta1/vesting_pools/{owner}'
  _QUERY.methods_by_name['VestingsSummary']._options = None
  _QUERY.methods_by_name['VestingsSummary']._serialized_options = b'\202\323\344\223\002\036\022\034/c4e/vesting/v1beta1/summary'
  _QUERY.methods_by_name['GenesisVestingsSummary']._options = None
  _QUERY.methods_by_name['GenesisVestingsSummary']._serialized_options = b'\202\323\344\223\002&\022$/c4e/vesting/v1beta1/genesis_summary'
  _QUERYPARAMSREQUEST._serialized_start=255
  _QUERYPARAMSREQUEST._serialized_end=275
  _QUERYPARAMSRESPONSE._serialized_start=277
  _QUERYPARAMSRESPONSE._serialized_end=362
  _QUERYVESTINGTYPEREQUEST._serialized_start=364
  _QUERYVESTINGTYPEREQUEST._serialized_end=389
  _QUERYVESTINGTYPERESPONSE._serialized_start=392
  _QUERYVESTINGTYPERESPONSE._serialized_end=525
  _QUERYVESTINGPOOLSREQUEST._serialized_start=527
  _QUERYVESTINGPOOLSREQUEST._serialized_end=568
  _QUERYVESTINGPOOLSRESPONSE._serialized_start=570
  _QUERYVESTINGPOOLSRESPONSE._serialized_end=671
  _VESTINGPOOLINFO._serialized_start=674
  _VESTINGPOOLINFO._serialized_end=963
  _QUERYVESTINGSSUMMARYREQUEST._serialized_start=965
  _QUERYVESTINGSSUMMARYREQUEST._serialized_end=994
  _QUERYVESTINGSSUMMARYRESPONSE._serialized_start=997
  _QUERYVESTINGSSUMMARYRESPONSE._serialized_end=1350
  _QUERYGENESISVESTINGSSUMMARYREQUEST._serialized_start=1352
  _QUERYGENESISVESTINGSSUMMARYREQUEST._serialized_end=1388
  _QUERYGENESISVESTINGSSUMMARYRESPONSE._serialized_start=1391
  _QUERYGENESISVESTINGSSUMMARYRESPONSE._serialized_end=1751
  _QUERY._serialized_start=1754
  _QUERY._serialized_end=2685
# @@protoc_insertion_point(module_scope)
