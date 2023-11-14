#
#   Copyright 2022 Logical Clocks AB
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#


class Tensor:
    """Metadata object representing a tensor in the schema for a model."""

    def __init__(self, type, shape, name=None, description=None):
        self.type = str(type)

        self.shape = str(shape)

        if name is not None:
            self.name = str(name)

        if description is not None:
            self.description = str(description)
