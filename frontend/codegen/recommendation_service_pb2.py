# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: recommendation_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1crecommendation_service.proto\x12\x0erecommendation\"7\n\x15RecommendationRequest\x12\x10\n\x08\x63\x61tegory\x18\x01 \x03(\t\x12\x0c\n\x04\x63ity\x18\x02 \x01(\t\"Y\n\x16RecommendationResponse\x12?\n\x0frecommendations\x18\x01 \x03(\x0b\x32&.recommendation.BusinessRecommendation\"\xbb\x01\n\x16\x42usinessRecommendation\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x02 \x01(\t\x12\x0e\n\x06rating\x18\x03 \x01(\x02\x12\x14\n\x0creview_count\x18\x04 \x01(\x05\x12\x0c\n\x04\x63ity\x18\x05 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x06 \x01(\t\x12\r\n\x05phone\x18\x07 \x01(\t\x12\r\n\x05price\x18\x08 \x01(\t\x12\x11\n\timage_url\x18\t \x01(\t\x12\x0b\n\x03url\x18\n \x01(\t2|\n\x15RecommendationService\x12\x63\n\x12GetRecommendations\x12%.recommendation.RecommendationRequest\x1a&.recommendation.RecommendationResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'recommendation_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_RECOMMENDATIONREQUEST']._serialized_start=48
  _globals['_RECOMMENDATIONREQUEST']._serialized_end=103
  _globals['_RECOMMENDATIONRESPONSE']._serialized_start=105
  _globals['_RECOMMENDATIONRESPONSE']._serialized_end=194
  _globals['_BUSINESSRECOMMENDATION']._serialized_start=197
  _globals['_BUSINESSRECOMMENDATION']._serialized_end=384
  _globals['_RECOMMENDATIONSERVICE']._serialized_start=386
  _globals['_RECOMMENDATIONSERVICE']._serialized_end=510
# @@protoc_insertion_point(module_scope)
