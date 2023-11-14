# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vdp/pipeline/v1alpha/pipeline_private_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from vdp.pipeline.v1alpha import operator_definition_pb2 as vdp_dot_pipeline_dot_v1alpha_dot_operator__definition__pb2
from vdp.pipeline.v1alpha import pipeline_pb2 as vdp_dot_pipeline_dot_v1alpha_dot_pipeline__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3vdp/pipeline/v1alpha/pipeline_private_service.proto\x12\x14vdp.pipeline.v1alpha\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a.vdp/pipeline/v1alpha/operator_definition.proto\x1a#vdp/pipeline/v1alpha/pipeline.proto2\x8d\x06\n\x16PipelinePrivateService\x12\x99\x01\n\x12ListPipelinesAdmin\x12/.vdp.pipeline.v1alpha.ListPipelinesAdminRequest\x1a\x30.vdp.pipeline.v1alpha.ListPipelinesAdminResponse\" \x82\xd3\xe4\x93\x02\x1a\x12\x18/v1alpha/admin/pipelines\x12\xbd\x01\n\x13LookUpPipelineAdmin\x12\x30.vdp.pipeline.v1alpha.LookUpPipelineAdminRequest\x1a\x31.vdp.pipeline.v1alpha.LookUpPipelineAdminResponse\"A\xda\x41\tpermalink\x82\xd3\xe4\x93\x02/\x12-/v1alpha/admin/{permalink=pipelines/*}/lookUp\x12\xe6\x01\n\x1dLookUpOperatorDefinitionAdmin\x12:.vdp.pipeline.v1alpha.LookUpOperatorDefinitionAdminRequest\x1a;.vdp.pipeline.v1alpha.LookUpOperatorDefinitionAdminResponse\"L\xda\x41\tpermalink\x82\xd3\xe4\x93\x02:\x12\x38/v1alpha/admin/{permalink=operator-definitions/*}/lookUp\x12\xad\x01\n\x19ListPipelineReleasesAdmin\x12\x36.vdp.pipeline.v1alpha.ListPipelineReleasesAdminRequest\x1a\x37.vdp.pipeline.v1alpha.ListPipelineReleasesAdminResponse\"\x1f\x82\xd3\xe4\x93\x02\x19\x12\x17/v1alpha/admin/releasesB\xf1\x01\n\x18\x63om.vdp.pipeline.v1alphaB\x1bPipelinePrivateServiceProtoP\x01ZFgithub.com/instill-ai/protogen-go/vdp/pipeline/v1alpha;pipelinev1alpha\xa2\x02\x03VPX\xaa\x02\x14Vdp.Pipeline.V1alpha\xca\x02\x14Vdp\\Pipeline\\V1alpha\xe2\x02 Vdp\\Pipeline\\V1alpha\\GPBMetadata\xea\x02\x16Vdp::Pipeline::V1alphab\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'vdp.pipeline.v1alpha.pipeline_private_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\030com.vdp.pipeline.v1alphaB\033PipelinePrivateServiceProtoP\001ZFgithub.com/instill-ai/protogen-go/vdp/pipeline/v1alpha;pipelinev1alpha\242\002\003VPX\252\002\024Vdp.Pipeline.V1alpha\312\002\024Vdp\\Pipeline\\V1alpha\342\002 Vdp\\Pipeline\\V1alpha\\GPBMetadata\352\002\026Vdp::Pipeline::V1alpha'
  _PIPELINEPRIVATESERVICE.methods_by_name['ListPipelinesAdmin']._options = None
  _PIPELINEPRIVATESERVICE.methods_by_name['ListPipelinesAdmin']._serialized_options = b'\202\323\344\223\002\032\022\030/v1alpha/admin/pipelines'
  _PIPELINEPRIVATESERVICE.methods_by_name['LookUpPipelineAdmin']._options = None
  _PIPELINEPRIVATESERVICE.methods_by_name['LookUpPipelineAdmin']._serialized_options = b'\332A\tpermalink\202\323\344\223\002/\022-/v1alpha/admin/{permalink=pipelines/*}/lookUp'
  _PIPELINEPRIVATESERVICE.methods_by_name['LookUpOperatorDefinitionAdmin']._options = None
  _PIPELINEPRIVATESERVICE.methods_by_name['LookUpOperatorDefinitionAdmin']._serialized_options = b'\332A\tpermalink\202\323\344\223\002:\0228/v1alpha/admin/{permalink=operator-definitions/*}/lookUp'
  _PIPELINEPRIVATESERVICE.methods_by_name['ListPipelineReleasesAdmin']._options = None
  _PIPELINEPRIVATESERVICE.methods_by_name['ListPipelineReleasesAdmin']._serialized_options = b'\202\323\344\223\002\031\022\027/v1alpha/admin/releases'
  _globals['_PIPELINEPRIVATESERVICE']._serialized_start=218
  _globals['_PIPELINEPRIVATESERVICE']._serialized_end=999
# @@protoc_insertion_point(module_scope)
