# Copyright 2015 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Implementation of the TF-Keras API, the high-level API of TensorFlow.

Detailed documentation and user guides are available at
[keras.io](https://keras.io).
"""

from tf_keras import applications
from tf_keras import distribute
from tf_keras import models
from tf_keras.engine.input_layer import Input
from tf_keras.engine.sequential import Sequential
from tf_keras.engine.training import Model
from tf_keras.testing_infra import test_utils

# isort: off

from tensorflow.python import tf2
from tensorflow.python.util.tf_export import keras_export

__version__ = "2.14.1"

keras_export("keras.__version__").export_constant(__name__, "__version__")
