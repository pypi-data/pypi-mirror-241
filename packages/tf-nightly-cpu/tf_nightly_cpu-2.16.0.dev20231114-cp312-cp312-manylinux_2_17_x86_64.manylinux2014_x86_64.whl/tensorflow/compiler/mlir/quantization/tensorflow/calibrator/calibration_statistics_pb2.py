# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/compiler/mlir/quantization/tensorflow/calibrator/calibration_statistics.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nXtensorflow/compiler/mlir/quantization/tensorflow/calibrator/calibration_statistics.proto\x12\x15tensorflow.calibrator\"\x9c\x04\n\x15\x43\x61librationStatistics\x12Y\n\x12min_max_statistics\x18\x01 \x01(\x0b\x32=.tensorflow.calibrator.CalibrationStatistics.MinMaxStatistics\x12h\n\x1a\x61verage_min_max_statistics\x18\x02 \x01(\x0b\x32\x44.tensorflow.calibrator.CalibrationStatistics.AverageMinMaxStatistics\x12^\n\x14histogram_statistics\x18\x03 \x01(\x0b\x32@.tensorflow.calibrator.CalibrationStatistics.HistogramStatistics\x1a:\n\x10MinMaxStatistics\x12\x12\n\nglobal_min\x18\x01 \x01(\x02\x12\x12\n\nglobal_max\x18\x02 \x01(\x02\x1aP\n\x17\x41verageMinMaxStatistics\x12\x0f\n\x07min_sum\x18\x01 \x01(\x02\x12\x0f\n\x07max_sum\x18\x02 \x01(\x02\x12\x13\n\x0bnum_samples\x18\x03 \x01(\x05\x1aP\n\x13HistogramStatistics\x12\x11\n\tbin_width\x18\x01 \x01(\x02\x12\x13\n\x0blower_bound\x18\x02 \x01(\x02\x12\x11\n\thist_freq\x18\x03 \x03(\x03\x42\x03\xf8\x01\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tensorflow.compiler.mlir.quantization.tensorflow.calibrator.calibration_statistics_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\370\001\001'
  _CALIBRATIONSTATISTICS._serialized_start=116
  _CALIBRATIONSTATISTICS._serialized_end=656
  _CALIBRATIONSTATISTICS_MINMAXSTATISTICS._serialized_start=434
  _CALIBRATIONSTATISTICS_MINMAXSTATISTICS._serialized_end=492
  _CALIBRATIONSTATISTICS_AVERAGEMINMAXSTATISTICS._serialized_start=494
  _CALIBRATIONSTATISTICS_AVERAGEMINMAXSTATISTICS._serialized_end=574
  _CALIBRATIONSTATISTICS_HISTOGRAMSTATISTICS._serialized_start=576
  _CALIBRATIONSTATISTICS_HISTOGRAMSTATISTICS._serialized_end=656
# @@protoc_insertion_point(module_scope)
