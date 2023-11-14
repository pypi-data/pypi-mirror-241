"""
Generated protobuf files for the library.
"""

# Standard
import os

# First Party
# Get the import helper from the core
from autoai_ts_libs.deps.watson_core.data_model.protobufs import import_protobufs

proto_dir = os.path.dirname(os.path.realpath(__file__))

# Import all probobufs as extensions to the core
import_protobufs(proto_dir, __name__, globals())
