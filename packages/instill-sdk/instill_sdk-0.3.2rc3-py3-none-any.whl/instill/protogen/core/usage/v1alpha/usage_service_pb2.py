# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: core/usage/v1alpha/usage_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from core.usage.v1alpha import usage_pb2 as core_dot_usage_dot_v1alpha_dot_usage__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&core/usage/v1alpha/usage_service.proto\x12\x12\x63ore.usage.v1alpha\x1a\x1e\x63ore/usage/v1alpha/usage.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto2\xde\x04\n\x0cUsageService\x12\x8b\x01\n\x08Liveness\x12#.core.usage.v1alpha.LivenessRequest\x1a$.core.usage.v1alpha.LivenessResponse\"4\x82\xd3\xe4\x93\x02.\x12\x13/v1alpha/__livenessZ\x17\x12\x15/v1alpha/health/usage\x12v\n\tReadiness\x12$.core.usage.v1alpha.ReadinessRequest\x1a%.core.usage.v1alpha.ReadinessResponse\"\x1c\x82\xd3\xe4\x93\x02\x16\x12\x14/v1alpha/__readiness\x12\x92\x01\n\rCreateSession\x12(.core.usage.v1alpha.CreateSessionRequest\x1a).core.usage.v1alpha.CreateSessionResponse\",\xda\x41\x07session\x82\xd3\xe4\x93\x02\x1c\"\x11/v1alpha/sessions:\x07session\x12\x9b\x01\n\x11SendSessionReport\x12,.core.usage.v1alpha.SendSessionReportRequest\x1a-.core.usage.v1alpha.SendSessionReportResponse\")\xda\x41\x06report\x82\xd3\xe4\x93\x02\x1a\"\x10/v1alpha/reports:\x06report\x1a\x15\xca\x41\x12usage.instill.techB\xd8\x01\n\x16\x63om.core.usage.v1alphaB\x11UsageServiceProtoP\x01ZAgithub.com/instill-ai/protogen-go/core/usage/v1alpha;usagev1alpha\xa2\x02\x03\x43UX\xaa\x02\x12\x43ore.Usage.V1alpha\xca\x02\x12\x43ore\\Usage\\V1alpha\xe2\x02\x1e\x43ore\\Usage\\V1alpha\\GPBMetadata\xea\x02\x14\x43ore::Usage::V1alphab\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'core.usage.v1alpha.usage_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\026com.core.usage.v1alphaB\021UsageServiceProtoP\001ZAgithub.com/instill-ai/protogen-go/core/usage/v1alpha;usagev1alpha\242\002\003CUX\252\002\022Core.Usage.V1alpha\312\002\022Core\\Usage\\V1alpha\342\002\036Core\\Usage\\V1alpha\\GPBMetadata\352\002\024Core::Usage::V1alpha'
  _USAGESERVICE._options = None
  _USAGESERVICE._serialized_options = b'\312A\022usage.instill.tech'
  _USAGESERVICE.methods_by_name['Liveness']._options = None
  _USAGESERVICE.methods_by_name['Liveness']._serialized_options = b'\202\323\344\223\002.\022\023/v1alpha/__livenessZ\027\022\025/v1alpha/health/usage'
  _USAGESERVICE.methods_by_name['Readiness']._options = None
  _USAGESERVICE.methods_by_name['Readiness']._serialized_options = b'\202\323\344\223\002\026\022\024/v1alpha/__readiness'
  _USAGESERVICE.methods_by_name['CreateSession']._options = None
  _USAGESERVICE.methods_by_name['CreateSession']._serialized_options = b'\332A\007session\202\323\344\223\002\034\"\021/v1alpha/sessions:\007session'
  _USAGESERVICE.methods_by_name['SendSessionReport']._options = None
  _USAGESERVICE.methods_by_name['SendSessionReport']._serialized_options = b'\332A\006report\202\323\344\223\002\032\"\020/v1alpha/reports:\006report'
  _globals['_USAGESERVICE']._serialized_start=150
  _globals['_USAGESERVICE']._serialized_end=756
# @@protoc_insertion_point(module_scope)
