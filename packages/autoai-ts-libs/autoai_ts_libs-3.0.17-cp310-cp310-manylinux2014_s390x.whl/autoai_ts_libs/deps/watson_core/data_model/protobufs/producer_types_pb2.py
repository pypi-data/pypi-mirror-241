# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: producer-types.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14producer-types.proto\x12\x1dwatson_core_data_model.common\"+\n\nProducerId\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\"P\n\x10ProducerPriority\x12<\n\tproducers\x18\x01 \x03(\x0b\x32).watson_core_data_model.common.ProducerIdb\x06proto3')



_PRODUCERID = DESCRIPTOR.message_types_by_name['ProducerId']
_PRODUCERPRIORITY = DESCRIPTOR.message_types_by_name['ProducerPriority']
ProducerId = _reflection.GeneratedProtocolMessageType('ProducerId', (_message.Message,), {
  'DESCRIPTOR' : _PRODUCERID,
  '__module__' : 'producer_types_pb2'
  # @@protoc_insertion_point(class_scope:watson_core_data_model.common.ProducerId)
  })
_sym_db.RegisterMessage(ProducerId)

ProducerPriority = _reflection.GeneratedProtocolMessageType('ProducerPriority', (_message.Message,), {
  'DESCRIPTOR' : _PRODUCERPRIORITY,
  '__module__' : 'producer_types_pb2'
  # @@protoc_insertion_point(class_scope:watson_core_data_model.common.ProducerPriority)
  })
_sym_db.RegisterMessage(ProducerPriority)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PRODUCERID._serialized_start=55
  _PRODUCERID._serialized_end=98
  _PRODUCERPRIORITY._serialized_start=100
  _PRODUCERPRIORITY._serialized_end=180
# @@protoc_insertion_point(module_scope)
