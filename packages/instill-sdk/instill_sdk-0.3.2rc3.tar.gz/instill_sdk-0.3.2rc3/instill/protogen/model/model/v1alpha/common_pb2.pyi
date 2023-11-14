"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class BoundingBox(google.protobuf.message.Message):
    """BoundingBox represents the bounding box data structure"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TOP_FIELD_NUMBER: builtins.int
    LEFT_FIELD_NUMBER: builtins.int
    WIDTH_FIELD_NUMBER: builtins.int
    HEIGHT_FIELD_NUMBER: builtins.int
    top: builtins.float
    """Bounding box top y-axis value"""
    left: builtins.float
    """Bounding box left x-axis value"""
    width: builtins.float
    """Bounding box width value"""
    height: builtins.float
    """Bounding box height value"""
    def __init__(
        self,
        *,
        top: builtins.float = ...,
        left: builtins.float = ...,
        width: builtins.float = ...,
        height: builtins.float = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["height", b"height", "left", b"left", "top", b"top", "width", b"width"]) -> None: ...

global___BoundingBox = BoundingBox
