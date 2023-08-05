"""
    Copyright 2020 Ext-Creators

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from collections import namedtuple


__version__ = "2021.04.13"

_VersionInfo = namedtuple("_VersionInfo", "major minor micro releaselevel serial")
version_info = _VersionInfo(major=2021, minor=4, micro=13, releaselevel="stable", serial=0)
