# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: quant_quotation_sys.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='quant_quotation_sys.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x19quant_quotation_sys.proto\"\xa4\x05\n\x08TickData\x12\x0e\n\x06symbol\x18\x01 \x02(\t\x12\x10\n\x08\x65xchange\x18\x02 \x02(\t\x12\x11\n\tlastPrice\x18\x03 \x02(\x01\x12\x12\n\nlastVolume\x18\x04 \x01(\x03\x12\x0e\n\x06volume\x18\x05 \x02(\x03\x12\x14\n\x0copenInterest\x18\x06 \x02(\x01\x12\x0c\n\x04time\x18\x07 \x02(\t\x12\x0c\n\x04\x64\x61te\x18\x08 \x02(\t\x12\x11\n\topenPrice\x18\t \x02(\x01\x12\x11\n\thighPrice\x18\n \x02(\x01\x12\x10\n\x08lowPrice\x18\x0b \x02(\x01\x12\x15\n\rpreClosePrice\x18\x0c \x02(\x01\x12\x12\n\nupperLimit\x18\r \x02(\x01\x12\x12\n\nlowerLimit\x18\x0e \x02(\x01\x12\x11\n\tbidPrice1\x18\x0f \x02(\x01\x12\x11\n\tbidPrice2\x18\x10 \x01(\x01\x12\x11\n\tbidPrice3\x18\x11 \x01(\x01\x12\x11\n\tbidPrice4\x18\x12 \x01(\x01\x12\x11\n\tbidPrice5\x18\x13 \x01(\x01\x12\x11\n\taskPrice1\x18\x14 \x02(\x01\x12\x11\n\taskPrice2\x18\x15 \x01(\x01\x12\x11\n\taskPrice3\x18\x16 \x01(\x01\x12\x11\n\taskPrice4\x18\x17 \x01(\x01\x12\x11\n\taskPrice5\x18\x18 \x01(\x01\x12\x12\n\nbidVolume1\x18\x19 \x02(\x03\x12\x12\n\nbidVolume2\x18\x1a \x01(\x03\x12\x12\n\nbidVolume3\x18\x1b \x01(\x03\x12\x12\n\nbidVolume4\x18\x1c \x01(\x03\x12\x12\n\nbidVolume5\x18\x1d \x01(\x03\x12\x12\n\naskVolume1\x18\x1e \x02(\x03\x12\x12\n\naskVolume2\x18\x1f \x01(\x03\x12\x12\n\naskVolume3\x18  \x01(\x03\x12\x12\n\naskVolume4\x18! \x01(\x03\x12\x12\n\naskVolume5\x18\" \x01(\x03\x12\x10\n\x08\x64\x61taType\x18# \x01(\t')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_TICKDATA = _descriptor.Descriptor(
  name='TickData',
  full_name='TickData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='symbol', full_name='TickData.symbol', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='exchange', full_name='TickData.exchange', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lastPrice', full_name='TickData.lastPrice', index=2,
      number=3, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lastVolume', full_name='TickData.lastVolume', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='volume', full_name='TickData.volume', index=4,
      number=5, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='openInterest', full_name='TickData.openInterest', index=5,
      number=6, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time', full_name='TickData.time', index=6,
      number=7, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='date', full_name='TickData.date', index=7,
      number=8, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='openPrice', full_name='TickData.openPrice', index=8,
      number=9, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='highPrice', full_name='TickData.highPrice', index=9,
      number=10, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lowPrice', full_name='TickData.lowPrice', index=10,
      number=11, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='preClosePrice', full_name='TickData.preClosePrice', index=11,
      number=12, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='upperLimit', full_name='TickData.upperLimit', index=12,
      number=13, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lowerLimit', full_name='TickData.lowerLimit', index=13,
      number=14, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bidPrice1', full_name='TickData.bidPrice1', index=14,
      number=15, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bidPrice2', full_name='TickData.bidPrice2', index=15,
      number=16, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bidPrice3', full_name='TickData.bidPrice3', index=16,
      number=17, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bidPrice4', full_name='TickData.bidPrice4', index=17,
      number=18, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bidPrice5', full_name='TickData.bidPrice5', index=18,
      number=19, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='askPrice1', full_name='TickData.askPrice1', index=19,
      number=20, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='askPrice2', full_name='TickData.askPrice2', index=20,
      number=21, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='askPrice3', full_name='TickData.askPrice3', index=21,
      number=22, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='askPrice4', full_name='TickData.askPrice4', index=22,
      number=23, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='askPrice5', full_name='TickData.askPrice5', index=23,
      number=24, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bidVolume1', full_name='TickData.bidVolume1', index=24,
      number=25, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bidVolume2', full_name='TickData.bidVolume2', index=25,
      number=26, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bidVolume3', full_name='TickData.bidVolume3', index=26,
      number=27, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bidVolume4', full_name='TickData.bidVolume4', index=27,
      number=28, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bidVolume5', full_name='TickData.bidVolume5', index=28,
      number=29, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='askVolume1', full_name='TickData.askVolume1', index=29,
      number=30, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='askVolume2', full_name='TickData.askVolume2', index=30,
      number=31, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='askVolume3', full_name='TickData.askVolume3', index=31,
      number=32, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='askVolume4', full_name='TickData.askVolume4', index=32,
      number=33, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='askVolume5', full_name='TickData.askVolume5', index=33,
      number=34, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dataType', full_name='TickData.dataType', index=34,
      number=35, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=30,
  serialized_end=706,
)

DESCRIPTOR.message_types_by_name['TickData'] = _TICKDATA

TickData = _reflection.GeneratedProtocolMessageType('TickData', (_message.Message,), dict(
  DESCRIPTOR = _TICKDATA,
  __module__ = 'quant_quotation_sys_pb2'
  # @@protoc_insertion_point(class_scope:TickData)
  ))
_sym_db.RegisterMessage(TickData)


# @@protoc_insertion_point(module_scope)
