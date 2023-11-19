# File: /example/fragments/doublec.py
# Project: gtklara
# File Created: 18-11-2023 15:39:42
# Author: Clay Risser
# -----
# BitSpur (c) Copyright 2022 - 2023
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

from gtklara import GTKlara, State
from ..views import Home
from ..fragments import Container, Button


class DoubleC(GTKlara):
    def __init__(self, children=[], **kwargs):
        self.c = State(Container(Container(children)))
        super().__init__(self.c, kwargs)

    def render(self):
        return Container(Button(self.Children, on_clicked=self.handle_clicked))

    def handle_clicked(self, widget):
        self.c.set(Button())
