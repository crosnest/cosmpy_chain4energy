# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/gov/v1beta1/query.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from cosmos.gov.v1beta1 import gov_pb2 as cosmos_dot_gov_dot_v1beta1_dot_gov__pb2
from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1e\x63osmos/gov/v1beta1/query.proto\x12\x12\x63osmos.gov.v1beta1\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1c\x63osmos/gov/v1beta1/gov.proto\x1a\x19\x63osmos_proto/cosmos.proto\"+\n\x14QueryProposalRequest\x12\x13\n\x0bproposal_id\x18\x01 \x01(\x04\"M\n\x15QueryProposalResponse\x12\x34\n\x08proposal\x18\x01 \x01(\x0b\x32\x1c.cosmos.gov.v1beta1.ProposalB\x04\xc8\xde\x1f\x00\"\xf0\x01\n\x15QueryProposalsRequest\x12;\n\x0fproposal_status\x18\x01 \x01(\x0e\x32\".cosmos.gov.v1beta1.ProposalStatus\x12\'\n\x05voter\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12+\n\tdepositor\x18\x03 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12:\n\npagination\x18\x04 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\x8c\x01\n\x16QueryProposalsResponse\x12\x35\n\tproposals\x18\x01 \x03(\x0b\x32\x1c.cosmos.gov.v1beta1.ProposalB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"Z\n\x10QueryVoteRequest\x12\x13\n\x0bproposal_id\x18\x01 \x01(\x04\x12\'\n\x05voter\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"A\n\x11QueryVoteResponse\x12,\n\x04vote\x18\x01 \x01(\x0b\x32\x18.cosmos.gov.v1beta1.VoteB\x04\xc8\xde\x1f\x00\"d\n\x11QueryVotesRequest\x12\x13\n\x0bproposal_id\x18\x01 \x01(\x04\x12:\n\npagination\x18\x02 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"\x80\x01\n\x12QueryVotesResponse\x12-\n\x05votes\x18\x01 \x03(\x0b\x32\x18.cosmos.gov.v1beta1.VoteB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\")\n\x12QueryParamsRequest\x12\x13\n\x0bparams_type\x18\x01 \x01(\t\"\xd2\x01\n\x13QueryParamsResponse\x12=\n\rvoting_params\x18\x01 \x01(\x0b\x32 .cosmos.gov.v1beta1.VotingParamsB\x04\xc8\xde\x1f\x00\x12?\n\x0e\x64\x65posit_params\x18\x02 \x01(\x0b\x32!.cosmos.gov.v1beta1.DepositParamsB\x04\xc8\xde\x1f\x00\x12;\n\x0ctally_params\x18\x03 \x01(\x0b\x32\x1f.cosmos.gov.v1beta1.TallyParamsB\x04\xc8\xde\x1f\x00\"a\n\x13QueryDepositRequest\x12\x13\n\x0bproposal_id\x18\x01 \x01(\x04\x12+\n\tdepositor\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\"J\n\x14QueryDepositResponse\x12\x32\n\x07\x64\x65posit\x18\x01 \x01(\x0b\x32\x1b.cosmos.gov.v1beta1.DepositB\x04\xc8\xde\x1f\x00\"g\n\x14QueryDepositsRequest\x12\x13\n\x0bproposal_id\x18\x01 \x01(\x04\x12:\n\npagination\x18\x02 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"\x89\x01\n\x15QueryDepositsResponse\x12\x33\n\x08\x64\x65posits\x18\x01 \x03(\x0b\x32\x1b.cosmos.gov.v1beta1.DepositB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\".\n\x17QueryTallyResultRequest\x12\x13\n\x0bproposal_id\x18\x01 \x01(\x04\"P\n\x18QueryTallyResultResponse\x12\x34\n\x05tally\x18\x01 \x01(\x0b\x32\x1f.cosmos.gov.v1beta1.TallyResultB\x04\xc8\xde\x1f\x00\x32\xd4\t\n\x05Query\x12\x94\x01\n\x08Proposal\x12(.cosmos.gov.v1beta1.QueryProposalRequest\x1a).cosmos.gov.v1beta1.QueryProposalResponse\"3\x82\xd3\xe4\x93\x02-\x12+/cosmos/gov/v1beta1/proposals/{proposal_id}\x12\x89\x01\n\tProposals\x12).cosmos.gov.v1beta1.QueryProposalsRequest\x1a*.cosmos.gov.v1beta1.QueryProposalsResponse\"%\x82\xd3\xe4\x93\x02\x1f\x12\x1d/cosmos/gov/v1beta1/proposals\x12\x96\x01\n\x04Vote\x12$.cosmos.gov.v1beta1.QueryVoteRequest\x1a%.cosmos.gov.v1beta1.QueryVoteResponse\"A\x82\xd3\xe4\x93\x02;\x12\x39/cosmos/gov/v1beta1/proposals/{proposal_id}/votes/{voter}\x12\x91\x01\n\x05Votes\x12%.cosmos.gov.v1beta1.QueryVotesRequest\x1a&.cosmos.gov.v1beta1.QueryVotesResponse\"9\x82\xd3\xe4\x93\x02\x33\x12\x31/cosmos/gov/v1beta1/proposals/{proposal_id}/votes\x12\x8b\x01\n\x06Params\x12&.cosmos.gov.v1beta1.QueryParamsRequest\x1a\'.cosmos.gov.v1beta1.QueryParamsResponse\"0\x82\xd3\xe4\x93\x02*\x12(/cosmos/gov/v1beta1/params/{params_type}\x12\xa6\x01\n\x07\x44\x65posit\x12\'.cosmos.gov.v1beta1.QueryDepositRequest\x1a(.cosmos.gov.v1beta1.QueryDepositResponse\"H\x82\xd3\xe4\x93\x02\x42\x12@/cosmos/gov/v1beta1/proposals/{proposal_id}/deposits/{depositor}\x12\x9d\x01\n\x08\x44\x65posits\x12(.cosmos.gov.v1beta1.QueryDepositsRequest\x1a).cosmos.gov.v1beta1.QueryDepositsResponse\"<\x82\xd3\xe4\x93\x02\x36\x12\x34/cosmos/gov/v1beta1/proposals/{proposal_id}/deposits\x12\xa3\x01\n\x0bTallyResult\x12+.cosmos.gov.v1beta1.QueryTallyResultRequest\x1a,.cosmos.gov.v1beta1.QueryTallyResultResponse\"9\x82\xd3\xe4\x93\x02\x33\x12\x31/cosmos/gov/v1beta1/proposals/{proposal_id}/tallyB2Z0github.com/cosmos/cosmos-sdk/x/gov/types/v1beta1b\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.gov.v1beta1.query_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z0github.com/cosmos/cosmos-sdk/x/gov/types/v1beta1'
  _QUERYPROPOSALRESPONSE.fields_by_name['proposal']._options = None
  _QUERYPROPOSALRESPONSE.fields_by_name['proposal']._serialized_options = b'\310\336\037\000'
  _QUERYPROPOSALSREQUEST.fields_by_name['voter']._options = None
  _QUERYPROPOSALSREQUEST.fields_by_name['voter']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _QUERYPROPOSALSREQUEST.fields_by_name['depositor']._options = None
  _QUERYPROPOSALSREQUEST.fields_by_name['depositor']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _QUERYPROPOSALSREQUEST._options = None
  _QUERYPROPOSALSREQUEST._serialized_options = b'\350\240\037\000\210\240\037\000'
  _QUERYPROPOSALSRESPONSE.fields_by_name['proposals']._options = None
  _QUERYPROPOSALSRESPONSE.fields_by_name['proposals']._serialized_options = b'\310\336\037\000'
  _QUERYVOTEREQUEST.fields_by_name['voter']._options = None
  _QUERYVOTEREQUEST.fields_by_name['voter']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _QUERYVOTEREQUEST._options = None
  _QUERYVOTEREQUEST._serialized_options = b'\350\240\037\000\210\240\037\000'
  _QUERYVOTERESPONSE.fields_by_name['vote']._options = None
  _QUERYVOTERESPONSE.fields_by_name['vote']._serialized_options = b'\310\336\037\000'
  _QUERYVOTESRESPONSE.fields_by_name['votes']._options = None
  _QUERYVOTESRESPONSE.fields_by_name['votes']._serialized_options = b'\310\336\037\000'
  _QUERYPARAMSRESPONSE.fields_by_name['voting_params']._options = None
  _QUERYPARAMSRESPONSE.fields_by_name['voting_params']._serialized_options = b'\310\336\037\000'
  _QUERYPARAMSRESPONSE.fields_by_name['deposit_params']._options = None
  _QUERYPARAMSRESPONSE.fields_by_name['deposit_params']._serialized_options = b'\310\336\037\000'
  _QUERYPARAMSRESPONSE.fields_by_name['tally_params']._options = None
  _QUERYPARAMSRESPONSE.fields_by_name['tally_params']._serialized_options = b'\310\336\037\000'
  _QUERYDEPOSITREQUEST.fields_by_name['depositor']._options = None
  _QUERYDEPOSITREQUEST.fields_by_name['depositor']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _QUERYDEPOSITREQUEST._options = None
  _QUERYDEPOSITREQUEST._serialized_options = b'\210\240\037\000\350\240\037\000'
  _QUERYDEPOSITRESPONSE.fields_by_name['deposit']._options = None
  _QUERYDEPOSITRESPONSE.fields_by_name['deposit']._serialized_options = b'\310\336\037\000'
  _QUERYDEPOSITSRESPONSE.fields_by_name['deposits']._options = None
  _QUERYDEPOSITSRESPONSE.fields_by_name['deposits']._serialized_options = b'\310\336\037\000'
  _QUERYTALLYRESULTRESPONSE.fields_by_name['tally']._options = None
  _QUERYTALLYRESULTRESPONSE.fields_by_name['tally']._serialized_options = b'\310\336\037\000'
  _QUERY.methods_by_name['Proposal']._options = None
  _QUERY.methods_by_name['Proposal']._serialized_options = b'\202\323\344\223\002-\022+/cosmos/gov/v1beta1/proposals/{proposal_id}'
  _QUERY.methods_by_name['Proposals']._options = None
  _QUERY.methods_by_name['Proposals']._serialized_options = b'\202\323\344\223\002\037\022\035/cosmos/gov/v1beta1/proposals'
  _QUERY.methods_by_name['Vote']._options = None
  _QUERY.methods_by_name['Vote']._serialized_options = b'\202\323\344\223\002;\0229/cosmos/gov/v1beta1/proposals/{proposal_id}/votes/{voter}'
  _QUERY.methods_by_name['Votes']._options = None
  _QUERY.methods_by_name['Votes']._serialized_options = b'\202\323\344\223\0023\0221/cosmos/gov/v1beta1/proposals/{proposal_id}/votes'
  _QUERY.methods_by_name['Params']._options = None
  _QUERY.methods_by_name['Params']._serialized_options = b'\202\323\344\223\002*\022(/cosmos/gov/v1beta1/params/{params_type}'
  _QUERY.methods_by_name['Deposit']._options = None
  _QUERY.methods_by_name['Deposit']._serialized_options = b'\202\323\344\223\002B\022@/cosmos/gov/v1beta1/proposals/{proposal_id}/deposits/{depositor}'
  _QUERY.methods_by_name['Deposits']._options = None
  _QUERY.methods_by_name['Deposits']._serialized_options = b'\202\323\344\223\0026\0224/cosmos/gov/v1beta1/proposals/{proposal_id}/deposits'
  _QUERY.methods_by_name['TallyResult']._options = None
  _QUERY.methods_by_name['TallyResult']._serialized_options = b'\202\323\344\223\0023\0221/cosmos/gov/v1beta1/proposals/{proposal_id}/tally'
  _QUERYPROPOSALREQUEST._serialized_start=207
  _QUERYPROPOSALREQUEST._serialized_end=250
  _QUERYPROPOSALRESPONSE._serialized_start=252
  _QUERYPROPOSALRESPONSE._serialized_end=329
  _QUERYPROPOSALSREQUEST._serialized_start=332
  _QUERYPROPOSALSREQUEST._serialized_end=572
  _QUERYPROPOSALSRESPONSE._serialized_start=575
  _QUERYPROPOSALSRESPONSE._serialized_end=715
  _QUERYVOTEREQUEST._serialized_start=717
  _QUERYVOTEREQUEST._serialized_end=807
  _QUERYVOTERESPONSE._serialized_start=809
  _QUERYVOTERESPONSE._serialized_end=874
  _QUERYVOTESREQUEST._serialized_start=876
  _QUERYVOTESREQUEST._serialized_end=976
  _QUERYVOTESRESPONSE._serialized_start=979
  _QUERYVOTESRESPONSE._serialized_end=1107
  _QUERYPARAMSREQUEST._serialized_start=1109
  _QUERYPARAMSREQUEST._serialized_end=1150
  _QUERYPARAMSRESPONSE._serialized_start=1153
  _QUERYPARAMSRESPONSE._serialized_end=1363
  _QUERYDEPOSITREQUEST._serialized_start=1365
  _QUERYDEPOSITREQUEST._serialized_end=1462
  _QUERYDEPOSITRESPONSE._serialized_start=1464
  _QUERYDEPOSITRESPONSE._serialized_end=1538
  _QUERYDEPOSITSREQUEST._serialized_start=1540
  _QUERYDEPOSITSREQUEST._serialized_end=1643
  _QUERYDEPOSITSRESPONSE._serialized_start=1646
  _QUERYDEPOSITSRESPONSE._serialized_end=1783
  _QUERYTALLYRESULTREQUEST._serialized_start=1785
  _QUERYTALLYRESULTREQUEST._serialized_end=1831
  _QUERYTALLYRESULTRESPONSE._serialized_start=1833
  _QUERYTALLYRESULTRESPONSE._serialized_end=1913
  _QUERY._serialized_start=1916
  _QUERY._serialized_end=3152
# @@protoc_insertion_point(module_scope)
